from __future__ import annotations
from typing import Union

from .base import Collection, Type, SequenceType, MappingType

AllType: Union[Collection, Type]


class JS7Type:
    @classmethod
    def build(cls, schema: Union[str, dict]):
        if isinstance(schema, str):
            schema = {'type': schema}
        if not isinstance(schema, dict):
            raise TypeError('Type should be passed a dict')
        if not isinstance(schema['type'], list):
            schema['type'] = [schema['type']]
        return Type(type=schema.pop('type'), properties=schema)


def _handle_type(value):
    if isinstance(value, dict):
        return True, (JS7Type.build(value),)
    elif isinstance(value, list):
        return False, tuple(JS7Type.build(i) for i in value)
    raise TypeError(f'value was neither a dict nor list: {value}')


class JS7Array:
    @classmethod
    def build(cls, schema):
        positional = ()
        repeating = (JS7Type.build('any'))
        if 'additionalItems' in schema:
            additional_items = schema.pop('additionalItems')
            if additional_items is False:
                repeating = ()
            else:
                single, repeating = _handle_type(additional_items)
                if not single:
                    raise ValueError("Additional Items can't be a list")
        if 'items' in schema:
            single, value = _handle_type(schema.pop('items'))
            if single:
                repeating = value
            else:
                positional = value
        elif 'contains' in schema:
            raise NotImplementedError('contains has not been implemented yet.')
        return Collection(
            MappingType(
                SequenceType((), (JS7Type.build('int'),), {}),
                SequenceType(positional, repeating, schema),
                {}
            ),
            {}
        )


def build(schema):
    if not isinstance(schema, dict):
        raise TypeError('type_ is not of type dict.')

    type_ = schema.pop('type', 'any')
    if type_ == 'object':
        raise NotImplementedError()
    elif type_ == 'array':
        return JS7Array.build(schema)
    else:
        schema['type'] = type_
        return JS7Type.build(schema)
