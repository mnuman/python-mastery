import csv


def read_csv_as_dicts(filename, conversions):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        return [
            dict(zip(headers, [
                conversion(value) for conversion, value in zip(conversions, row)
            ])) for row in reader
        ]
