from pyexcel.cookbook import merge_all_to_a_book
import glob

def write_xls(file_name):
    merge_all_to_a_book(glob.glob(f"{file_name}.csv"), f"{file_name}.xlsx")