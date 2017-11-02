from pprint import pprint
from datetime import datetime
import csv
import regex

def get_input(fname):

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
    return all_data

def write_output(data):

    order = ["Account Number","Read Date","Address","Zip Code", "Consumption"]

    with open('file.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, order)
        dict_writer.writeheader()
        dict_writer.writerows(data)


##### helpers #####

def get_address(text):
    reg = regex.compile(r'\b[0-9]{1,3}(?:\s\p{L}+)+')
    results = reg.search(text)

    if results:
        return results.group(0)
    else:
        return None

def get_date(text):
    reg = regex.compile(r'\w{3}[ ]\d{1,2}[ ]\d{4}')
    results = reg.search(text)

    if results:
        datetime_object = datetime.strptime(results.group(0), '%b %d %Y')
        return datetime.strftime(datetime_object, '%Y%m%d')
    else:
        return None

write_output(get_input('example_input.txt'))