# code/benchmarks/cxr_classification/utils_cxr.py
"""Utility functions specific to the CXR benchmark."""

import torch

def evaluate_cxr(model, dataloader, device):
    """Evaluates the CXR model on the given dataloader."""
    model.eval()
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for images, labels in dataloader:
            images = images.to(device)
            # labels = labels.to(device) # Keep labels on CPU for easier aggregation

            outputs = model(images)
            # Apply sigmoid for multi-label probabilities
            preds = torch.sigmoid(outputs)

            all_preds.append(preds.cpu())
            all_labels.append(labels.cpu())

    all_preds = torch.cat(all_preds).numpy()
    all_labels = torch.cat(all_labels).numpy()

    print("Placeholder: Evaluation complete. Returning dummy data.")
    # Replace with actual calculation using metrics like AUC per class
    # return all_labels, all_preds
    return all_labels, all_preds # Return collected data
