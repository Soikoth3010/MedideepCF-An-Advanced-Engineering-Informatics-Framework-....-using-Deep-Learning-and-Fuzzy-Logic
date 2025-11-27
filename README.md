# MedideepCF: An Advanced Engineering Informatics Framework for Interpretable Maize Leaf Disease Detection and Severity Estimation using Deep Learning and Fuzzy Logic

This repository contains the datasets and supplementary materials associated with the paper:

**“MedideepCF: An Advanced Engineering Informatics Framework for Interpretable Maize Leaf Disease Detection and Severity Estimation Using Deep Learning and Fuzzy Logic.”**  

Submitted to **Advanced Engineering Informatics (Elsevier)**.

---

## Repository Contents

### **Model Dataset**
- Includes the **original and augmented RGB images** used for disease classification.  
- Contains four classes:
  - Blight  
  - Common Rust  
  - Gray Leaf Spot  
  - Healthy  


### **Masked Dataset**
- Includes the **polygon-annotated segmentation masks** created using **Labelme**.
- Used for training the DeepLabV3+ (ResNet-50) segmentation module.
- Enables pixel-level lesion localization for interpretability and severity estimation.

---

## Summary of the MedideepCF Framework

MedideepCF is a multi-task AI pipeline combining:

### **1. Preprocessing**
- Channel-wise **median filtering** for noise removal  
- Linear contrast enhancement for improved lesion visibility

### **2. Semantic Segmentation**
- DeepLabV3+ with **ResNet-50** backbone  
- Produces binary lesion masks for downstream analysis

### **3. Disease Classification**
- EfficientNet-B0 enhanced with **CBAM attention**  
- Robust against noise, variable lighting, and field conditions

### **4. Severity Estimation**
- A Mamdani-type **fuzzy inference system**  
- Uses lesion area, count, and color deviation  
- Outputs interpretable severity score (0–100)

---

## Performance Highlights

- **Accuracy:** 96.42%  
- **F1-Score:** 96.51%  
- Validated using **4-fold stratified cross-validation**  
- Strong performance in segmentation and classification  
- Fully interpretable and lightweight (CPU-friendly)

---

## How to Use This Dataset

### **Clone the repository:**

```bash
git clone https://github.com/Soikoth3010/MedideepCF-An-Advanced-Engineering-Informatics-Framework-....-using-Deep-Learning-and-Fuzzy-Logic.git
