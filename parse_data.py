from pprint import pprint
from datetime import datetime
import regex
import csv

def parse_and_write_csv(fname):
    """Reads in text file, parses data, and writes to file"""

    with open(fname) as f:
        data = f.readlines()

    all_data = []

    for line in data:
        address = get_address(line)
        date = get_date(line)

        row = line.split()
        all_data.append({'Address': address,
                         'Account Number': regex.sub('[^0-9]','', row[0]).zfill(6),
                         'Consumption': regex.sub('[^0-9]','', row[-1]),
                         'Read Date': date,
                         'Zip Code': regex.sub('[^0-9]','', row[-2])})

    order = ["Account Number","Read Date","Address","Zip Code", "Consumption"]

    write_output(all_data, order)

##### helpers #####

def write_output(data, order):
    """Takes in a list of dictionaries, an order based on keys, and writes to a csv."""

    with open('file.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, order)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def get_address(text):
    """Uses regex to get street address."""

    reg = regex.compile(r'\b[0-9]{1,3}(?:\s\p{L}+)+')
    results = reg.search(text)

    if results:
        return results.group(0)
    else:
        return None

def get_date(text):
    """Uses regex to get date in format like 'Mar 2 2017' and reformats to
       YYYYMMDD.

    """

    reg = regex.compile(r'\w{3}[ ]\d{1,2}[ ]\d{4}')
    results = reg.search(text)

    if results:
        datetime_object = datetime.strptime(results.group(0), '%b %d %Y')
        return datetime.strftime(datetime_object, '%Y%m%d')
    else:
        return None

parse_and_write_csv('example_input.txt')