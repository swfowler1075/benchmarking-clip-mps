import sys
import time
import torch
from PIL import Image

from transformers import CLIPModel, CLIPProcessor

"""
DEV NOTES — cliploader.py
Role: Pretrained CLIP Inference Engine & Hardware Telemetry
---------------------------------------------------------------------------
- Wraps Hugging Face `CLIPModel` and `CLIPProcessor` (openai/clip-vit-base-patch32).
- Toggles execution between `cpu` (Float32) and Apple Silicon `mps` (Float16/Float32).
- Encodes unseen class text prompts (short labels vs. attribute-enriched descriptions)
  and L2-normalizes embeddings once per run.
- Encodes image batches and computes cosine similarity scaled by `logit_scale`.
- Calls `torch.mps.synchronize()` before/after timed blocks for accurate ms latency
  and reads `torch.mps.current_allocated_memory()` for GPU memory footprint.
- Next: Instantiate CLIPZeroShotRunner inside main.py for CPU vs. MPS trials.
"""


class CLIPZeroShotRunner:
    def __init__(self) :
        pass
