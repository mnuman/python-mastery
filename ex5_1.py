import time
from typing import Optional, Tuple


def parse_line(line: str) -> Optional[Tuple[str, str]]:
    '''
    Parse a line of text into a name and value
    '''
    vals = line.split('=')
    if len(vals) == 2:
        return vals[0], vals[1]
    return None


def worker(x, y):
    print('About to work')
    time.sleep(20)
    print('Done')
    return x + y
