import globals as G
import utility as U
from dataclasses import dataclass, field
from objects_text import Memo

@dataclass
class Fragment( Memo ):

    __type: str = ""

    def __init__ ( self, name: str = "", lines: list = [], lang = "", type = "" ):
        if G.debug == True:
            print( f"name='{name}'\nlines='{lines[0]}'...\nlang='{lang}'" )
        super().__init__( name, lines, lang )
        self.__type = type

    @property
    def lines( self ):
        return super().__lines
    @lines.setter
    def value( self, lines: list ):
        super().__lines = lines

    def add_newlines( self ):
        for index, each_line in enumerate( super().__lines ):
            super().__lines[ index ] = each_line + "\n"
    
    def remove_newlines( self ):
        for index, each_line in enumerate( super().__lines ):
            super().__lines[ index ] = U.drop_nl( each_line )

    def has_newlines( self ):
        has_flag = True
        for each_line in self.__lines:
            if each_line[len(each_line)-1] == "\n":
                pass
            else:
                has_flag = False
                break
        return has_flag

    #def exec( self ):
    #def number_lines( self ):
    #def add_terminator( self, terminator ):
    #def remove_terminator( self ):

    def stringify_lines( self ):
        return str( super().__lines )

    def concat_and_stringify_lines( self ):
        concated_str = ""
        for each_line in super().__lines:
            concated_str += each_line
        return concated_str

    def to_string( self ):
        base_string = super().to_string()
        return base_string
