"""
This software is to handle formal systems.
"""

import utility as U
import object_man as OM

import objects_adt as ADT
import objects_base as BASE
import objects_code as CODE
import objects_function as FUN
import objects_logic as LOGIC
import objects_text as TXT

def main():
    print(  "executing Montague" )
    obj_man = OM.ObjectManager()
    
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
    # objects_base
    # --------------------------------

    """
    # Phrase and Sentence examples
    sen1 = TXT.Sentence( "first", "the big house is nearby", "decl" )
    print( str(sen1.uuid) )
    sen1.regen_uuid()
    print( str(sen1.uuid) )
    #"""

    """
    # obj_man.copy_obj( key ) examples
    sen1 = TXT.Sentence( "first", "the big house is nearby", "decl" )
    #print( sen1.to_string() )
    obj_man.add_object( sen1 )
    #print( obj_man.list_keys() )
    #print( obj_man.stringified_list_keys() )
    print( obj_man.annotated_list_keys() )
    obj_man.copy_obj( sen1 )
    print( obj_man.annotated_list_keys() )
    #"""

    # --------------------------------
    # objects_code
    # --------------------------------

    ""
    # Phrase and Sentence examples
    code_fragment = [   "my_set = { 1, 2, 3 }",
                        "for each_element in my_set:",
                        "  print( each_element )"
    ]
    code1 = CODE.Fragment( "fragment", code_fragment, "python" )
    code1.add_newlines()
    print( code1.concat_and_stringify_lines() )
    #exec( code1.concat_and_stringify_lines() )
    code1.remove_newlines()
    print( code1.value )

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
    sen1 = ( "S1", "All men are mortal." )
    sen2 = ( "S2", "Socrates is a man." )
    sen3 = ( "S3", "Socrates is mortal." )
    prop1 = TXT.Proposition( "P1", sen1 )
    prop2 = TXT.Proposition( "P2", sen2 )
    concl = TXT.Proposition( "C", sen3 )

    arg1 = TXT.Argument( "syllogism", [prop1, prop2], concl )
    print( arg1.toMultiString() )
    #"""

    """
    # Proposition example
    sen1 = TXT.Sentence( "example", "Die Gedanken sind Frei.", "german")
    prop1 = TXT.Proposition( "P", sen1, True )
    print( prop1.stringify_sentence() )
    print( prop1.stringify_appraised_truth_cond() )
    #"""

    """
    # Proposition examples
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

    #"""

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
