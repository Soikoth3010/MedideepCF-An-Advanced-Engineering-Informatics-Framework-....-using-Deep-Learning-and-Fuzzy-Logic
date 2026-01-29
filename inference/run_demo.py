import os
import torch
import cv2
import numpy as np
import argparse

from torchvision import transforms
from part4_model import MediDeepCFNet
from part5_fuzzy import calculate_severity
from part1_setup import decode_segmap, get_device

# -----------------------------
# Configuration
# -----------------------------
CLASS_NAMES = [
    "Corn_Health",
    "Corn_Blight",
    "Corn_Common_Rust",
    "Corn_Gray_Leaf_Spot"
]

IMAGE_SIZE = 224

# -----------------------------
# Preprocessing
# -----------------------------
def get_inference_transform():
    return transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=(0.485, 0.456, 0.406),
            std=(0.229, 0.224, 0.225)
        )
    ])

# -----------------------------
# Model Loader
# -----------------------------
def load_model(model_path, device):
    model = MediDeepCFNet(num_classes=len(CLASS_NAMES))
    checkpoint = torch.load(model_path, map_location=device)

    if isinstance(checkpoint, dict):
        model.load_state_dict(checkpoint)
    else:
        model.load_state_dict(checkpoint.state_dict())

    model.to(device)
    model.eval()
    return model

# -----------------------------
# Inference Pipeline
# -----------------------------
@torch.no_grad()
def run_inference(model, image_path, device):
    image_bgr = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    transform = get_inference_transform()
    image_tensor = transform(image_rgb).unsqueeze(0).to(device)

    seg_logits, class_probs = model(image_tensor)

    # Segmentation
    seg_mask = torch.argmax(seg_logits, dim=1).squeeze(0).cpu().numpy()

    # Classification
    class_id = torch.argmax(class_probs, dim=1).remember = class_id = torch.argmax(class_probs, dim=1).item()
    class_name = CLASS_NAMES[class_id]
    confidence = class_probs[0, class_id].item()

    # Severity estimation
    severity_info = calculate_severity(seg_mask)

    return {
        "class_id": class_id,
        "class_name": class_name,
        "confidence": round(confidence * 100, 2),
        "segmentation_mask": seg_mask,
        "severity": severity_info,
        "original_image": image_rgb
    }

# -----------------------------
# Visualization
# -----------------------------
def save_outputs(result, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    seg_color = decode_segmap(result["segmentation_mask"])
    overlay = cv2.addWeighted(
        result["original_image"], 0.6,
        seg_color, 0.4, 0
    )

    cv2.imwrite(
        os.path.join(output_dir, "segmentation_overlay.png"),
        cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR)
    )

    with open(os.path.join(output_dir, "prediction.txt"), "w") as f:
        f.write(f"Disease Class: {result['class_name']}\n")
        f.write(f"Confidence: {result['confidence']}%\n\n")
        f.write("Severity Analysis:\n")
        for cls, info in result["severity"].items():
            f.write(f"  Class {cls}: {info['percent']}% ({info['severity']})\n")

# -----------------------------
# Main
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="MediDeepCF Inference Demo")
    parser.add_argument("--image", required=True, help="Path to input leaf image")
    parser.add_argument("--model", required=True, help="Path to pretrained model")
    parser.add_argument("--output", default="outputs", help="Output directory")

    args = parser.parse_args()

    device = get_device()
    model = load_model(args.model, device)

    result = run_inference(model, args.image, device)
    save_outputs(result, args.output)

    print("Inference completed successfully.")
    print(f"Predicted Class: {result['class_name']} ({result['confidence']}%)")

if __name__ == "__main__":
    main()

