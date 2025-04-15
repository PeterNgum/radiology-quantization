# data/README_CXR.md

## Chest X-ray Dataset (e.g., ChestX-ray14)

This benchmark uses a large-scale chest X-ray dataset, such as the NIH ChestX-ray14 dataset.

**Instructions:**

1.  **Download:** Obtain the dataset from the official source:
    *   NIH ChestX-ray14: [https://nihcc.app.box.com/v/ChestXray-NIHCC](https://nihcc.app.box.com/v/ChestXray-NIHCC) (Requires agreeing to terms)
    *   Other datasets like CheXpert or MIMIC-CXR could also be adapted.

2.  **Extract:** Unzip the downloaded files into a directory structure. You should have:
    *   Image files (e.g., `images_001.zip`, `images_002.zip`, ...) -> Extract to an `images/` folder.
    *   Metadata file (e.g., `Data_Entry_2017.csv`).

3.  **Configure Path:** Update the `data.path` variable in `code/benchmarks/cxr_classification/config_cxr.yaml` to point to the **root directory** containing the `images/` folder and the metadata CSV file.

**Expected Structure:**

```
/path/to/your/cxr/dataset/
├── images/
│   ├── 00000001_000.png
│   ├── 00000001_001.png
│   └── ...
├── Data_Entry_2017.csv # Or relevant metadata file
└── ... # Other files like BBox lists, etc. (may not be needed by default benchmark)
```

**Note:** The `data_loader_cxr.py` script will need to be implemented to correctly parse this structure and the metadata file. The current version is a placeholder.
