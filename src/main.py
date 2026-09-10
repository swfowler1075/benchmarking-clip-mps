import os
from pathlib import Path
import yaml
from awa2_dataset_loader import AwA2DatasetLoader

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
    loader.test()
    loader.load()


if __name__ == "__main__":
    main()