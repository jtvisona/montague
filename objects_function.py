import globals as G
import inspect as I
from dataclasses import dataclass, field
from objects_base import Object
from objects_code import Fragment

@dataclass
class Process( Object ):
    __args: dict = field( default_factory=dict )
    __body: Fragment = ""
    __body2: str = "test"

    def __init__ ( self, name: str = "", args: dict = {}, body: Fragment = "" ):
        if G.debug:
            print( f"{self.__class__.__name__}.{I.currentframe().f_code.co_name}() called by {I.stack()[1].function}()" )
            print( f"name='{name}'\nargs='{dict}'\nbody='{body}'" )
        super().__init__( name )
        self.__args = args
        self.__body = body

    @property
    def args( self ):
        return self.__args
    @args.setter
    def args( self, args: dict ):
        self.__args = args

    def to_python( self ):
        args_expr = ""
        for each_arg in self.args.keys():
            args_expr += each_arg + ", "
        args_expr = args_expr[ 0: len(args_expr)-2 ] # Get rid of last comma and space in text sequence
        python_expr = f"def {self.name}( {args_expr} ):\n" \
            f"\t{str(self.__body)}"
        return python_expr
    
    def to_string( self ):
        base_string = super().to_string()
        body_string = self.__body.name
        return f"{base_string} " \
            f"args={self.__args} " \
            f"body={body_string}"
            #f"body={ self.__body.to_stringified_lines() }" # can't produce lines
            #f"body={type( self.__body )}"
            
    