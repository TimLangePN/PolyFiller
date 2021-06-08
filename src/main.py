from spatial_calculations import *
from csv_writer import *
from reverse_geocoder import *
from name_resolver import *
from kml_parser import *
from bootstrap import *

# Retrieve KML file from relative path
kml_file = retrieve_kml()

# Initialize a list that is used for storing N random generated points per feature
coordinates_list = []

# Init parse of the KML.
features = parse_kml(kml_file)

# Retrieve
nested_features = list(features[0].features())

# Get polygon and calculate random points inside polygon
for feature in nested_features:
    random_coordinates_list = generate_random_coordinates(5, feature.geometry)
    for coordinates in random_coordinates_list:
        coordinates_list.append(coordinates)

# grabs the prefix from the reverse_geocoder and replaces countryname with a prefix
country_prefix, city_name = get_country_prefix_and_city_name(features[0].name)

file_name = f'data\\{country_prefix}_{city_name}.csv'

# Writes the header of the CSV
write_header(file_name)

for coordinates in coordinates_list:
    street_name = resolve_street_name(str(coordinates.y), str(coordinates.x))
    write_rows(file_name, coordinates, city_name, country_prefix, street_name)