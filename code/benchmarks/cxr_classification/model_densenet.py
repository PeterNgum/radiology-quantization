# code/benchmarks/cxr_classification/model_densenet.py
"""Model definition (e.g., DenseNet) for CXR classification."""

import torchvision.models as models
import torch.nn as nn

def get_densenet_model(num_classes=14, pretrained=True, **kwargs):
    """Gets a pre-trained DenseNet-121 model adapted for multi-label classification."""
    # Allow passing quantization args like load_in_8bit through kwargs
    # This basic example doesn't use them directly but allows the calling code to pass them
    model = models.densenet121(pretrained=pretrained)
    num_ftrs = model.classifier.in_features
    model.classifier = nn.Linear(num_ftrs, num_classes)
    # Sigmoid needed for multi-label classification (applied outside model during eval usually)
    return model
