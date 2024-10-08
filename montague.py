# Utility modules
#import utility as U
#import sys as SYS
import tkinter as TK
from tkinter import ttk as TTK, messagebox as MBOX
from dataclasses import dataclass, field

import logging
logger = logging.getLogger( __name__ )

# Montague modules
"""
import object_man as OM
import objects_adt as ADT
import objects_base as BASE
import objects_code as CODE
import objects_function as FUN
import objects_logic as LOGIC
import objects_text as TXT
"""

@dataclass
class Application():

    # For tkinter root
    __app_root = ""
    __frame = ""
    __padding = "15 15 15 15"

    __button_exit = ""
    __button_load_script = ""
    __button_exec_script = ""
    __button_save = ""
    __button_clear = ""
    __button_exec_command = ""

    __entry_text_selection : str = field( default_factory=str )
    __entry_command : str = field( default_factory=str )
    __memo_output : str = field( default_factory=str )

    # put pointer to current object in manager
    __obj_manager : object = field( default_factory=object )

    # script management
    __current_script = "/scripts_montague/set_example.py"
    __script_string : str = field( default_factory=str )

    # --------------------------------
    # INIT
    # --------------------------------

    def __init__( self, app_root, obj_man ):
        logger.info( "Application.__init__()" )
        
        self.__app_root = app_root
        self.__obj_manager = obj_man
        self.__script_string = 'print( "Hello, world!!!" )'

        # FRAME
        self.__frame = TTK.Frame( self.__app_root, padding=self.__padding )
        self.__frame.pack( fill=TK.BOTH, expand=True )

        # BUTTON: EXIT
        self.__button_exit = TTK.Button( self.__frame, text="Exit Montague", command=self.click_button_exit )
        self.__button_exit.pack()

        # OBJECT SELECTOR
        TTK.Label( self.__frame, text="Object Selected" ).pack()
        self.__entry_text_selection = TK.StringVar()
        self.__entry_text_selection.set( "This is a test." )
        #self.__entry_text_selection = TTK.Entry( self.__frame, width=25, textvariable=self.__entry_text_selection, state="readonly" )
        self.__entry_text_selection = TTK.Entry( self.__frame, width=25, textvariable=self.__entry_text_selection )
        self.__entry_text_selection.pack()

        # BUTTON: LIST OBJECTS
        self.open_subroot_button = TK.Button(self.__app_root, text="List objects", command=self.click_button_open_subroot)
        self.open_subroot_button.pack()

        # BUTTON: LOAD SCRIPT
        self.__button_load_script = TTK.Button( self.__frame, text="Load script", command=self.click_button_load_script )
        self.__button_load_script.pack()

        # BUTTON: EXECUTE SCRIPT
        self.__button_exec_script = TTK.Button( self.__frame, text="Execute script", command=self.click_button_exec_script )
        self.__button_exec_script.pack()

        # BUTTON: SAVE OUTPUT
        self.__button_save = TTK.Button( self.__frame, text="Save output", command=self.click_button_save_output )
        self.__button_save.pack()

        # BUTTON: CLEAR OUTPUT
        self.__button_clear = TTK.Button( self.__frame, text="Clear output", command=self.click_button_clear_memo )
        self.__button_clear.pack()
        
        # ENTRY TEXT: COMMAND
        TTK.Label( self.__frame, text="Command" ).pack()
        self.__entry_command = TK.StringVar()
        self.__entry_command = TTK.Entry( self.__frame, width=25, textvariable=self.__entry_command )
        self.__entry_command.pack()

        # BUTTON: EXECUTE COMMAND
        self.__button_exec_command = TTK.Button( self.__frame, text="Execute command", command=self.click_button_exec_command )
        self.__button_exec_command.pack()

        # MEMO: OUTPUT
        self.__memo_output = TK.Text( self.__app_root, height=10, width=100 )
        self.__memo_output.pack()

        # Moved to end because allows rendering and makes text entries writable; no idea why
        MBOX.showinfo( "Montague", " Montague Tool for Sentiment Analysis" )
        MBOX.showinfo( "Montague", " Version 0.0.1" )

    # --------------------------------
    # BUTTON METHODS
    # --------------------------------

    def click_button_open_subroot( self ):
        subroot = TK.Toplevel( self.__app_root )
        subroot.title( "List Objects" )

    def click_button_save_output( self ):
        memo_content = self.__memo_output.get("1.0", TK.END).strip()
        if memo_content:
            with open("output.txt", "w") as file:
                file.write( memo_content )
            MBOX.showinfo("Success", "Output from script saved successfully!")
        else:
            MBOX.showwarning("Input Error", "There is no output to save.")

    def click_button_load_script( self ):
        MBOX.showwarning( "Loading script!", f"Loading script: {self.__current_script}" )
        self.__script_string = "printf( \"Hello, world!!!\" )"

    def click_button_exec_script( self ):
        #exec( )
        output = "Script executed"
        self.__memo_output.insert( TK.END, output )

    def click_button_exec_command( self ):
        #exec( )
        output = "Script executed"
        self.__memo_output.insert( TK.END, output )

    def click_button_save_output( self ):
        memo_content = self.__memo_output.get("1.0", TK.END).strip()
        if memo_content:
            with open("output.txt", "w") as file:
                file.write( memo_content )
            MBOX.showinfo("Success", "Output from script saved successfully!")
        else:
            MBOX.showwarning("Input Error", "There is no output to save.")

    def click_button_clear_memo( self ):
        #self.__memo_output.clipboard_get
        #self.__memo_output.destroy()
        self.__memo_output.delete( "1.0", "end" )

    def click_button_exit( self ):
        #self.__app_root.title( """ )
        self.__app_root.destroy()

    def __post_init__( self ):
        self.__entry_text_selection.set( "This is a test." )
