import sys
full_list = []

def resolve_tariff_range(style):
    if style == '#style1':
        return '0 - 0,99'
    elif style == '#style2':
        return '1 - 1,99'
    elif style == '#style3':
        return '2 - 2,99'
    elif style == '#style4':
        return '3 - 3,99'
    elif style == '#style5':
        return '4 - 4,99'
    elif style == '#style6':
        return '5 +'
    else:
        sys.exit('Style not found')

def get_total_items(zone_code, lat, lon, country_prefix, city_name, street_name, zone_description, tariff_range, counter):
        counter = counter + 1
        display_streetname = street_name
        google_streetname = display_streetname
        zone_street = google_streetname

        lat = str(lat).replace('.', ',')
        lon = str(lon).replace('.', ',')

        unique_id = f'{country_prefix}{city_name[0:3].upper()}{counter}'

        all_parameters = zone_code, lat, lon, city_name, display_streetname, google_streetname, zone_street, zone_description, tariff_range, unique_id
        full_list.append(all_parameters)
        return full_list, counter 