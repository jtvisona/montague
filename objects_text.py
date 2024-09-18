from dataclasses import dataclass, field
from objects_base import Object
 
@dataclass
class Proposition( Object ):
    __val : str = "There is no assigned valosition."
    __lang : str = "english"

    def __init__ ( self, name = "", val = "", lang = "" ):
        super().__init__( name )
        if not val == "":
            self.__val = val
        if not lang == "":
            self.__lang = lang

    @property
    def val( self ):
        return self.__val
    @val.setter
    def val( self, val ):
        self.__val = val

    def toString( self ): # Cannot put ANYTHING after backslash in these explict continuations
        base_string = super().toString()
        return f"{base_string} " \
        f"val={super().delim}{self.__val}{super().delim} " \
            f"lang={self.__lang}"
    
@dataclass
class Argument( Object ):
    __premises : list = field( default_factory=list ) # Can tighten types by making this PropositionList
    __conclusion : Proposition = ""

    def __init__ ( self, name:str = "", premises:list = [], conclusion:Proposition = "" ): # Can tighten types by making SafeStr
        super().__init__( name )
        if not premises == []:
            self.__premises = premises
        if not conclusion == "":
            self.__conclusion = conclusion

    @property
    def premises( self ):
        return self.__premises
    @premises.setter
    def val( self, premises ):
        self.__premises = premises

    @property
    def conclusion( self ):
        return self.__conclusion
    @premises.setter
    def val( self, conclusion ):
        self.__conclusion = conclusion

    def to_multi_string( self ):
        multi_str = ""
        for prop in self.__premises:
            multi_str += prop.name + ":\t" + prop.val + "\n"
        multi_str += self.__conclusion.name + ":\t" + self.__conclusion.val + "\n"
        return multi_str

    # ADD def to_multi_MD( self ):

    def toString( self ):
        base_string = super().toString()
        return f"{base_string} " \
        f"val={super().delim}{self.__val}{super().delim} " \
        f"lang={self.__lang}"
    