def get_country_prefix_and_city_name(kml_name_obj):
    split_result = kml_name_obj.partition('_')
    country_prefix = split_result[0]
    city_name = split_result[2]
    return country_prefix, city_name