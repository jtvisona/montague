"""
This software is to handle formal systems.
"""
import text_objects as tobj
from uuid import uuid4

def main():
    print( "Executing montague" )
    p1 = tobj.Proposition()
    p2 = tobj.Proposition( "This is also a proposition." )
    print( p1.toString() )
    print( p2.toString() )



# if this module is called first, call the main function
if __name__ == "__main__":
    main()