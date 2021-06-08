import geocoder


def resolve_street_name(y, x):
    location = geocoder.bing(
        [y, x], method='reverse', key='Ai7XinRoS3z2Nydo0_dtrqjNLlHhOozDWUAijI0BikpnI-vwCcWSxj7yyM48TG8k')
    street_name = location.current_result.road
    return street_name