from spatial_calculations import *
from csv_writer import *
from reverse_geocoder import *
from name_resolver import *
from kml_parser import *
from bootstrap import *
from csv_helpers import *
import PySimpleGUI as sg

def init(amount_of_points, counter,  kml_path):

    # Init parse of the KML. 
    features = parse_kml(kml_path)

    # Extract country_prefix (e.g. 'FR') and city_name (e.g. 'Toulouse') from KML root
    country_prefix, city_name = get_country_prefix_and_city_name(
        features[0].name)

    # Concatenate country_prefix and city_name to file_name
    file_name = f'data\\{country_prefix}_{city_name}.csv'

    # Retrieve nested features and puts them in a list
    nested_features = list(features[0].features())

    for feature in nested_features:
        try:
            if hasattr(feature, 'geometry'):
                feature_geometry_obj = feature.geometry
            elif hasattr(feature._features[0]._geometry, 'geometry'):
                feature_geometry_obj = feature._features[0]._geometry.geometry
        # Need to replace link with proper wiki ref
        except:
            return 'Unable to parse polygons that are defined within the KML, please refer to: https://github.com/TimLangePN/PolyFiller#readme'
        # Compute N random computed coordinates within the bounds of a feature.geometry object
        random_coordinates_list = generate_random_coordinates(amount_of_points, feature_geometry_obj)

        # Retrieve the tariff_range (e.g. '1 - 1,99) from the styleUrl that's attached to a feature
        tariff_range = resolve_tariff_range(feature.styleUrl)
        if tariff_range == False:
            return 'missing tariff feature within kml file'
        try:
            # grab the zone_code from the attribute name
            zone_code = feature.name # TODO: What if feature name is empty or forgotten, this would mean your entire generated CSV is considered `bad`, whilst you're still returning a `success` to the client.
        except:
            return 'missing name feature within kml file'
        zone_description = f'{city_name} - Zone {zone_code}'

        # Initialize a list that is used for storing N random generated points per feature
        coordinates_list = []
        total_points = get_total_points(amount_of_points, features)
        # For every y and x in the list of randomly computed coordinates append it to the list of all coordinates
        for coordinates in random_coordinates_list:
            coordinates_list.append(coordinates)
        # For every y and x in the list of coordinates loop through this to persist records to the .csv
        for coordinates in coordinates_list:
            # Retrieve the street name for a computed random generated coordinate
            street_name = resolve_street_name(str(coordinates.y), str(coordinates.x))

            # Appends all values to a list to make it writeable for write_csv
            rows_and_counter = get_all_rows(zone_code, str(coordinates.y), str(coordinates.x), country_prefix, city_name, street_name, zone_description, tariff_range, counter)
            all_rows = rows_and_counter[0]
            counter = rows_and_counter[1]

            # Opens a another window with a progress bar that walks through the total calculated points
            # Returns a false value when cancelled/done
            progess_bar = sg.one_line_progress_meter('Progress meter', counter, total_points, 'key', 'Writing to .csv', no_titlebar=True)
            if progess_bar == False and counter == total_points:
                write_csv(file_name, all_rows)
                return 'csv has been created'
            elif progess_bar == False and counter != total_points :
                return 'cancelled by user'