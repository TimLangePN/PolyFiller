from spatial_calculations import *
from csv_writer import *
from reverse_geocoder import *
from name_resolver import *
from kml_parser import *
from bootstrap import *
from csv_helpers import *

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
counter = 0

for feature in nested_features:

    # Compute N random computed coordinates within the bounds of a feature.geometry object
    random_coordinates_list = generate_random_coordinates(amount_of_random_generated_coordinates, feature.geometry)

    # Retrieve the tariff_range (e.g. '1 - 1,99) from the styleUrl that's attached to a feature 
    tariff_range = resolve_tariff_range(feature.styleUrl)

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
        write_rows(file_name, coordinates, city_name, country_prefix, street_name, tariff_range, unique_id)

        # Increment counter per iteration
        counter += 1