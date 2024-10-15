# Utility imports
import globals as G
import utility as U
import inspect as I
import copy as CP
from dataclasses import dataclass, field
import logging
logger = logging.getLogger( __name__ )

# Montague imports
from objects_base import Object
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
class ObjectManager( Object ):
    _object_list : dict = field( default_factory=dict )
    _linked_interpreter : object = field( default_factory=object )

    def __init__( self, name="", interpreter="" ):
        logger.debug( "Called " )
        self._object_list = []
        logger.info( "Assigning intepreter to object manager" )
        self._linked_interpreter = interpreter
        #self._linked_interpreter.link_to_manager( self )

    @property
    def object_list( self ):
        return self._object_list

    def add_object( self, obj: object ) -> bool:
        self._object_list[ obj.uuid ] = obj

    #def pop_object( self, obj: object ):

    """
    def list_keys( self ):
        if G.debug:
            logger.info( "*** ObjectManager.list_keys()" )
        return list( self.__obj_register.keys() )
    """
    """
    def stringified_list_keys( self ):
        if G.debug:
            logger.info( "*** ObjectManager.stringified_list_keys()" )
        return str( list( self.__obj_register.keys() ) )
    """
    """
    def annotated_list_keys( self ):
        return "*** ObjectManagerRegister:" + str( list( self.__obj_register.keys() ) )
    """
    """
    def get_val_by_key( self, key: str ): ## Maybe should leave key type as UUID to tighten type system?
        if G.debug:
            logger.info( "*** ObjectManager.get_val_by_key()" )
        return self.__obj_register.get( key )
    """
    """
    def get_size( self ) -> int:
        return len( self.__obj_register )
    """
    """
    def copy_obj( self, obj: object ) -> object:
        original_uuid = obj.stringified_uuid()
        original_object = self.__obj_register[ original_uuid ]
        copied_object = CP.deepcopy( original_object )
        copied_object.regen_uuid()

        return copied_object
    """
    """
    def create_obj( self, obj_cmd ):
    """


