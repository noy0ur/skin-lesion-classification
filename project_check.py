
# project_check.py
# Skin Lesion Classification Project
# Step 4: Project setup verification

from pathlib import Path
import platform
import sys

PROJECT_NAME = "Skin Lesion Classification"
DATASET_NAME = "HAM10000"

CLASS_NAMES = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc",
]

print("=" * 45)
print(PROJECT_NAME)
print("=" * 45)

print("Python version:", sys.version.split()[0])
print("Platform:", platform.system())
print("Dataset planned:", DATASET_NAME)

print("\nClassification categories:")
for index, class_name in enumerate(CLASS_NAMES, start=1):
    print(f"{index}. {class_name}")

print("\nProject setup check completed!")
print("This file does not train a model yet.")
