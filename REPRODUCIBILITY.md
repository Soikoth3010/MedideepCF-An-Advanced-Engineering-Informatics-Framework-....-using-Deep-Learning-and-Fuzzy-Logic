# Reproducibility Statement

This repository supports reproducibility of the MedideepCF framework as reported in the accompanying manuscript.

## What Is Provided

- Dataset directory structure and annotation format
- Pretrained segmentation and classification model weights
- Inference script demonstrating the complete pipeline
- Detailed methodological description in the manuscript

## What Is Not Provided

- Full training scripts
- Original full-resolution dataset

These components are restricted due to data ownership and computational constraints.

## Reproducing Results

Researchers can reproduce the reported results by:
1. Organizing their dataset following the `data/` directory structure
2. Using the provided pretrained models
3. Running the inference script on test images
4. Evaluating predictions using metrics described in the manuscript

## External Dataset Generalization

The framework is designed to be dataset-agnostic.  
Users may evaluate cross-dataset generalization by substituting compatible maize leaf datasets.

## Ethical and Practical Considerations

This repository is intended for academic research and benchmarking purposes.

