from dataclasses import dataclass, field

import copy as CP

import objects_adt as ADT
import objects_base as BASE
import objects_function as FUN
import objects_logic as LOGIC
import objects_text as TXT

# ----------------------------------------------------------------
# OBJECTMANAGER
# ----------------------------------------------------------------

"""
Keeps track of metadata about all objects that have been instanticated
"""

@dataclass
class ObjectManager:
    __obj_register: dict = field( default_factory=dict )

    def __init__( self ): # NEED TO INCLUDE SELF HERE OR CAUSES DOWNSTREAM PROBLEMS
        print( "Creating ObjectManager" )
        self.__obj_register = {}

    @property
    def object_list( self ):
        return self.__obj_register

    def add_object( self, obj: object ):
        self.__obj_register[ str( obj.uuid ) ] = obj

    def pop_object( self, obj: object ):
        return self.__obj_register.pop( obj.get_uuid_str() )

    def list_keys( self ):
        return list( self.__obj_register.keys() )

    def stringified_list_keys( self ):
        return str( list( self.__obj_register.keys() ) )

    def annotated_list_keys( self ):
        return "ObjectManagerRegister:" + str( list( self.__obj_register.keys() ) )

    def get_val_by_key( self, key: str ): ## Maybe should leave key type as UUID to tighten type system?
        return self.__obj_register.get( key )
    
    def get_size( self ):
        return len( self.__obj_register )

    def copy_obj( self, obj: object ):
        original_uuid = obj.stringified_uuid()
        print( f"Copying {original_uuid}")
        original_object = self.__obj_register[ original_uuid ]
        copied_object = CP.deepcopy( original_object )
        copied_object.regen_uuid()
        print( f"{original_object.uuid} copied to {copied_object.uuid}" )
        self.__obj_register[ str( copied_object.uuid ) ] = copied_object
        return copied_object

    """
    def create_obj( self, obj_cmd ):
    """
