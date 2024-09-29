import csv
from dataclasses import dataclass


@dataclass
class Row:
    route: str
    date: str
    daytype: str
    rides: str


def read_rides_as_dict(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            records.append(Row(row[0], row[1], row[2], row[3]))
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_dict('Data/ctabus.csv')
    print('Memory Use - dataclass: Current %d, Peak %d' %
          tracemalloc.get_traced_memory())
