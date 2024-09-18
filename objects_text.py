import utility as U
from dataclasses import dataclass, field
from objects_base import Object

@dataclass
class Phrase( Object ):
    __value: str = ""
    __type: str = ""
    __lang: str = ""

    def __init__ ( self, name: str = "", value: str = "", lang: str = "english" ):
        super().__init__( name )
        self.__value = value
        self.__lang = lang

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
    def type( self, type: str ):
        self.__type = type

    def to_string( self ):
        base_string = super().to_string()
        return f"{base_string} " \
        f"val={super().delim}{self.__value}{super().delim} " \
            f"lang={self.__lang}"

@dataclass
class Sentence( Object ):
    __value: str = ""
    __type: str = ""
    __lang: str = ""

    def __init__ ( self, name: str = "", value: str = "", lang: str = "english" ):
        super().__init__( name )
        self.__value = value
        self.__lang = lang

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
    def type( self, type: str ):
        self.__type = type

    def cap_and_stop( self ):
        self.__value = U.cap_and_stop( self.__value )
    def cap_and_bang( self ):
        self.__value = U.cap_and_bang( self.__value )
    def cap_and_huh( self ):
        self.__value = U.cap_and_huh( self.__value )
    def cap_and_also( self ):
        self.__value = U.cap_and_also( self.__value )
    def uncap_and_drop( self ):
        self.__value = U.uncap_and_drop( self.__value )

    def to_string( self ): # Cannot put ANYTHING after backslash in these explict continuations
        base_string = super().to_string()
        return f"{base_string} " \
        f"val={super().delim}{self.__value}{super().delim} " \
            f"lang={self.__lang}"

@dataclass
class Memo( Object ):
    __lines: list = field( default_factory=list )
    __lang: str = ""

    def __init__ ( self, name: str = "", lines: list = "", lang: str = "english" ): # tighten types by adding Text
        super().__init__( name )
        if not lines == []:
            self.__lines = lines
        if not lang == "":
            self.__lang = lang

    @property
    def lines( self ):
        return self.__lines
    @lines.setter
    def value( self, lines: list ):
        self.__lines = lines

    def to_stringified_lines( self ):
        stringified_lines = ""
        for each_line in self.__lines:
            stringified_lines += each_line + "\n"
        return stringified_lines

    def to_stringified_list( self ):
        return str( self.__lines )

    def to_string( self ):
        base_string = super().to_string()
        return f"{base_string} " \
        f"lines={super().delim}{self.__lines}{super().delim} " \
            f"lang={self.__lang}"

@dataclass
class Proposition( Object ):
    __value: Sentence = ""
    __truth_cond: bool = ""

    def __init__ ( self, name: str = "", value: Sentence = "", truth_cond: bool = "" ):
        super().__init__( name )
        self.__value = value
        self.__truth_cond = truth_cond

    @property
    def value( self ):
        return self.__value
    @value.setter
    def value( self, value: str ):
        self.__value = value

    @property
    def truth_cond( self ):
        return self.__truth_cond
    @truth_cond.setter
    def truth_cond( self, truth_cond: bool ):
        self.__truth_cond = truth_cond

    def stringify_sentence( self ):
        sentence = self.__value
        return sentence.value

    def stringify_appraised_truth_cond( self ):
        sentence = self.__value
        return f"{U.squote(U.drop(sentence.value))} is {str(self.__truth_cond).lower()}."

    def to_string( self ):
        base_string = super().to_string()
        return f"{base_string} " \
        f"val={super().delim}{self.__value}{super().delim} " \
            f"lang={self.__lang}"
    
@dataclass
class Argument( Object ):
    __premises: list = field( default_factory=list ) # Can tighten types by making this PropositionList
    __conclusion: Proposition = ""

    def __init__ ( self, name: str = "", premises: list = [], conclusion: Proposition = "" ): # Can tighten types by making SafeStr
        super().__init__( name )
        if not premises == []:
            self.__premises = premises
        if not conclusion == "":
            self.__conclusion = conclusion

    @property
    def premises( self ):
        return self.__premises
    @premises.setter
    def presmises( self, premises: list ):
        self.__premises = premises

    @property
    def conclusion( self ):
        return self.__conclusion
    @premises.setter
    def conclusion( self, conclusion: Proposition ):
        self.__conclusion = conclusion

    def to_multi_string( self ):
        multi_str = ""
        for prop in self.__premises:
            multi_str += prop.name + ":\t" + prop.val + "\n"
        multi_str += self.__conclusion.name + ":\t" + self.__conclusion.val + "\n"
        return multi_str

    # ADD def to_multi_MD( self ):

    def to_string( self ):
        base_string = super().to_string()
        return f"{base_string} " \
        f"val={super().delim}{self.__value}{super().delim} " \
        f"lang={self.__lang}"
    