from dataclasses import dataclass, field
from objects_base import Object

@dataclass
class Variable:
    __symb: str = ""
    __type: str = ""
    __value: object = field( default_factory=object )

    def __init__ ( self, name = "", symb: str = "", type: str = "" ): # Create Type
        super().__init__( name )
        if not symb == "":
            self.__symb = symb
        if not type == "":
            self.__type = type

    @property
    def symb( self ):
        return self.__symb
    @symb.setter
    def symb( self, symb ):
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
    @value.setter
    def value( self, type: str ):
        self.__type = type

    def to_string( self ):
        base_string = super().to_string()
        return f"{base_string} " \
            f"symbol={self.__sym} " \
            f"val={self.__value}"
