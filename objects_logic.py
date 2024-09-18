from dataclasses import dataclass, field
from objects_base import Object

@dataclass
class Variable:
    __symb : str = ""
    __type : str = ""
    __value : object = field( default_factory=object )

    def __init__ ( self, name = "", symb = "", type = "" ):
        super().__init__( name )
        if not symb == "":
            self.__symb = symb
        if not type == "":
            self.__type = type

    @property
    def symb( self ):
        return self.__sym
    @symb.setter
    def symb( self, __sym ):
        self.__sym = __sym

    @property
    def value( self ):
        return self.__value
    @value.setter
    def value( self, __value ):
        self.__value = __value

    @property
    def type( self ):
        return self.__type
    @value.setter
    def value( self, type ):
        self.__type = type

    def toString( self ):
        base_string = super().toString()
        return f"{base_string} " \
            f"symbol={self.__sym} " \
            f"val={self.__value}"
