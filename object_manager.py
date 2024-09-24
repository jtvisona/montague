from dataclasses import dataclass, field

# ----------------------------------------------------------------
# OBJECTMANAGER
# ----------------------------------------------------------------

"""
Keeps track of metadata about all objects that have been instanticated
"""

@dataclass
class ObjectManager:
    __objectList : dict = field( default_factory=dict )

    def __init__():
        print( "Creating ObjectManager" )
        __objectList = []

    def addObject( self, obj ):
        self.__objectList[ obj.uuid ] = obj
    
    def objectList( self ):
        print( self.__objectList )
        return "yay"
