import pandas as pd

class CsvReader:
    def read_csv(self, csvfile):
        df = pd.read_csv(csvfile)
        return df
