import globals as G

from dataclasses import dataclass, field
from objects_base import Object

@dataclass
class Set( Object ):
    __value: set = field( default_factory=set )
    __type: str = ""

    def __init__ ( self, name: str = "", value: set = {}, type: str = "" ):
        super().__init__( name )
        self.__value = value
        self.__type = type

    @property
    def value( self ):
        return self.__value
    @value.setter
    def value( self, value: set ):
        self.__value = value

    def toString( self ):
        base_string = super().toString()
        return f"{base_string} " \
            f"value={self.__value} " \
            f"type={self.__type}"
    
@dataclass
class Multiset( Object ):
    __value: list = field( default_factory=list )
    __type: str = ""

    def __init__ ( self, name: str = "", value: list = [], type: str = "" ):
        super().__init__( name )
        self.__value = value
        self.__type = type

    @property
    def value( self ):
        return self.__value
    @value.setter
    def value( self, value: list ):
        self.__value = value

    def to_stringified_list( self ):
        return str( self.__value )

    def to_string( self ):
        base_string = super().toString()
        return f"{base_string} " \
            f"value={self.__value} " \
            f"type={self.__type}"