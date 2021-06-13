from spatial_calculations import *
from csv_writer import *
from reverse_geocoder import *
from name_resolver import *
from kml_parser import *
from bootstrap import *
from csv_helpers import *
import sys

# Retrieve KML file from relative path
kml_file = retrieve_kml()

# Init parse of the KML.
features = parse_kml(kml_file)

# Extract country_prefix (e.g. 'FR') and city_name (e.g. 'Toulouse') from KML root
country_prefix, city_name = get_country_prefix_and_city_name(features[0].name)

# Concatenate country_prefix and city_name to file_name
file_name = f'data\\{country_prefix}_{city_name}.csv'

# Writes the header of the CSV
write_header(file_name)

# Retrieve
nested_features = list(features[0].features())

# To be made dynamically so the client delegates the amount of random generated coordinates within a feature
amount_of_random_generated_coordinates = 5

# Initiliaze a counter that we increase per iteration, this is passed to the 'unique_id' variable
counter = 1
increment_const = 1

for feature in nested_features:

    try:
        if hasattr(feature, 'geometry'):
            feature_geometry_obj =  feature.geometry
        elif hasattr(feature._features[0]._geometry, 'geometry'):
            feature_geometry_obj =  feature._features[0]._geometry.geometry
    except:                                                                                     # Need to replace link with proper wiki ref
            sys.exit("Unable to parse polygons that are defined within the KML, please refer to: https://github.com/TimLangePN/PolyFiller/wiki")

    # Compute N random computed coordinates within the bounds of a feature.geometry object
    random_coordinates_list = generate_random_coordinates(amount_of_random_generated_coordinates, feature_geometry_obj)

    # Retrieve the tariff_range (e.g. '1 - 1,99) from the styleUrl that's attached to a feature
    tariff_range = resolve_tariff_range(feature.styleUrl)

    #grab the zone_code from the attribute name
    zone_code = feature.name
    zone_description = f'{city_name} - Zone {zone_code}'

    # Initialize a list that is used for storing N random generated points per feature
    coordinates_list = []

    # For every y and x in the list of randomly computed coordinates append it to the list of all coordinates 
    for coordinates in random_coordinates_list:
        coordinates_list.append(coordinates)

    # For every y and x in the list of coordinates loop through this to persist records to the .csv
    for coordinates in coordinates_list:

        # Retrieve the street name for a computed random generated coordinate 
        street_name = resolve_street_name(str(coordinates.y), str(coordinates.x))

        # Calculate and construct the 'unique_id'
        unique_id = f'{country_prefix}{city_name[0:3].upper()}{counter}'

        # Persist row as record to file
        write_rows(file_name,zone_code, coordinates, city_name, country_prefix, street_name, tariff_range, zone_description, unique_id)

        # Increment counter per iteration
        counter += increment_const