from spatial_calculations import *
from csv_writer import *
from reverse_geocoder import *
from name_resolver import *
from kml_parser import *
from bootstrap import *
from csv_helpers import *
import sys
import PySimpleGUI as sg

total_points = '10'

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Add a KML:')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Text('Amount of Points per Polygon'), sg.Input(size=(2, None))],
          [sg.OK('Start'), sg.Cancel('Cancel')]]


window = sg.Window('PolyFiller', layout, icon='favicon.ico')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        window.close()
        break
    elif event == 'Start' and values[0] == '':
        sg.popup('KML can not be empty')
    elif event == 'Start' and values[1] == '':
        sg.popup('Amount of Points can not be empty')
    else:
        kml_path = values[0]
        # Init parse of the KML.
        features = parse_kml(kml_path)
        # Extract country_prefix (e.g. 'FR') and city_name (e.g. 'Toulouse') from KML root
        country_prefix, city_name = get_country_prefix_and_city_name(
            features[0].name)

        # Concatenate country_prefix and city_name to file_name
        file_name = f'data\\{country_prefix}_{city_name}.csv'

        # Writes the header of the CSV
        write_header(file_name)

        # Retrieve
        nested_features = list(features[0].features())

        # To be made dynamically so the client delegates the amount of random generated coordinates within a feature
        amount_of_random_generated_coordinates = int(values[1])
        total_points = get_total_points(
            amount_of_random_generated_coordinates, features)
        # Initiliaze a counter that we increase per iteration, this is passed to the 'unique_id' variable
        counter = 1

        for feature in nested_features:

            try:
                if hasattr(feature, 'geometry'):
                    feature_geometry_obj = feature.geometry
                elif hasattr(feature._features[0]._geometry, 'geometry'):
                    feature_geometry_obj = feature._features[0]._geometry.geometry
            # Need to replace link with proper wiki ref
            except:
                sys.exit(
                    "Unable to parse polygons that are defined within the KML, please refer to: https://github.com/TimLangePN/PolyFiller/wiki")

            # Compute N random computed coordinates within the bounds of a feature.geometry object
            random_coordinates_list = generate_random_coordinates(
                amount_of_random_generated_coordinates, feature_geometry_obj)

            # Retrieve the tariff_range (e.g. '1 - 1,99) from the styleUrl that's attached to a feature
            tariff_range = resolve_tariff_range(feature.styleUrl)

            # grab the zone_code from the attribute name
            zone_code = feature.name
            zone_description = f'{city_name} - Zone {zone_code}'

            # Initialize a list that is used for storing N random generated points per feature
            coordinates_list = []

            # For every y and x in the list of randomly computed coordinates append it to the list of all coordinates
            for coordinates in random_coordinates_list:
                coordinates_list.append(coordinates)

            # For every y and x in the list of coordinates loop through this to persist records to the .csv
            for coordinates in coordinates_list:
                progress_meter = sg.one_line_progress_meter(
                    'Progress meter', counter, total_points, 'key', 'Writing to .csv', no_titlebar=True)
                if progress_meter == False:
                    sg.Popup('Done!')
                    window.close()
                    sys.exit()
                # Retrieve the street name for a computed random generated coordinate
                street_name = resolve_street_name(
                    str(coordinates.y), str(coordinates.x))

                # Persist row as record to file and increment the counter
                counter = write_rows(file_name, zone_code, coordinates, city_name,
                                     country_prefix, street_name, tariff_range, zone_description, counter)
