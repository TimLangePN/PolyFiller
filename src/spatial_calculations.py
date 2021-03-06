from shapely.geometry import Point
import random

# Generates N random points inside a polygon
def generate_random_coordinates(number, polygon):
    coordinates = []
    minx, miny, maxx, maxy = polygon.bounds
    while len(coordinates) < number:
        point = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(point):
            coordinates.append(point)
    return coordinates

def get_total_points(number, features):
    for features in features:
        total_polygons = len(features._features)
    return total_polygons * number