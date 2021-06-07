import csv

# Should make this function responsible for writing 
# the data from a strongly typed object to a .csv
# currently only writes points to the .csv as sample
def write_data_to_csv(file, points, address):
    with open(file, 'a', newline='') as file:
        writer = csv.writer(file)
        for point in points:
            writer.writerow([point.y, point.x, address])
