import csv


def read_rides_as_dict(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': row[3],
            }
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_dict('Data/ctabus.csv')
    print('Memory Use - dict: Current %d, Peak %d' %
          tracemalloc.get_traced_memory())
