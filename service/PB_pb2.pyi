from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

COMEDY: Genre
DESCRIPTOR: _descriptor.FileDescriptor
HORROR: Genre
ROMANCE: Genre

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "title", "year"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    isbn: str
    title: str
    year: int
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., year: _Optional[int] = ..., genre: _Optional[_Union[Genre, str]] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "number"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.Status
    BOOK_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.Status
    book: Book
    number: str
    def __init__(self, number: _Optional[str] = ..., book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
