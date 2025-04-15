# Precision Meets Efficiency: Quantization in Radiology AI - Code Repository

This repository contains the code, results, and manuscript source for the paper "Precision Meets Efficiency: A Gentle Introduction to Quantization in Radiology AI".

## Overview

The project aims to:
1.  Provide a practical overview of model quantization techniques relevant to radiology AI.
2.  Benchmark the performance (accuracy, efficiency) of quantized models (using PTQ and `bitsandbytes`) against full-precision baselines on public radiology datasets (Chest X-ray classification, MRI segmentation).
3.  Offer practical resources including code examples, a quantization readiness checklist, and a CLAIM-aligned deployment guide discussion.

## Repository Structure

```
radiology_quantization_paper/
│
├── manuscript/         # LaTeX source for the paper
├── code/               # Benchmark code, notebooks, utilities
├── data/               # Instructions/links to datasets
├── results/            # Raw and processed benchmark results
├── docs/               # Supporting documents (CLAIM checklist, Scorecard)
├── .gitignore          # Git ignore file
├── environment.yml     # Conda environment specification
└── README.md           # This file
```

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd radiology_quantization_paper
    ```
2.  **Create Conda Environment:**
    ```bash
    conda env create -f environment.yml
    conda activate radio-quant
    ```
3.  **Download Data:** Follow instructions in `data/README_CXR.md` and `data/README_MRI.md` to download the necessary datasets. Update paths in benchmark configuration files if needed.

## Running Benchmarks

Navigate to the specific benchmark directory and run the main script:

```bash
# Example for Chest X-ray benchmark
cd code/benchmarks/cxr_classification
python run_cxr_benchmark.py --config config_cxr.yaml # (Config file TBD)
```

Refer to the scripts and configuration files within each `code/benchmarks/<task>` directory for details.

## Manuscript

The manuscript source is located in the `manuscript/` directory and can be compiled using a standard LaTeX distribution (e.g., TeX Live, MiKTeX).

```bash
cd manuscript
pdflatex main.tex
bibtex main # If using BibTeX
pdflatex main.tex
pdflatex main.tex
```

## Contributing

[Optional: Add contribution guidelines if applicable]

## Citation

[Optional: Add citation information once the paper is published/preprinted]

