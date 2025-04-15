# data/README_MRI.md

## MRI Segmentation Dataset (e.g., BraTS)

This benchmark is designed for a 3D MRI brain segmentation dataset, such as the BraTS (Brain Tumor Segmentation) challenge dataset.

**Instructions:**

1.  **Download:** Obtain the dataset from the official source. Access often requires registration:
    *   BraTS: [https://www.med.upenn.edu/cbica/brats-challenge/](https://www.med.upenn.edu/cbica/brats-challenge/) (Look for the specific year's data, e.g., BraTS 2020, 2021)
    *   Other public MRI segmentation datasets could be adapted.

2.  **Organize:** Ensure the data is organized consistently. BraTS data typically comes structured per patient, with different MRI sequences (T1, T1ce, T2, FLAIR) and a segmentation mask (SEG).

3.  **Configure Path:** Update the `data.path` variable in `code/benchmarks/mri_segmentation/config_mri.yaml` to point to the **root directory** containing the patient folders (or the training/validation split folders).

**Expected Structure (Example for BraTS):**

```
/path/to/your/mri/dataset/ # e.g., BraTS2021/ASNR-MICCAI-BraTS2021-TrainingData-16July2021/
├── BraTS2021_00000/
│   ├── BraTS2021_00000_flair.nii.gz
│   ├── BraTS2021_00000_seg.nii.gz
│   ├── BraTS2021_00000_t1.nii.gz
│   ├── BraTS2021_00000_t1ce.nii.gz
│   └── BraTS2021_00000_t2.nii.gz
├── BraTS2021_00002/
│   └── ...
└── ...
```

**Note:** The `data_loader_mri.py` script needs full implementation to handle loading `.nii.gz` files (e.g., using `nibabel` or `SimpleITK`), potentially selecting specific modalities, and performing necessary preprocessing (like normalization, resampling, cropping/padding). The current version is a placeholder.
