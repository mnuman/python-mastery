import csv


class Validator:
    @classmethod
    def check(cls, value):
        return value


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


class NonEmptyString(String, NonEmpty):
    pass


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
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.shares!r}, {self.price!r})'

    def __eq__(self, other):
        return isinstance(other, Stock) and (
            (self.name, self.shares, self.price) ==
            (other.name, other.shares, other.price))


def read_portfolio(filename):
    global headers
    portfolio = None
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header row
        portfolio = [Stock.from_row(row) for row in rows]
    return portfolio
