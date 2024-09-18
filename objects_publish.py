import globals as G
from dataclasses import dataclass, field

from objects_base import Object

@dataclass
class Document:
    __contents: list = field( default_factory=list )
    __type: str = ""

    def __init__ ( self, name = "", contents: list = [], type: str = "" ):
        super().__init__( name )
        self.__contents = contents
        self.__type = type

    @property
    def contents( self ):
        return self.__contents
    @contents.setter
    def symb( self, contents: list ):
        self.__contents = contents

    @property
    def type( self ):
        return self.__type
    @type.setter
    def type( self, type: str ):
        self.__type = type

    def to_string( self ):
        base_string = super().to_string()
        return f"{base_string} " \
            f"symbol={self.__sym} " \
            f"val={self.__value}"
