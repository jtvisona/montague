"""
This software is to handle formal systems.
"""

import utility as U
import objects_adt as ADT
import objects_base as BASE
import objects_function as FUN
import objects_logic as LOGIC
import objects_text as TXT

def main():
    print(  "executing Montague" )
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
    #"""

    """
    # Multiset example
    mset1 = ADT.Multiset( "TestSet", [3,4,5,1,1], "whole" )
    #for each_value in list( mset1.value ):
    #    print( "'" + str( each_value ) + "'", end= " " )
    #print()
    print( mset1.to_stringified_list() )
    #print( mset1.to_string() )
    #"""

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
    #"""

    # --------------------------------
    # objects_logic
    # --------------------------------

    """
    var1 = LOGIC.Variable( "x", "length" )
    var1.setVal( set1 )
    print( var1.to_string() )
    #"""

    # --------------------------------
    # objects_text
    # --------------------------------

    """
    # Phrase and Sentence examples
    sen1 = TXT.Sentence( "first", "the big house is nearby", "decl" )
    print( str(sen1.uuid) )
    sen1.regen_uuid()
    print( str(sen1.uuid) )
    #"""

    """
    # Phrase and Sentence examples
    sen1 = TXT.Sentence( "first", "the big house is nearby", "decl" )
    print( sen1.value )
    sen1.to_cap_and_stop()
    print( sen1.value )
    sen1.to_uncap_and_drop()
    print( sen1.value )
    #"""
    
    """
    # Memo example
    lines = [ "This is a test of the EBS.", \
        "This is only a test.",
        "If this were a real emergency..." ]
    memo1 = TXT.Memo( "test", lines )
    #print( memo1.to_string() )
    #print( memo1.to_stringified_list() )
    print( memo1.to_stringified_lines(), end="" )
    #"""

    """
    # Argument example
    prop1 = TXT.Proposition( "P1", "All men are mortal.", "english" )
    prop2 = TXT.Proposition( "P2", "Socrates is a man.", "english" )
    concl = TXT.Proposition( "C", "Socrates is mortal.", "english" )
    obj_man.add_object( prop1 ) # CONVERT TO: prop1.register( obj_man )

    arg1 = TXT.Argument( "syllogism", [prop1, prop2], concl )
    print( arg1.toMultiString() )
    #"""

    """
    # Proposition example
    sen1 = TXT.Sentence( "example", "Die Gedanken Sind Frei.", "german")
    prop1 = TXT.Proposition( "P", sen1, True )
    print( prop1.stringify_appraised_truth_cond() )
    #"""

    """
    # Expand examples
    sen1 = TXT.Proposition( "S1", "All men are mortal." )
    sen2 = TXT.Proposition( "S2", "Socrates is a man." )
    prop1 = TXT.Proposition( "P1", sen1 )
    prop2 = TXT.Proposition( "P2", sen2 )
    
    print( prop1.stringify_sentence() )
    print( prop2.stringify_sentence() )
    # print( obj_man.list_keys() )
    #print( obj_man.get_val_by_key( prop2.get_uuid_str() ) )
    #print( obj_man.get_size() )
    #obj_man.pop_object( prop2 )
    #print( obj_man.object_list )
    #print( obj_man.list_keys() )
    #"""

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
