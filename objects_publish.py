import globals as G
import inspect as I
from dataclasses import dataclass, field

from objects_base import Object

@dataclass
class Document:
    __contents: list = field( default_factory=list )
    __type: str = ""

    def __init__ ( self, name = "", contents: list = [], type: str = "" ):
        if G.debug:
            print( f"{self.__class__.__name__}.{I.currentframe().f_code.co_name}() called by {I.stack()[1].function}()" )
            print( f"\tname='{name}'\n\tcontents='{contents[0]}'...\n\ttype='{type}'" )
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
