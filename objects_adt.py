from dataclasses import dataclass, field
from objects_base import Object

@dataclass
class Set( Object ):
    __value : set = field( default_factory=set )
    __type : str = ""

    def __init__ ( self, name = "", value = {}, type = "" ):
        super().__init__( name )
        if not value == {}:
            self.__value = value
        if not type == "":
            self.__type = type

    @property
    def value( self ):
        return self.__value
    @value.setter
    def value( self, value ):
        self.__value = value

    def toString( self ):
        base_string = super().toString()
        return f"{base_string} " \
            f"value={self.__value} " \
            f"type={self.__type}"