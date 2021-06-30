import pandas as pd

def write_xls(file_name):
    pd.read_csv(f"{file_name}.csv", delimiter=";", decimal=',', converters={'ZONE_CODE':int},).to_excel(f"{file_name}.xls", index=False)