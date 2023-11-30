import os
import pandas as pd

def read_data(folderpath):
    datasets = {}
    try:
        for filename in os.listdir(folderpath):
            if filename.endswith(".csv"):
                filepath = os.path.join(folderpath, filename)
                dataset_name = os.path.splitext(filename)[0]
                datasets[dataset_name] = pd.read_csv(filepath)
                null_values = check_null_values(datasets[dataset_name])
                if null_values is not None:
                    print(f"Null values found in {dataset_name}:")
                    print(null_values)
        return datasets
    except FileNotFoundError:
        print("Folder not found.")
        return None

def check_null_values(dataset):
    return dataset.isnull().sum()

if __name__ == "__main__":
    datasets = read_data("data/full")
    for dataset_name, dataset in datasets.items():
        print(f"Dataset: {dataset_name}")
        print()
