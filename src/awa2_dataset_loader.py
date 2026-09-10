import os
from pathlib import Path
import yaml


class AwA2DatasetLoader:
    def __init__(self,configfile):
        pass
        print("AwA2DatasetLoader")
        # Pass the relative path from the project root
        self.cfg = configfile
        # Resolve base directory relative to the project root
        current_file = Path(__file__).resolve()
        project_root = current_file.parent.parent
        print("project_root", project_root)

    def test(self):
        print("Test")

    def load(self):
        pass
        print("Load")