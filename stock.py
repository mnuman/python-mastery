import csv

headers = []


class Stock:
    types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)


def read_portfolio(filename):
    global headers
    portfolio = None
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header row
        portfolio = [Stock.from_row(row) for row in rows]
    return portfolio


def print_portfolio(portfolio):
    # print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s}")
    # print(('-'*10 + ' ')*3)
    for s in portfolio:
        print(f"{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}")


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    print_portfolio(portfolio)
