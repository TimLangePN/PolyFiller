# for match support you need 3.10 or higer, todo: add to requirements.txt
def resolve_tariff_range(style):
    if style == '#style1':
        return '1 - 1,99'
    elif style == '#style2':
        return '2 - 2,99'
    elif style == '#style3':
        return '3 - 3,99'
    elif style == '#style4':
        return '4 - 4,99'
    elif style == '#style5':
        return '5+'
    else:
        print('Style is not supported!')