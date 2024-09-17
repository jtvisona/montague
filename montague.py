"""
This software is to handle formal systems.
"""

import objects_base as bobj
import objects_text as tobj
#import objects_function as fobj
#import objects_number as nobj
#import objects_logic as lobj

def main():
    print( "Executing Montague" )
    OM = bobj.ObjectManager()
    
    # --------------------------------
    # objects_text
    # --------------------------------

    prop1 = tobj.Proposition( "This is also a proposition." )
    prop2 = tobj.Proposition( "is(Socrates,mortal)", "predcalc" )
    prop1.regen_uuid()
    print( prop1.toString() )
    print( prop2.toString() )
    OM.add_object( prop1 )
    OM.add_object( prop2 )
    print( OM.list_keys() )
    print( OM.get_val_by_key( prop2.get_uuid_str() ) )
    print( OM.get_size() )
    OM.pop_object( prop2 )
    print( OM.object_list )
    

    # --------------------------------
    # objects_function
    # --------------------------------

    """
    proc1 = fobj.Process( "Test Process",
        { "first_arg": [ "number", "first_body" ],
            "second_arg" : [ "proposition" , "second_body" ],
            "third_arg" : [ "set", "third_body" ] } )
    print( proc1.toString() )
    """

    # --------------------------------
    # objects_data_structure
    # --------------------------------

    """
    set1 = nobj.Set( {3,4,5,1}, "Test" )
    print( set1.toString() )
    """

    # --------------------------------
    # objects_logic
    # --------------------------------

    """
    var1 = lobj.Variable( "x", "length" )
    var1.setVal( set1 )
    print( var1.toString() )
    """

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
