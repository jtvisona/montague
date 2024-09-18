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
    obj_man = BASE.ObjectManager()
    
    # --------------------------------
    # objects_adt
    # --------------------------------

    """
    # Set example
    set1 = ADT.Set( "TestSet", {3,4,5,1}, "whole" )
    for each_value in list( set1.value ):
        print( "'" + str( each_value ) + "'", end= " " )
    print()
    print( set1.to_string() )
    """
    """
    # Multiset example
    mset1 = ADT.Multiset( "TestSet", [3,4,5,1,1], "whole" )
    #for each_value in list( mset1.value ):
    #    print( "'" + str( each_value ) + "'", end= " " )
    #print()
    print( mset1.to_stringified_list() )
    #print( mset1.to_string() )
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
        "DO Sobj_manE STUFF"
    )
    #print( proc1.to_string() )
    #print( proc1.toPython() )
    """

    # --------------------------------
    # objects_logic
    # --------------------------------

    """
    var1 = LOGIC.Variable( "x", "length" )
    var1.setVal( set1 )
    print( var1.to_string() )
    """

    # --------------------------------
    # objects_text
    # --------------------------------

    lines = [ "This is a test of the EBS.\n", \
        "This is only a test.\n",
        "If this were a real emergency...\n" ]
    memo1 = TEXT.Memo( "test", lines )
    #print( memo1.to_string() )
    #print( memo1.to_stringified_list() )
    print( memo1.to_stringified_lines() )
    

    """
    # Argument example
    prop1 = TEXT.Proposition( "P1", "All men are mortal.", "english" )
    prop2 = TEXT.Proposition( "P2", "Socrates is a man.", "english" )
    concl = TEXT.Proposition( "C", "Socrates is mortal.", "english" )
    obj_man.add_object( prop1 ) # CONVERT TO: prop1.register( obj_man )

    arg1 = TEXT.Argument( "syllogism", [prop1, prop2], concl )
    print( arg1.toMultiString() )
    """

    """
    # Expand examples
    prop1 = TEXT.Proposition( "P1", "All men are mortal.", "english" )
    prop2 = TEXT.Proposition( "P2", "Socrates is a man.", "english" )
    #prop1.regen_uuid()
    #print( prop1.to_string() )
    #print( prop2.to_string() )
    # print( obj_man.list_keys() )
    #print( obj_man.get_val_by_key( prop2.get_uuid_str() ) )
    #print( obj_man.get_size() )
    #obj_man.pop_object( prop2 )
    #print( obj_man.object_list )
    #print( obj_man.list_keys() )
    """

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
