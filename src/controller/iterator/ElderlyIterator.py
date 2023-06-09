from collections.abc import Iterator
from typing import Any

class ElderlyIterator(Iterator):
    
    _position: int = None

    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False) -> None:
        self.collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            value = self.collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value
    
    def __iter__(self) -> Iterator:
        return self