# Progress Tracker: Precision Meets Efficiency - Quantization in Radiology AI

**Version:** 1.0
**Date:** 2025-04-15

**Status Key:** `NS` (Not Started), `IP` (In Progress), `C` (Completed), `B` (Blocked)

| Task ID | Category      | Task Description                                                     | Status | Assignee | Due Date | Notes / Link                                     |
| :------ | :------------ | :------------------------------------------------------------------- | :----- | :------- | :------- | :----------------------------------------------- |
| **SETUP & FOUNDATION** |               |                                                                      |        |          |          |                                                  |
| T01     | Environment   | Verify/Finalize `environment.yml` dependencies                       | C      | Cascade  |          | `environment.yml`                              |
| T02     | Environment   | Create and test Conda environment build                            | NS     | User     |          | `conda env create -f environment.yml`          |
| T03     | Data          | Download Chest X-ray dataset (e.g., NIH ChestX-ray14)                | NS     | User     |          | See `data/README_CXR.md`                       |
| T04     | Data          | Download MRI Segmentation dataset (e.g., BraTS)                    | NS     | User     |          | See `data/README_MRI.md`                       |
| T05     | Config        | Update `config_cxr.yaml` with actual CXR dataset path                | NS     | User     |          | `code/benchmarks/cxr_classification/config_cxr.yaml` |
| T06     | Config        | Update `config_mri.yaml` with actual MRI dataset path                | NS     | User     |          | `code/benchmarks/mri_segmentation/config_mri.yaml` |
| T07     | Code: Common  | Implement core logic in `quantization_wrappers.py`                 | NS     | User     |          | `code/benchmarks/common/quantization_wrappers.py`  |
| T08     | Code: Common  | Implement core logic in `evaluation_metrics.py`                    | NS     | User     |          | `code/benchmarks/common/evaluation_metrics.py`   |
| T09     | Manuscript    | Draft Abstract (`00_abstract.tex`)                                   | NS     | User     |          | `manuscript/sections/00_abstract.tex`          |
| T10     | Manuscript    | Draft Introduction (`01_introduction.tex`)                           | NS     | User     |          | `manuscript/sections/01_introduction.tex`      |
| T11     | Manuscript    | Draft Fundamentals (`02_fundamentals.tex`)                           | NS     | User     |          | `manuscript/sections/02_fundamentals.tex`      |
| T12     | Manuscript    | Draft Techniques (`03_techniques.tex`)                               | NS     | User     |          | `manuscript/sections/03_techniques.tex`        |
| T13     | Manuscript    | Populate `bibliography.bib` with initial key references              | NS     | User     |          | `manuscript/bibliography.bib`                  |
| **CORE BENCHMARKING** |               |                                                                      |        |          |          |                                                  |
| T14     | Code: CXR     | Implement `data_loader_cxr.py`                                       | NS     | User     |          | `code/benchmarks/cxr_classification/data_loader_cxr.py` |
| T15     | Code: CXR     | Finalize/Test `model_densenet.py` integration                      | NS     | User     |          | `code/benchmarks/cxr_classification/model_densenet.py` |
| T16     | Code: CXR     | Implement main logic in `run_cxr_benchmark.py`                       | NS     | User     |          | `code/benchmarks/cxr_classification/run_cxr_benchmark.py` |
| T17     | Results: CXR  | Run CXR benchmark script and generate `cxr_benchmark_results.csv`    | NS     | User     |          | `results/processed/`                           |
| T18     | Code: MRI     | Implement `data_loader_mri.py` (handle 3D NIfTI)                   | NS     | User     |          | `code/benchmarks/mri_segmentation/data_loader_mri.py` |
| T19     | Code: MRI     | Finalize/Test `model_unet.py` integration                          | NS     | User     |          | `code/benchmarks/mri_segmentation/model_unet.py` |
| T20     | Code: MRI     | Implement main logic in `run_mri_benchmark.py`                       | NS     | User     |          | `code/benchmarks/mri_segmentation/run_mri_benchmark.py` |
| T21     | Results: MRI  | Run MRI benchmark script and generate `mri_benchmark_results.csv`    | NS     | User     |          | `results/processed/`                           |
| T22     | Results       | Analyze combined benchmark results                                   | NS     | User     |          |                                                  |
| T23     | Manuscript    | Draft Applications section (`04_applications.tex`)                   | NS     | User     |          | `manuscript/sections/04_applications.tex`      |
| **REFINEMENT & DOCS** |               |                                                                      |        |          |          |                                                  |
| T24     | Code          | Refactor/Comment benchmark code                                        | NS     | User     |          | `code/benchmarks/`                             |
| T25     | Results       | Generate figures/tables from results                                 | NS     | User     |          | `docs/figures/`, `docs/tables/`                |
| T26     | Manuscript    | Draft Ethical/Practical section (`05_ethical_practical.tex`)       | NS     | User     |          | `manuscript/sections/05_ethical_practical.tex` |
| T27     | Manuscript    | Draft Future Directions section (`06_future_directions.tex`)         | NS     | User     |          | `manuscript/sections/06_future_directions.tex` |
| T28     | Manuscript    | Draft Conclusion section (`07_conclusion.tex`)                       | NS     | User     |          | `manuscript/sections/07_conclusion.tex`        |
| T29     | Manuscript    | Finalize References (`bibliography.bib`)                             | NS     | User     |          | `manuscript/bibliography.bib`                  |
| T30     | Docs          | Complete `CLAIM_Checklist.md`                                        | NS     | User     |          | `docs/CLAIM_Checklist.md`                      |
| T31     | Docs          | Complete `Quantization_Readiness_Scorecard.md`                       | NS     | User     |          | `docs/Quantization_Readiness_Scorecard.md`     |
| T32     | Manuscript    | Review and revise full manuscript draft                              | NS     | User     |          | `manuscript/main.tex`                          |
| **REVIEW & FINALIZATION** |           |                                                                      |        |          |          |                                                  |
| T33     | Review        | Internal review of manuscript and code                               | NS     | User     |          |                                                  |
| T34     | Revision      | Incorporate review feedback                                          | NS     | User     |          |                                                  |
| T35     | QA            | Final proofread of manuscript                                        | NS     | User     |          | `manuscript/main.tex`                          |
| T36     | QA            | Test code execution based on `README.md` instructions                | NS     | User     |          | `README.md`                                    |
| T37     | Finalization  | (Optional) Format manuscript for target journal                      | NS     | User     |          |                                                  |
| T38     | Finalization  | Final commit and push to GitHub                                      | NS     | User     |          | `git push`                                     |

