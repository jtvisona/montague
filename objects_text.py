from dataclasses import dataclass
from objects_base import Object

@dataclass
class Proposition( Object ):
    __prop : str = "There is no assigned proposition."
    __lang : str = "english"

    def __init__ ( self, prop = "", lang = "" ):
        super().__init__()
        if not prop == "":
            self.__prop = prop
        if not lang == "":
            self.__lang = lang

    @property
    def prop( self ):
        return self.__prop
    @prop.setter
    def prop( self, prop ):
        self.__prop = prop

    def toString( self ): # Cannot put ANYTHING after backslash in these explict continuations
        base_string = super().toString()
        return f"{base_string} " \
        f"prop={super().delim}{self.__prop}{super().delim} " \
            f"lang={self.__lang}"