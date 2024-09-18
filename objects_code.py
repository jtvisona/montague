import utility as U
from dataclasses import dataclass, field
from objects_text import Memo

@dataclass
class Fragment( Memo ):
    __lines: list = field( default_factory=list )

    def __init__ ( self, name: str = "", lines: list = [], lang = "" ):
        super().__init__( name=name, lang=lang )
        self.__lines = lines

    @property
    def lines( self ):
        return self.__lines
    @lines.setter
    def value( self, lines: list ):
        self.__lines = lines

    def add_newlines( self ):
        for index, each_line in enumerate( self.__lines ):
            #print( f"Modifying line {index}:{U.squote(each_line)}" )
            self.__lines[ index ] = each_line + "\n"
    
    def remove_newlines( self ):
        for index, each_line in enumerate( self.__lines ):
            #text = U.squote( str( each_line[ len(each_line)-2: len(each_line) ] ) )
            #print( f"Modifying line {index}:{text} " )
            self.__lines[ index ] = U.drop_nl( each_line )

    def stringify_lines( self ):
        return str( self.__lines )

    def concat_and_stringify_lines( self ):
        concated_str = ""
        copy_lines = self.__lines
        for each_line in copy_lines:
            #each_line = each_line.replace( "{", "\{" ) # Add detect backslash and maybe make utility function remove_escapes(), etc.
            #each_line = each_line.replace( "}", "\}" )
            concated_str += each_line
        return concated_str

    def to_string( self ):
        base_string = super().to_string()
        return base_string
