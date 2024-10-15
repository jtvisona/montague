# utility imports
import io as IO
import sys as SYS
import tkinter as TK
from tkinter import ttk as TTK, messagebox as MBOX
from dataclasses import dataclass, field
import logging
logger = logging.getLogger( __name__ )

# montague imports
import utility as U
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
    _button_show_log = ""

    _entry_text_selection : str = field( default_factory=str )
    _entry_command : str = field( default_factory=str )
    _entry_script_name : str = field( default_factory=str )
    _memo_output : str = field( default_factory=str )

    # put pointer to current object in manager
    _obj_manager : object = field( default_factory=object )
    _cli : object = field( default_factory=object )

    # script management
    _script_path = ""
    _script_name = ""
    _script_buffer : str = field( default_factory=str )

    # --------------------------------
    # INIT
    # --------------------------------

    def __init__( self, application_root="", object_manager="", interpreter="" ):
        if application_root is None:
            logger.error( "No application root assigned to application" )
            raise Exception( "No application root assigned to application" )
        if object_manager is None:
            logger.error( "No object manager assigned to application" )
            raise Exception( "No object manager assigned to application" )
        if interpreter is None:
            logger.error( "No interpreter assigned to application" )
            raise Exception( "No interpreter assigned to application" )
        
        #
        #logger.debug( f"{application_root=} {object_manager=} {interpreter=}" )

        self._app_root = application_root
        self._obj_manager = object_manager
        self._interpreter = interpreter
        self._script_name = "default.py"
        self._script_path = "./"
        self._script_buffer = 'print( "Hello, world!!!" )'

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
        self._entry_text_selection = TTK.Entry( self._frame, width=50, textvariable=self._entry_text_selection )
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
        self._entry_script_name = TK.StringVar()
        self._entry_script_name = TTK.Entry( self._frame, width=50, textvariable=self._entry_script_name )
        self._entry_script_name.grid( row=current_row, column=1, padx=5, pady=5, sticky=TK.W )

        # BUTTON: EXECUTE SCRIPT
        self._button_exec_script = TTK.Button( self._frame, text="Execute script", command=self.click_button_exec_script )
        self._button_exec_script.grid( row=current_row, column=2, padx=5, pady=5, sticky=TK.W )

        # BUTTON: SHOW SCRIPT
        self._button_show_script = TTK.Button( self._frame, text="Show script", command=self.click_button_show_script )
        self._button_show_script.grid( row=current_row, column=3, padx=5, pady=5, sticky=TK.W )

        # --------
        # ROW 2
        # --------
        current_row = 2

        # LABEL: COMMAND
        TTK.Label( self._frame, text="Command" ).grid( row=current_row, column=0, padx=5, pady=5, sticky=TK.W )
        
        # ENTRY TEXT: COMMAND
        self._entry_command = TK.StringVar()
        self._entry_command = TTK.Entry( self._frame, width=50, textvariable=self._entry_command )
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

        # ENTRY TEXT: SAVE FILENAME
        self._entry_save_filename = TK.StringVar()
        self._entry_save_filename = TTK.Entry( self._frame, width=50, textvariable=self._entry_save_filename )
        self._entry_save_filename.grid( row=current_row, column=1, padx=5, pady=5, sticky=TK.W )

        # BUTTON: CLEAR OUTPUT
        self._button_clear = TTK.Button( self._frame, text="Clear output", command=self.click_button_clear_memo )
        self._button_clear.grid( row=current_row, column=2, padx=5, pady=5, sticky=TK.W )

        # BUTTON: SHOW LOG
        self._button_show_log = TTK.Button( self._frame, text="Show log", command=self.click_button_show_log )
        self._button_show_log.grid( row=current_row, column=3, padx=5, pady=5, sticky=TK.W )

        # --------
        # ROW 4
        # --------
        current_row = 4

        # MEMO: OUTPUT
        self._memo_output = TK.Text( self._app_root, height=20, width=100 )
        self._memo_output.grid( row=current_row, column=0, columnspan=4, padx=5, pady=5, sticky=TK.W )

        # Maybe make About button?
        #MBOX.showinfo( "Montague", "Montague Tool for Sentiment Analysis" )

    # --------------------------------
    # BUTTON METHODS
    # --------------------------------

    # NB Don't forget to use .get() on text_entries

    def click_button_open_subroot( self ):
        logger.info( "Called" )
        subroot = TK.Toplevel( self._app_root )
        subroot.title( "List Objects" )

    def click_button_load_script( self ):
        logger.info( "Called" )
        # pull from globals eventually; hardcoded for now
        self._script_name = self._entry_script_name.get()
        self._script_path = 'C:\\Users\\17082\\Documents\\github-repos\\montague\\'
        logger.debug( f"path:{self._script_path=} name:{self._entry_script_name}" )
        # Redirect output to child window eventually
        success_flag, self._script_buffer = U.read_file_to_text( self._script_path + self._script_name )
        logger.debug( f"{success_flag=} {self._script_buffer[:5]=}..." )
        # Advise the user of success or failure
        if success_flag:
            logger.debug( f"size of file:{len(self._script_buffer)=}" )
            self._memo_output.insert( TK.END, f"Loaded '{self._script_path + self._script_name}'" ) 
        else:
            self._memo_output.insert( TK.END, f"{self._script_buffer}" ) 

    def click_button_exec_script( self ):
        logger.info( "Called" )
        self._memo_output.delete( "1.0", "end" )
        try:
            # Redirect stdout to the StringIO object
            exec_output = IO.StringIO()
            old_stdout = SYS.stdout
            SYS.stdout = exec_output
            exec( self._script_buffer )
            # Return to original stout
            SYS.stdout = old_stdout
            self._memo_output.insert( TK.END, exec_output.getvalue() )
        except Exception as e:
            logger.error( e )
            self._memo_output.delete( "1.0", "end" )
            self._memo_output.insert( TK.END, str( e ) )
 
    def click_button_show_script( self ):
        logger.info( "Called" )
        logger.debug( f"{self._script_name} shown" )
        self._memo_output.delete( "1.0", "end" )
        self._memo_output.insert( TK.END, self._script_buffer )

    def click_button_exec_command( self ):
        logger.info( "Called" )
        output = ""
        self._memo_output.delete( "1.0", "end" )
        command = self._entry_command.get().strip()
        output = self._interpreter.process_command( command )
        self._memo_output.insert( TK.END, output)

    def click_button_save_output( self ):
        # REPLACE W UTILITY FUNCTION
        logger.info( "Called" )
        memo_content = self._memo_output.get("1.0", TK.END).strip()
        filename = self._entry_save_filename.get()

        logger.debug( f"Attempting to write {len(memo_content)} bytes to '{filename}'" )
        if memo_content and filename:
            with open( filename, "w") as file:
                file.write( memo_content )
            self._memo_output.delete( "1.0", "end" )
            self._memo_output.insert( TK.END, "Output from script saved successfully!" )
        else:
            self._memo_output.delete( "1.0", "end" )
            self._memo_output.insert( TK.END, "There is no output to save." )

    def click_button_show_log( self ):
        logger.info( "Called" )
        # pull from globals eventually; hardcoded for now
        path_and_file = 'C:\\Users\\17082\\Documents\\github-repos\\montague\\montague.log'
        # redirect output to child window eventually
        # return success_flag and add 
        output = U.read_file_to_text( path_and_file )
        self._memo_output.delete( "1.0", "end" )
        self._memo_output.insert( TK.END, output ) 

    def click_button_clear_memo( self ):
        logger.info( "Called" )
        #self._memo_output.clipboard_get
        self._memo_output.delete( "1.0", "end" )

    """
    def __post_init__( self ):
        logger.debug( "Called" )
        self._entry_text_selection.set( "This is a test." )
    """
