import csv

source_file = open('JC-202201-citibike-tripdata.csv')

citibike_reader = csv.DictReader(source_file)

print(citibike_reader.fieldnames)

