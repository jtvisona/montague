from dataclasses import dataclass, field
#import tkinter as tk
#from tkinter import messagebox

# ----------------------------------------------------------------
# OBJECTMANAGER
# ----------------------------------------------------------------

"""
Keeps track of metadata about all objects that have been instanticated
"""

@dataclass
class ObjectManager:
    __object_list : dict = field( default_factory=dict )

    def __init__():
        print( "Creating ObjectManager" )
        __object_list = []

    def add_object( self, obj ):
        self.__object_list[ obj.uuid ] = obj
    
    def object_list( self ):
        print( self.__object_list )
        return "yay"
