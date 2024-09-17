"""
This software is to handle formal systems.
"""

import objects_base as bobj
import objects_text as tobj
import objects_function as fobj
import objects_number as nobj
import objects_logic as lobj



def main():
    print( "Executing Montague" )

    OM = bobj.
    prop1 = tobj.Proposition( "This is also a proposition." )
    prop2 = tobj.Proposition( "is(Socrates,mortal)", "predcalc" )
    print( prop1.toString() )
    print( prop2.toString() )

    proc1 = fobj.Process( "Test Process",
        { "first_arg": [ "number", "first_body" ],
            "second_arg" : [ "proposition" , "second_body" ],
            "third_arg" : [ "set", "third_body" ] } )
    print( proc1.toString() )

    set1 = nobj.Set( {3,4,5,1}, "Test" )
    print( set1.toString() )

    var1 = lobj.Variable( "x", "length" )
    var1.setVal( set1 )
    print( var1.toString() )

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
