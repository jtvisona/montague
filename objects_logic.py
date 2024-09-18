from dataclasses import dataclass, field
from objects_base import Object

@dataclass
class Variable:
    __symb: str = ""
    __type: str = ""
    __value: object = field( default_factory=object )

    def __init__ ( self, name = "", symb: str = "", type: str = "" ): # Create Type
        super().__init__( name )
        self.__symb = symb
        self.__type = type

    @property
    def symb( self ):
        return self.__symb
    @symb.setter
    def symb( self, symb: str ): # tighten up by adding Symbol type
        self.__symb = symb

    @property
    def value( self ):
        return self.__value
    @value.setter
    def value( self, value: str ):
        self.__value = value

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
