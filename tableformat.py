from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        ...

    @abstractmethod
    def row(self, rowdata):
        ...


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(h for h in headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', ''.join(
            f"<th>{h}</th>" for h in headers), '</tr>', sep='')

    def row(self, rowdata):
        print('<tr>', ''.join(
            f"<td>{str(d)}</td>" for d in rowdata), '</tr>', sep='')


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'csv':
        formatter_class = CSVTableFormatter
    elif name == 'html':
        formatter_class = HTMLTableFormatter
    elif name == 'text':
        formatter_class = TextTableFormatter
    else:
        raise RuntimeError(f'Unknown format {format}')
    if column_formats:
        class formatter_class(ColumnFormatMixin, formatter_class):  # type: ignore
            formats = column_formats

    if upper_headers:
        class formatter_class(UpperHeadersMixin, formatter_class):  # type: ignore
            pass

    return formatter_class()


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)     # type: ignore


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
