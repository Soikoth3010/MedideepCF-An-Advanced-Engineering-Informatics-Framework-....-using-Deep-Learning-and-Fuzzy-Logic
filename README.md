MedideepCF

An Advanced Engineering Informatics Framework for Interpretable Maize Leaf Disease Detection and Severity Estimation using Deep Learning and Fuzzy Logic

Version: v1.0
Author: Soikoth3010
DOI: 10.5281/zenodo.18405364

Transparency Note

This repository provides pretrained models and an end-to-end inference pipeline for the MedideepCF framework.
The full training pipeline is not publicly released; however, the provided scripts enable reproduction and verification of all reported inference results presented in the manuscript.

Overview

MedideepCF is a research-grade, interpretable AI framework for maize leaf disease detection and severity estimation.
It integrates semantic segmentation, attention-enhanced classification, and fuzzy logic–based reasoning within a unified pipeline.

The framework combines:

DeepLabV3+ (ResNet-50) for pixel-level lesion segmentation

EfficientNet-B0 with CBAM for robust disease classification

Mamdani-type fuzzy inference system for interpretable severity estimation

Repository Structure

The repository is organized to support clarity, transparency, and reproducibility:

data/        Dataset references and annotations
models/      Pretrained segmentation and classification models
inference/   End-to-end inference scripts

Repository Contents
Dataset

Model Dataset

RGB maize leaf images used for classification

Four classes:

Blight

Common Rust

Gray Leaf Spot

Healthy

Masked Dataset

Polygon-based segmentation masks created using Labelme

Used for training and validating the DeepLabV3+ segmentation module

Enables pixel-level lesion localization and severity reasoning

MedideepCF Pipeline Summary
1. Preprocessing

Channel-wise median filtering for noise suppression

Linear contrast enhancement for improved lesion visibility

2. Semantic Segmentation

DeepLabV3+ with ResNet-50 backbone

Generates binary lesion masks for spatial interpretability

3. Disease Classification

EfficientNet-B0 enhanced with CBAM attention

Robust to illumination variation and field noise

4. Severity Estimation

Mamdani-type fuzzy inference system

Inputs: lesion area, lesion count, color deviation

Output: interpretable severity score (0–100)

Performance Highlights

Accuracy: 96.42%

F1-Score: 96.51%

Evaluated using 4-fold stratified cross-validation

Strong performance in both segmentation and classification

Lightweight and CPU-friendly inference

Inference Demo

The inference/run_demo.py script demonstrates the complete MedideepCF pipeline on a single input image, including preprocessing, segmentation, classification, and severity estimation using pretrained models.

This script is intended for:

Verifying model compatibility

Demonstrating end-to-end inference flow

Supporting qualitative evaluation

Citation

If you use MedideepCF in your research, please cite:

Soikoth, S. (2026). MedideepCF – An Advanced Engineering Informatics Framework Using Deep Learning and Fuzzy Logic. Zenodo. https://doi.org/10.5281/zenodo.18405364
