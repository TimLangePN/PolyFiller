import csv

schema = ['ZONE_CODE','LAT','LON','CITY','DISPLAY_STREETNAME','GOOGLE_STREETNAME','ZONE_STREET','ZONE_DESCRIPTION','Tariff_range','Unieke ID']

def write_header(city_name):
    file_name = f'data\\DE_{city_name}.csv'

    with open(file_name, 'a', newline='') as file_name:
        writer = csv.writer(file_name)
        writer.writerow([header for header in schema])
        
def write_rows(coordinate, city_name, street_name):
    file_name = f'data\\DE_{city_name}.csv'

    display_streetname = street_name
    google_streetname = display_streetname
    zone_street = google_streetname

    with open(file_name, 'a', newline='') as file_name:
        writer = csv.writer(file_name)
        writer.writerow([coordinate.y, coordinate.x, city_name, display_streetname, google_streetname, zone_street])