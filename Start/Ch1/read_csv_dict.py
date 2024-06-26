# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini
# Reading CSV file into an dictionary

import csv
import pprint

def read_csv_to_dict(filename):
  data = {}
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)    
    #row = next(reader) # read and skip header
    key = 0
    for row in reader:
      data[key] = row
      key += 1
  return data

# Example usage
inventory_data = read_csv_to_dict("Inventory.csv")

# Accessing data
pprint.pprint(inventory_data)
pprint.pprint(inventory_data[0])
pprint.pprint(inventory_data[0]["Consumer Price"])