import csv
from typing import Callable, ClassVar, Dict, List, Optional, Sequence, Type


def csv_as_dicts(lines: Sequence, types: List[Callable], headers: Optional[List[str]] = None) -> Sequence[Dict]:
    '''
    Convert lines of CSV text into a list of dictionaries
    '''
    records = []
    rows = csv.reader(lines)
    # design challenge - headers may be present in the file
    # otherwise we will use the first row as headers
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {name: func(val)
                  for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances(lines: Sequence, cls: Type) -> Sequence[Type]:
    '''
    Convert lines of CSV text into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    _ = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


def read_csv_as_dicts(filename: str, types: List[Callable]) -> Sequence[Dict]:
    return csv_as_dicts(open(filename), types)  # type: ignore


def read_csv_as_instances(filename: str, cls: Type) -> Sequence[Type]:
    return csv_as_instances(open(filename), cls)    # type: ignore
