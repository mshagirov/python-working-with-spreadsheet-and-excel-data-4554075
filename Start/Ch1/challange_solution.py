# Solution to Challange 1
#
# 1. Read "Inventory.csv" (CSV file)
# 2. Add a new column "Margin"="Consumer Price" - "Wholesale Price"
# 3. Save the new CSV, e.g. "Output.csv"

import csv
import pprint
# better to use decimal.Decimal for currency and for working with decimal numbers

def read_csv_to_dict(filename):
  data = []
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      data.append(row)
  return data

def compute_margin_for_dictarray(data):
  for row in data:
    row['Margin']= "{:.2f}".format(float(row['Consumer Price']) - float(row['Wholesale Price']))


def write_dictarray_to_csv(data, filename):
  fieldnames = ['Item Name','Category','Quantity','Wholesale Price','Consumer Price', 'Margin']
  with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

data = read_csv_to_dict("Inventory.csv")
compute_margin_for_dictarray(data)
write_dictarray_to_csv(data, "output_ch1.csv")