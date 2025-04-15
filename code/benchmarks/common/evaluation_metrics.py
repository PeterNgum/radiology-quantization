# code/benchmarks/common/evaluation_metrics.py
"""
Evaluation metrics for benchmark tasks.
"""
import time
import torch
from sklearn.metrics import roc_auc_score
import numpy as np

def calculate_auc(y_true, y_pred_probs):
    """Calculates AUC score."""
    try:
        return roc_auc_score(y_true, y_pred_probs)
    except ValueError as e:
        print(f"Warning: Could not calculate AUC: {e}")
        return np.nan

def dice_coefficient(y_true_mask, y_pred_mask, smooth=1e-6):
    """Calculates Dice coefficient for segmentation."""
    # Flatten masks
    y_true_f = y_true_mask.flatten()
    y_pred_f = y_pred_mask.flatten()
    intersection = np.sum(y_true_f * y_pred_f)
    dice = (2. * intersection + smooth) / (np.sum(y_true_f) + np.sum(y_pred_f) + smooth)
    return dice

def measure_inference_time(model, dummy_input, device, repetitions=30, warmup=10):
    """Measures average inference time."""
    model.eval()
    model.to(device)
    dummy_input = dummy_input.to(device)
    times = []

    # Warmup runs
    with torch.no_grad():
        for _ in range(warmup):
            _ = model(dummy_input)

    # Timed runs
    with torch.no_grad():
        for _ in range(repetitions):
            start_time = time.perf_counter()
            _ = model(dummy_input)
            # Synchronize GPU time if using CUDA
            if device.type == 'cuda':
                torch.cuda.synchronize()
            end_time = time.perf_counter()
            times.append(end_time - start_time)

    avg_time = np.mean(times)
    std_time = np.std(times)
    return avg_time, std_time

def estimate_memory_usage(model):
    """Estimates model memory usage in MB (parameters only)."""
    mem_params = sum([param.nelement() * param.element_size() for param in model.parameters()])
    # mem_bufs = sum([buf.nelement() * buf.element_size() for buf in model.buffers()])
    # total_mem = mem_params + mem_bufs
    total_mem_mb = mem_params / (1024**2)
    return total_mem_mb

# Add other metrics as needed
