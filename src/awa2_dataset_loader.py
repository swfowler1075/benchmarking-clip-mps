import os
from pathlib import Path
import yaml


class AwA2DatasetLoader:
    def __init__(self,configfile):
        pass
        print("AwA2DatasetLoader")
        # Pass the config file contents to self.cfg
        self.cfg = configfile

        # Resolve base directory relative to the project root
        current_file = Path(__file__).resolve()
        project_root = current_file.parent.parent
        print("project_root", project_root)

        # Stripping leading dots if any from the YAML path strings
        #/data/Animals_with_Attributes2
        base_dir_str = self.cfg['paths']['base_metadata_dir'].lstrip("./")
        self.base_dir = project_root / base_dir_str
        print("self.base_dir", self.base_dir)

        # now extract the data from config file and concatenate the corrected
        # paths
        self.classes_file = self.base_dir / self.cfg['dataset']['classes_file']
        self.train_file = self.base_dir / self.cfg['dataset']['train_split_file']
        self.test_file = self.base_dir / self.cfg['dataset']['test_split_file']

        print("self.classes_file", self.classes_file)
        print("self.train_file", self.train_file)
        print("self.test_file", self.test_file)

    def load_attributes(self):
        pass
        # Loads the attribute matrix values and attribute(predicate) names
        matrix_path = self.base_dir / self.cfg['dataset']['matrix_file']
        predicates_path = self.base_dir / self.cfg['dataset']['predicates_file']

        # Load attribute string names (e.g., 'black', 'white','furry', 'stripes')
        with open(predicates_path, 'r') as f:
            attributes = [line.split()[-1] for line in f if line.strip()]

        # Load the 50x85 numerical matrix
        matrix = []
        with open(matrix_path, 'r') as f:
            for line in f:
                if line.strip():
                    row_values = [float(val) for val in line.split()]
                    matrix.append(row_values)

        print(f"Successfully loaded attribute matrix: {len(matrix)} animals x {len(attributes)} attributes.")
        return attributes, matrix

    def load_splits(self):
        pass

        """Parses the total classes and segments them into seen (train) and unseen (test) sets."""
        # 1. Load all 50 classes into a clean Python list
        all_classes = []
        with open(self.classes_file, 'r') as f:
            for line in f:
                if line.strip():
                    # Splits "1\tantelope" or "1  antelope" and takes the name portion
                    class_name = line.split()[-1]
                    all_classes.append(class_name)

        # 2. Read the seen (train) animal names
        with open(self.train_file, 'r') as f:
            seen_classes = [line.strip() for line in f if line.strip()]

        # 3. Read the unseen (test) animal names
        with open(self.test_file, 'r') as f:
            unseen_classes = [line.strip() for line in f if line.strip()]

        print(f"Loaded {len(all_classes)} total classes.")
        print(f"-> Seen (Train) classes: {len(seen_classes)}")
        print(f"-> Unseen (Test) classes: {len(unseen_classes)}")

        return all_classes, seen_classes, unseen_classes

    def get_image_paths(self, target_classes):

        # AwA2 contains images inside a directory named 'JPEGImages'
        images_root = self.base_dir / "JPEGImages"
        image_paths = []

        # Loop through only the classes requested (e.g., seen or unseen)
        for class_name in target_classes:
            class_folder = images_root / class_name

            if class_folder.exists():
                # Glob all files ending in .jpg or .jpeg inside that folder
                class_images = list(class_folder.glob("*.jpg")) + list(class_folder.glob("*.jpeg"))
                image_paths.extend(class_images)
            else:
                print(f"Warning: Folder not found for class: {class_name}")

        print(f"Indexed {len(image_paths)} total images across {len(target_classes)} classes.")
        return image_paths