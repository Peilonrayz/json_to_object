from pprint import pprint

from schema import build

base = {'type': 'T'}
array = {
    'type': 'array',
    'items': {
        'type': 'number'
    }
}
tuple_ = {
    'type': 'array',
    'items': [
        {'type': 'number'},
        {'type': 'string'}
    ]
}
mapping = {
    'type': 'object',
    'additionalProperties': {'type': 'string'}
}
object_ = {
    'type': 'object',
    'properties': {
        'a': {'type': 'number'},
        'b': {'type': 'string'}
    }
}


if __name__ == '__main__':
    pprint(build(base))
    pprint(build(array))
    pprint(build(tuple_))
