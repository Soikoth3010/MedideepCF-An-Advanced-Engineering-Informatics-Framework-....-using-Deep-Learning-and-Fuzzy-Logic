## Dataset Organization

This directory contains the dataset structure used in the MedideepCF framework.

### Directory Structure

- `raw/`  
  Contains original RGB maize leaf images collected from real agricultural fields.  
  Images correspond to four classes: Blight, Common Rust, Gray Leaf Spot, and Healthy.

- `masks/`  
  Contains pixel-level lesion segmentation masks annotated using polygon-based labeling.  
  Each mask aligns one-to-one with its corresponding raw image.

### Notes on Data Availability

Due to data ownership and ethical considerations, the full-resolution dataset used in the manuscript is not publicly redistributed.  
However, the directory structure, naming conventions, and annotation format are preserved to ensure reproducibility of the pipeline.

Researchers may substitute this directory with their own maize leaf datasets following the same structure.

### Reference

The dataset corresponds to the experimental setup described in Section 3 (Methodology) of the manuscript.


