from dataclasses import dataclass, field
from objects_base import Object

@dataclass
class Process( Object ):
    __args: dict = field( default_factory=dict )
    __body: str = ""

    def __init__ ( self, name: str = "", args: dict = {}, body: str = "" ):
        super().__init__( name )
        self.__args = args
        self.__body = body

    @property
    def args( self ):
        return self.__args
    @args.setter
    def args( self, args: dict ):
        self.__args = args

    def toPython( self ):
        args_expr = ""
        for each_arg in self.args.keys():
            args_expr += each_arg + ", "
        args_expr = args_expr[ 0: len(args_expr)-2 ] # Get rid of last comma and space in text sequence
        python_expr = f"def {self.name}( {args_expr} ):\n" \
            f"\t{self.__body}"
        return python_expr
    
    def toString( self ):
        base_string = super().toString()
        return f"{base_string} " \
            f"args={self.__args}"
    