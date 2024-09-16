"""
This software is to handle formal systems.
"""
import text_objects as tobj
import function_objects as fobj

def main():
    print( "Executing Montague" )

    p1 = tobj.Proposition()
    p2 = tobj.Proposition( "This is also a proposition." )
    print( p1.toString() )
    print( p2.toString() )

    f1 = fobj.Process( "Test Process",
        { "first_arg": [ "number", "first_body" ],
            "second_arg" : [ "proposition" , "second_body" ],
            "third_arg" : [ "set", "third_body" ] } )
    print( f1.toString() )


# if this module is called first, call the main function
if __name__ == "__main__":
    main()