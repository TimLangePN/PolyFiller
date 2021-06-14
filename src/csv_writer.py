import csv
import os

schema = ['ZONE_CODE', 'LAT', 'LON', 'CITY', 'DISPLAY_STREETNAME', 'GOOGLE_STREETNAME', 'ZONE_STREET', 'ZONE_DESCRIPTION', 'Tariff_range', 'Unieke ID']

def write_header(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'a', newline='') as file_name:
        writer = csv.writer(file_name, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow([header for header in schema])

def write_rows(file_name, zone_code, coordinate, city_name, country_prefix, street_name, tariff_range, zone_description, counter):
    file_name = f'data\\{country_prefix}_{city_name}.csv'

    if file_name is None:
        return counter
    elif zone_code is None:
        return counter
    elif coordinate is None:
        return counter
    elif city_name is None:
        return counter
    elif country_prefix is None:
        return counter
    elif street_name is None:
        return counter
    elif tariff_range is None:
        return counter
    elif zone_description is None:
        return counter

    display_streetname = street_name
    google_streetname = display_streetname
    zone_street = google_streetname

     # Calculate and construct the 'unique_id'
    unique_id = f'{country_prefix}{city_name[0:3].upper()}{counter}'

    with open(file_name, 'a', encoding="utf-8", newline='') as file_name:
        writer = csv.writer(file_name, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow([zone_code, coordinate.y, coordinate.x, city_name, display_streetname, google_streetname, zone_street, tariff_range, zone_description, unique_id])

    return counter + 1