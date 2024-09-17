from dataclasses import dataclass, field
import utility as U
from uuid import uuid4

# ----------------------------------------------------------------
# OBJECT
# ----------------------------------------------------------------

"""
Base class for all objects contained in the montague application.
"""

@dataclass
class Object:
    __uuid : str = ""
    __type : str = ""
    __name : str = ""
    __delim : str = "`"

    def __init__ ( self, name = "" ):
        self.__uuid = uuid4() # returns UUID obj and not string; to convert str(self.__uuid)
        self.__type = type( self )
        if not name == "":
            self.__name = name

    @property
    def uuid( self ):
        return self.__uuid
    @uuid.setter
    def uuid( self, uuid ):
        self.__uuid = uuid
    def get_uuid_str( self ):
        return str( self.__uuid )
    def regen_uuid( self ):
        self.__uuid = uuid4()

    @property
    def type( self ):
        return self.__type

    @property
    def name( self ):
        return self.__name
    @name.setter
    def name( self, name ):
        self.__name = name

    @property
    def delim( self ):
        return self.__delim
    @delim.setter
    def delim( self, delim ):
        self.__delim = delim

    def toString( self ):
        return f"uuid={self.__uuid} " \
            f"type={self.__type} " \
            f"name={self.__delim}{self.__name}{self.__delim} "

# ----------------------------------------------------------------
# OBJECTMANAGER
# ----------------------------------------------------------------

"""
Keeps track of metadata about all objects that have been instanticated
"""

@dataclass
class ObjectManager:
    __object_dict : dict = field( default_factory=dict )

    def __init__( self ): # NEED TO INCLUDE SELF HERE OR CAUSES DOWNSTREAM PROBLEMS
        print( "Creating ObjectManager" )
        self.__object_dict = {}

    @property
    def object_list( self ):
        return self.__object_dict

    def add_object( self, obj ):
        #self.__object_dict[ U.get_substring( obj.uuid, "'", "'" ) ] = obj
        self.__object_dict[ str( obj.uuid ) ] = obj

    def pop_object( self, obj ):
        return self.__object_dict.pop( obj.get_uuid_str() )

    def list_keys( self ):
        return list( self.__object_dict.keys() )
        
    def get_val_by_key( self, key ):
        return self.__object_dict.get( key )
    
    def get_size( self ):
        return len( self.__object_dict )
    
    """ EXPERIMENTAL
    def create_obj( self, obj_cmd ):
        exec( obj_cmd )
    """