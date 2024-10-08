import globals as G
import utility as U
import inspect as I
from dataclasses import dataclass, field

import copy as CP

import objects_adt as ADT
import objects_base as BASE
import objects_function as FUN
import objects_logic as LOGIC
import objects_text as TXT

import logging
logger = logging.getLogger( __name__ )

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
        self.__obj_register = {}

    @property
    def object_list( self ):
        return self.__obj_register

    def add_object( self, obj: object ) -> bool:
        success_flag = True
        if  G.debug:
            logger.info( "*** ObjectManager.add_object( object ) -> bool" )
            logger.info( f"* Args\n\t{obj.__class__}")
        self.__obj_register[ str( obj.uuid ) ] = obj
        return success_flag

    def pop_object( self, obj: object ):
        if  G.debug:
            logger.info( "*** ObjectManager.pop_object()" )
            logger.info( f"* Args\n\t{obj.__class__}")
        return self.__obj_register.pop( obj.get_uuid_str() )

    def list_keys( self ):
        if G.debug:
            logger.info( "*** ObjectManager.list_keys()" )
        return list( self.__obj_register.keys() )

    def stringified_list_keys( self ):
        if G.debug:
            logger.info( "*** ObjectManager.stringified_list_keys()" )
        return str( list( self.__obj_register.keys() ) )

    def annotated_list_keys( self ):
        return "*** ObjectManagerRegister:" + str( list( self.__obj_register.keys() ) )

    def get_val_by_key( self, key: str ): ## Maybe should leave key type as UUID to tighten type system?
        if G.debug:
            logger.info( "*** ObjectManager.get_val_by_key()" )
        return self.__obj_register.get( key )
    
    def get_size( self ) -> int:
        if G.debug:
            logger.info( "*** ObjectManager.get_size()" )
        return len( self.__obj_register )

    def copy_obj( self, obj: object ) -> object:
        if G.debug:
            logger.info( f"*** ObjectManager.copy_obj() -> object\n " \
                  f"* Args:\n\tobj={str(obj.__class__)}" )
        original_uuid = obj.stringified_uuid()
        if G.debug:
            logger.info( f"- Copying {original_uuid}")
        original_object = self.__obj_register[ original_uuid ]
        copied_object = CP.deepcopy( original_object )
        copied_object.regen_uuid()
        if G.debug:
            logger.info( f"- Copied {original_object.uuid} to {copied_object.uuid}" )
        self.__obj_register[ str( copied_object.uuid ) ] = copied_object
        return copied_object

    """
    def create_obj( self, obj_cmd ):
    """
