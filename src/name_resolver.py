import geocoder


def get_city_name(features):
    if '_' in features[0].name:
        city_name_full = str(features[0].name)
        city_prefix_split = city_name_full.split('_')[0]
        city_prefix_full = f'{city_prefix_split}_'
        city_name = city_name_full.partition(city_prefix_full)
        return city_name[2]
    else:
        return str(features[0].name)


def get_country_prefix(y, x):
    location = geocoder.bing(
        [y, x], method='reverse', key='Ai7XinRoS3z2Nydo0_dtrqjNLlHhOozDWUAijI0BikpnI-vwCcWSxj7yyM48TG8k')
    country_name = str(location.current_result.country)
    country_prefix = replace_country_name_to_prefix(country_name)
    return country_prefix


def replace_country_name_to_prefix(country_name):
    country_name = country_name.replace('France', 'FR_')
    country_name = country_name.replace('Germany', 'DE_')
    country_name = country_name.replace('Switzerland', 'CH_')
    country_name = country_name.replace('Austria', 'AU_')
    country_name = country_name.replace('Netherlands', 'NL_')
    country_name = country_name.replace('Belgium', 'BE_')
    return country_name