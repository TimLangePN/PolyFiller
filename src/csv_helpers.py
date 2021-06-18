import sys

# for match support you need 3.10 or higer, todo: add to requirements.txt
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
        return ''

def validate_city_name(city_name):
    if not city_name:
        sys.exit('City name not found')
    else:
        return city_name