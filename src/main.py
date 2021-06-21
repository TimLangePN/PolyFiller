from spatial_calculations import *
from csv_writer import *
from reverse_geocoder import *
from name_resolver import *
from kml_parser import *
from bootstrap import *
from csv_helpers import *

# init function
def init(amount_of_points, kml_path):

    # Init parse of the KML.
    features = parse_kml(kml_path)

    # Extract country_prefix (e.g. 'FR') and city_name (e.g. 'Toulouse') from KML root
    country_prefix, city_name = get_country_prefix_and_city_name(
        features[0].name)

    # Concatenate country_prefix and city_name to file_name
    file_name = f'data\\{country_prefix}_{city_name}.csv'

    # Writes the header of the CSV
    write_header(file_name)

    # Retrieve nested features and puts them in a list
    nested_features = list(features[0].features())

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
            sg.popup('Unable to parse polygons that are defined within the KML, please refer to: https://github.com/TimLangePN/PolyFiller/wiki')
            return
        # Compute N random computed coordinates within the bounds of a feature.geometry object
        random_coordinates_list = generate_random_coordinates(amount_of_points, feature_geometry_obj)

        # Retrieve the tariff_range (e.g. '1 - 1,99) from the styleUrl that's attached to a feature
        tariff_range = resolve_tariff_range(feature.styleUrl)

        # grab the zone_code from the attribute name
        zone_code = feature.name
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

            # Opens a another window with a progress bar that walks through the total calculated points
            # Returns a false value when cancelled/done
            progress_meter = sg.one_line_progress_meter(
                'Progress meter', counter, total_points, 'key', 'Writing to .csv', no_titlebar=True)
            if progress_meter == False and counter == total_points:
                sg.popup('.csv has been created')
                return
            elif progress_meter == False:
                return
            counter = write_rows(file_name, zone_code, coordinates, city_name, country_prefix, street_name, zone_description, tariff_range, counter)