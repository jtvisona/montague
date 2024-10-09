from dataclasses import dataclass, field
import logging
logger = logging.getLogger( __name__ )

@dataclass
class Interpreter:

    _history : list = field( default_factory=list )

    def __init__( self ):
        logger.debug( "Called" )
        self._history = []

    def process_command( self, command: str ) -> str :
        logger.debug( "Called" )
        logger.info( f"Appending '{command}' to history" )
        self._history.append( command )

        output = ""
        logger.info( "Checking for valid command" )
        if command == "test":
            output = "testing complete"
        elif command == "clear history":
            self.clear_history()
        elif command == "show history":
            output = str( self._history )
        elif command == "help":
            output = 'test - verify that the interpreter is functioning\n' +\
                'clear history - clears the history list\n' +\
                'show history - provides a list of all the commands that have been entered' +\
                'help - this menu'
        else:
            output = "command unrecognized"
        return output

    def show_history( self ) -> str :
        logger.debug( "Called" )
        history = str( self._history )
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
