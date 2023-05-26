from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Reply(_message.Message):
    __slots__ = ["jsonData"]
    JSONDATA_FIELD_NUMBER: _ClassVar[int]
    jsonData: str
    def __init__(self, jsonData: _Optional[str] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["Url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    Url: str
    def __init__(self, Url: _Optional[str] = ...) -> None: ...

class TextRequest(_message.Message):
    __slots__ = ["Content"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    Content: str
    def __init__(self, Content: _Optional[str] = ...) -> None: ...
