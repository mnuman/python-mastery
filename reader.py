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


def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
