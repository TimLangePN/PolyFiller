all_rows = []
tariff_list = ['0 - 0,99', '1 - 1,99', '2 - 2,99', '3 - 3,99', '4 - 4,99', '5 +']

def resolve_tariff_range(feature):
    try:
        if feature.styleUrl is not None:
            style = feature.styleUrl
        elif hasattr(feature._features[0], 'styleUrl'):
            style = feature._features[0].styleUrl
    except:
        return False
    if style == '#style1' or style == '#Style1':
        return '0 - 0,99'
    elif style == '#style2' or style == '#Style2':
        return '1 - 1,99'
    elif style == '#style3' or style == '#Style3':
        return '2 - 2,99'
    elif style == '#style4' or style == '#Style4':
        return '3 - 3,99'
    elif style == '#style5' or style == '#Style5':
        return '4 - 4,99'
    elif style == '#style6' or style == '#Style6':
        return '5 +'
    else:
        return False

def get_all_rows(zone_code, lat, lon, country_prefix, city_name, street_name, zone_description, tariff_range, counter):
        counter = counter + 1

        display_streetname = street_name
        google_streetname = display_streetname
        zone_street = google_streetname

        lat = str(lat).replace('.', ',')
        lon = str(lon).replace('.', ',')

        unique_id = f'{country_prefix}{city_name[0:3].upper()}{counter}'

        row_attributes = zone_code, lat, lon, city_name, display_streetname, google_streetname, zone_street, zone_description, tariff_range, unique_id
        all_rows.append(row_attributes)
        return all_rows, counter 

def get_tariff_and_id(feature):
    try:
        if any(tariffs in feature.description for tariffs in tariff_list):
            splitted_features = feature.description.split("\n<br/>", 2,)
            tariff_range = splitted_features[0].split(': ')[1]
            zone_code = splitted_features[1].split(': ')[1].split('</p>')[0]
            return tariff_range, zone_code
        else:
            return resolve_tariff_range(feature), feature.name
    except:
            return resolve_tariff_range(feature), feature.name