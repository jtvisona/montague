# utility imports
import tkinter as TK
from tkinter import ttk as TTK, messagebox as MBOX
from dataclasses import dataclass, field
import logging
logger = logging.getLogger( __name__ )

# montague imports
import objects_interpreters as INT
from objects_base import Object

# ----------------------------------------------------------------
# APPLICATION
# ----------------------------------------------------------------

@dataclass
class Application( Object ):

    # For tkinter root
    _app_root = ""
    _frame = ""
    _padding = "15 15 15 15"

    _button_load_script = ""
    _button_exec_script = ""
    _button_save = ""
    _button_clear = ""
    _button_exec_command = ""

    _entry_text_selection : str = field( default_factory=str )
    _entry_command : str = field( default_factory=str )
    _entry_script : str = field( default_factory=str )
    _memo_output : str = field( default_factory=str )

    # put pointer to current object in manager
    _obj_manager : object = field( default_factory=object )
    _cli : object = field( default_factory=object )

    # script management
    _current_script = "/scripts_montague/set_example.py"
    _script_string : str = field( default_factory=str )

    # --------------------------------
    # INIT
    # --------------------------------

    def __init__( self, app_root, obj_man, inter ):
        logger.debug( f"{app_root=} {obj_man=}" )

        self._app_root = app_root
        self._obj_manager = obj_man
        self._interpreter = inter
        self._script_string = 'print( "Hello, world!!!" )'

        # --------------------------------
        # GUI
        # --------------------------------
        # FRAME
        self._frame = TTK.Frame( self._app_root, padding=self._padding ).grid( row=0, column=0 )

        # --------
        # ROW 0
        # --------
        current_row = 0
        
        # OBJECT SELECTOR
        TTK.Label( self._frame, text="Object Selected" ).grid( row=0, column=0, padx=5, pady=5, sticky=TK.W )
        self._entry_text_selection = TK.StringVar()
        self._entry_text_selection.set( "This is a test." )
        self._app_root.update()
        self._entry_text_selection = TTK.Entry( self._frame, width=25, textvariable=self._entry_text_selection )
        self._entry_text_selection.grid( row=current_row, column=1, padx=5, pady=5, sticky=TK.W )

        # BUTTON: LIST OBJECTS
        self.open_subroot_button = TK.Button(self._app_root, text="List objects", command=self.click_button_open_subroot)
        self.open_subroot_button.grid( row=current_row, column=2, padx=5, pady=5, sticky=TK.W )

        # --------
        # ROW 1
        # --------
        current_row = 1
        

        # BUTTON: LOAD SCRIPT
        self._button_load_script = TTK.Button( self._frame, text="Load script", command=self.click_button_load_script )
        self._button_load_script.grid( row=current_row, column=0, padx=5, pady=5, sticky=TK.W )
        
        # ENTRY TEXT: SCRIPT
        self._entry_script = TK.StringVar()
        self._entry_script = TTK.Entry( self._frame, width=25, textvariable=self._entry_script )
        self._entry_script.grid( row=current_row, column=1, padx=5, pady=5, sticky=TK.W )

        # BUTTON: EXECUTE SCRIPT
        self._button_exec_script = TTK.Button( self._frame, text="Execute script", command=self.click_button_exec_script )
        self._button_exec_script.grid( row=current_row, column=2, padx=5, pady=5, sticky=TK.W )

        # --------
        # ROW 2
        # --------
        current_row = 2

        # LABEL: COMMAND
        TTK.Label( self._frame, text="Command" ).grid( row=current_row, column=0, padx=5, pady=5, sticky=TK.W )
        
        # ENTRY TEXT: COMMAND
        self._entry_command = TK.StringVar()
        self._entry_command = TTK.Entry( self._frame, width=25, textvariable=self._entry_command )
        self._entry_command.grid( row=current_row, column=1, padx=5, pady=5, sticky=TK.W )

        # BUTTON: EXECUTE COMMAND
        self._button_exec_command = TTK.Button( self._frame, text="Execute command", command=self.click_button_exec_command )
        self._button_exec_command.grid( row=current_row, column=2, padx=5, pady=5, sticky=TK.W )

        # --------
        # ROW 3
        # --------
        current_row = 3

        # BUTTON: SAVE OUTPUT
        self._button_save = TTK.Button( self._frame, text="Save output", command=self.click_button_save_output )
        self._button_save.grid( row=current_row, column=0, padx=5, pady=5, sticky=TK.W )

        # BUTTON: CLEAR OUTPUT
        self._button_clear = TTK.Button( self._frame, text="Clear output", command=self.click_button_clear_memo )
        self._button_clear.grid( row=current_row, column=1, padx=5, pady=5, sticky=TK.W )

        # --------
        # ROW 4
        # --------
        current_row = 4

        # MEMO: OUTPUT
        self._memo_output = TK.Text( self._app_root, height=20, width=100 )
        self._memo_output.grid( row=current_row, column=0, columnspan=3, padx=5, pady=5, sticky=TK.W )



        # Maybe make About button?
        #MBOX.showinfo( "Montague", "Montague Tool for Sentiment Analysis" )

    # --------------------------------
    # BUTTON METHODS
    # --------------------------------

    # NB Don't forget to use .get() on text_entries

    def click_button_open_subroot( self ):
        subroot = TK.Toplevel( self._app_root )
        subroot.title( "List Objects" )

    def click_button_save_output( self ):
        memo_content = self._memo_output.get("1.0", TK.END).strip()
        if memo_content:
            with open("output.txt", "w") as file:
                file.write( memo_content )
            MBOX.showinfo( "Success", "Output from script saved successfully!" )
        else:
            MBOX.showwarning("Input Error", "There is no output to save.")

    def click_button_load_script( self ):
        MBOX.showwarning( "Loading script!", f"Loading script: {self._entry_script.get()}" )

    def click_button_exec_script( self ):
        output = f"{self._entry_script.get()} executed"
        self._memo_output.delete( "1.0", "end" )
        self._memo_output.insert( TK.END, output )

    def click_button_exec_command( self ):
        output = ""
        self._memo_output.delete( "1.0", "end" )
        command = self._entry_command.get().strip()
        output = self._interpreter.process_command( command )
        self._memo_output.insert( TK.END, output)

    def click_button_save_output( self ):
        memo_content = self._memo_output.get( "1.0", TK.END ).strip()
        if memo_content:
            with open("output.txt", "w") as file:
                file.write( memo_content )
            MBOX.showinfo("Success", "Output from script saved successfully!")
        else:
            MBOX.showwarning("Input Error", "There is no output to save.")

    def click_button_clear_memo( self ):
        #self._memo_output.clipboard_get
        self._memo_output.delete( "1.0", "end" )

    """
    def __post_init__( self ):
        logger.debug( "Called" )
        self._entry_text_selection.set( "This is a test." )
    """
