"""
This software is to handle formal systems.
"""

import objects_adt as ADT
import objects_base as BASE
import objects_function as FUN
import objects_logic as LOGIC
import objects_text as TEXT

#import objects_logic as LOGIC

def main():
    print( "Executing Montague" )
    OM = BASE.ObjectManager()
    
    # --------------------------------
    # objects_adt
    # --------------------------------

    """
    set1 = ADT.Set( "TestSet", {3,4,5,1}, "whole" )
    for each_value in list( set1.value ):
        print( "'" + str( each_value ) + "'", end= " " )
    print()
    print( set1.toString() )
    """
    
    # --------------------------------
    # objects_function
    # --------------------------------

    """
    proc1 = FUN.Process( "function_call",
        { "first_arg": { "number" },
            "second_arg" : { "proposition" },
            "third_arg" : { "set" }
        },
        "DO SOME STUFF"
    )
    #print( proc1.toString() )
    #print( proc1.toPython() )
    """

    # --------------------------------
    # objects_logic
    # --------------------------------

    """
    var1 = LOGIC.Variable( "x", "length" )
    var1.setVal( set1 )
    print( var1.toString() )
    """

    # --------------------------------
    # objects_text
    # --------------------------------
    """
    prop1 = TEXT.Proposition( "This is also a proposition." )
    prop2 = TEXT.Proposition( "is(Socrates,mortal)", "predcalc" )
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
    OM.create_obj( exec_command )
    print( OM.list_keys() )
    """

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
