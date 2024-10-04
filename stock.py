import csv

headers = []


class Stock:
    _types = (str, int, float)
    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, nshares):
        self.shares -= nshares

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if isinstance(value, self._types[1]) and value >= 0:
            self._shares = value
        else:
            raise TypeError('Expected positive non-negative integer')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, self._types[2]) and value >= 0:
            self._price = value
        else:
            raise TypeError(
                f'Expected positive non-negative {self._types[2].__name__}')

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price


def read_portfolio(filename):
    global headers
    portfolio = None
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header row
        portfolio = [Stock.from_row(row) for row in rows]
    return portfolio



if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    print_portfolio(portfolio)
