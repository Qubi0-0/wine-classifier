import pandas as pd

class DataHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
    
    def read_data(self):
        try:
            self.data = pd.read_csv(self.filepath)
            null_values = self.check_null_values()
            if null_values is not None:
                print("Null values found in the data:")
                print(null_values)
            return self.data
        except FileNotFoundError:
            print("File not found.")
            return None

    def check_null_values(self):
        if self.data is not None:
            return self.data.isnull().sum()
        else:
            return None

    
if __name__ == "__main__":
    data_handler = DataHandler("data/winequality-red.csv")
    data = data_handler.read_data()
    print(data.head())