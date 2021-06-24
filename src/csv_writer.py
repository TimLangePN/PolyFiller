import csv
import os

def write_header(file_name):
    schema = ['ZONE_CODE', 'LAT', 'LON', 'CITY', 'DISPLAY_STREETNAME', 'GOOGLE_STREETNAME', 'ZONE_STREET', 'ZONE_DESCRIPTION', 'Tariff_range', 'Unieke ID']

    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'a', newline='') as file_name:
        writer = csv.writer(file_name, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow([header for header in schema])

def write_rows(file_name, row_list):
    import csv

    with open(file_name, 'a', encoding="utf-8", newline='') as file_name:
        writer = csv.writer(file_name, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerows(row_list)