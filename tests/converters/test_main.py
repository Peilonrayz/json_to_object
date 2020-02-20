from dataclasses import dataclass
from datetime import datetime
from converters import Converter, Converters

from dataclasses_json import dataclass_json


@dataclass
class Range:
    start: datetime
    end: datetime


@dataclass
class Base:
    date: datetime
    range: Range


@dataclass_json
@dataclass(init=False)
class International(Converter[Base]):
    date: str = Converters.date('date', '%d/%m/%y %H:%M')
    start: str = Converters.date('range.start', '%d/%m/%y %H:%M')
    end: str = Converters.date('range.end', '%d/%m/%y %H:%M')


class American(Converter[Base]):
    date: str = Converters.date('date', '%m/%d/%y %H:%M')
    start: str = Converters.date('range.start', '%m/%d/%y %H:%M')
    end: str = Converters.date('range.end', '%m/%d/%y %H:%M')


if __name__ == '__main__':
    i = International.from_json('''{
        "date": "14/02/19 12:00",
        "start": "14/02/19 12:00",
        "end": "14/02/19 12:00"
    }''')
    b = i.build()
    a = American.from_(b)

    FORMAT = '{1}:\n\tdate: {0.date}\n\tstart: {0.range.start}\n\tend: {0.range.end}'
    FORMAT_C = '{1}:\n\tdate: {0.date}\n\tstart: {0.start}\n\tend: {0.end}'
    print(FORMAT.format(b, 'b'))
    print(FORMAT_C.format(a, 'a'))
    print(FORMAT_C.format(i, 'i'))
    print('\nupdate b.date')
    b.date = datetime(2019, 2, 14, 12, 30)
    print(FORMAT.format(b, 'b'))
    print(FORMAT_C.format(a, 'a'))
    print(FORMAT_C.format(i, 'i'))
    print('\nupdate b.range.start')
    b.range.start = datetime(2019, 2, 14, 13, 00)
    print(FORMAT.format(b, 'b'))
    print(FORMAT_C.format(a, 'a'))
    print(FORMAT_C.format(i, 'i'))

    print('\njson dump')
    print(i.to_json())
