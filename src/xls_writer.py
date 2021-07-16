import pandas as pd
import os

def write_xls(file_name):

    if os.path.exists(file_name):
        os.remove(file_name)

    pd.read_csv(f"{file_name}.csv", delimiter=";", decimal=',').to_excel(f"{file_name}.xls", index=False)