import os
import pandas as pd

class DataHandler:
    def __init__(self, folderpath):
        self.folderpath = folderpath
        self.datasets = {}

    def read_data(self):
        try:
            for filename in os.listdir(self.folderpath):
                if filename.endswith(".csv"):
                    filepath = os.path.join(self.folderpath, filename)
                    dataset_name = os.path.splitext(filename)[0]
                    self.datasets[dataset_name] = pd.read_csv(filepath)
                    null_values = self.check_null_values(dataset_name)
                    if null_values is not None:
                        print(f"Null values found in {dataset_name}:")
                        print(null_values)
            return self.datasets
        except FileNotFoundError:
            print("Folder not found.")
            return None

    def check_null_values(self, dataset_name):
        if dataset_name in self.datasets:
            return self.datasets[dataset_name].isnull().sum()
        else:
            return None

    
if __name__ == "__main__":
    data_handler = DataHandler("data")
    datasets = data_handler.read_data()
    for dataset_name, dataset in datasets.items():
        print(f"Dataset: {dataset_name}")
        print(dataset.head())
        print()
