from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple, Optional, Union


@dataclass
class Type:
    type: Tuple[str]
    properties: dict


@dataclass
class SequenceType:
    positional: Tuple[Type, ...]
    repeat: Tuple[Type, ...]
    properties: dict
    length: Optional[int] = None

    def indexed(self, key: int) -> Type:
        if self.length is not None and key >= self.length:
            raise KeyError('key exceeds length of SequenceType')
        if key < len(self.positional):
            return self.positional[key]
        return self.repeat[(key - len(self.positional)) % len(self.repeat)]


def _nullable_less_than(a: Union[int, float, None], b: Union[int, float]):
    if a is None:
        return False
    return a < b


@dataclass
class MappingType:
    keys: SequenceType
    values: SequenceType
    properties: dict

    def indexed(self, key: int, *, longest: bool=False) -> Tuple[Type, Type]:
        if not longest:
            return self.keys.indexed(key), self.values.indexed(key)

        key_ = _nullable_less_than(self.keys.length, key)
        value_ = _nullable_less_than(self.values.length, key)
        if key_ and value_:
            raise KeyError('key exceeds length of MappingType')
        return (
            self.keys.indexed(key) if key_ else None,
            self.values.indexed(key) if value_ else None
        )


@dataclass
class Collection:
    values: MappingType
    properties: dict
    args: Optional[MappingType] = None
