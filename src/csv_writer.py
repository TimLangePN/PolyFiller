import csv
import os

def write_csv(file_name, row_list):
    schema = ['ZONE_CODE', 'LAT', 'LON', 'CITY', 'DISPLAY_STREETNAME', 'GOOGLE_STREETNAME', 'ZONE_STREET', 'ZONE_DESCRIPTION', 'Tariff_range', 'Unieke ID']

    file_name = f"{file_name}.csv"
    
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'a', encoding='utf-8-sig', newline='') as file_name:
        writer = csv.writer(file_name, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow([header for header in schema])
        writer.writerows(row_list)