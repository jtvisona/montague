from dataclasses import dataclass, field
import logging
from objects_base import Object
import object_manager as OM
logger = logging.getLogger( __name__ )

@dataclass
class Interpreter( Object ):

    _history : list = field( default_factory=list )
    _object_manager : object = field( default_factory=object )

    def __init__( self ):
        logger.debug( "Called" )
        self._history = []

    @property
    def history( self ) -> list:
        return self._history

    # Setter for age
    @history.setter
    def history( self, value ):
        if type( value ) == list:
            self._history = value
        else:
            raise ValueError( "Interpreter._history must be list" )

    def process_command( self, command: str ) -> str :
        logger.debug( "Called" )
        logger.info( f"Appending command '{command}' to interpreter history" )
        self._history.append( command )

        output = ""
        logger.info( "Checking for valid command" )
        if command == "test":
            output = "testing complete"
        elif command == "list object":
            #output = str( self._object_manager.object_list() )
            output = "list object"
        elif command == "clear history":
            self.clear_history()
        elif command == "show history":
            output = str( self._history )
        elif command == "help":
            output = 'test - verify that the interpreter is functioning\n' +\
                'clear history - clears the history list\n' +\
                'show history - provides a list of all the commands that have been entered\n' +\
                'help - this menu\n'
        else:
            output = "command unrecognized"
        return output

    def show_history( self ) -> str :
        logger.debug( "Called" )
        history = ""
        for each_entry in self._history:
            history += each_entry + "\n"
        return history

    def clear_history( self ) -> bool :
        logger.debug( "Called" )
        success_flag = True
        try:
            self._history = []
        except:
            logger.exception( "Failed to clear history" )
            success_flag = False
        return success_flag
    
    def link_to_manager( self, object_manager ) -> None :
        logger.debug( "Called" )
        self._object_manager = object_manager
        logger.info( f"Object manager {object_manager.name} linked" )
