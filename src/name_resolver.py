import sys

def get_country_prefix_and_city_name(kml_name_obj):  
    split_result = kml_name_obj.partition('_')
    country_prefix = split_result[0]
    city_name = split_result[2]
    if not city_name: 
        sys.exit('City name cannot be empty')
    elif not country_prefix: 
        sys.exit('Country prefix cannot be empty')
    return country_prefix, city_name