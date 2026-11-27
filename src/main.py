import os
from pathlib import Path
import yaml
from awa2_dataset_loader import AwA2DatasetLoader

"""
DEV NOTES — main.py
Role: Benchmark Orchestrator & MLflow Experiment Logger
---------------------------------------------------------------------------
- Reads hyperparameters, device targets, and prompt templates from config/config.yaml.
- Pulls unseen class splits and image paths via AwA2DatasetLoader.
- Executes 1 warm-up pass on MPS (excluded from metrics), then runs 10 timed trials
  comparing CPU (Float32) vs. MPS (Float16/Float32).
- Captures and logs to local MLflow (`mlruns/`):
    1. Average batch latency (ms) across 10 trials
    2. Throughput (images/sec)
    3. Peak MPS memory allocation (MB)
    4. Top-1 zero-shot classification accuracy parity between CPU and MPS
- Next: Add the 10-trial benchmark loop, MLflow logging, and CSV/figure export for the report.
"""

def load_config(configfile):

    # 1. Get the path of this exact script (e.g., ../src/main.py)
    current_file = Path(__file__).resolve()

    # 2. Go up to the parent of 'src', which is your true project root directory
    project_root = current_file.parent.parent

    # 3. Create an absolute path straight to the config file
    config_file = project_root / configfile

    with open(config_file, "r") as file:
        return yaml.safe_load(file)

def main():
    print("Main")
    config_file_path = "config/config.yaml"
    configfile = load_config(config_file_path)
    loader = AwA2DatasetLoader(configfile)
    ll_cls, seen_cls, unseen_cls = loader.load_splits()
    attrs, mat = loader.load_attributes()

    # Test indexing images for the training (seen) set
    print("\nIndexing testing dataset images...")
    seen_images = loader.get_image_paths(unseen_cls)



if __name__ == "__main__":
    main()