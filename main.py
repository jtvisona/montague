"""
Montague is an object-manipulation framework designed to support encoding arbitary formal systems.
It is named after Richard Montague, who along with Barbara Partee and others, advanced linguisitc formal semantics.

by Jonathan Visona 
jtvisona can be emailed at yahoo com
"""

# utility imports
#import sys
import tkinter as TK
# https://docs.python.org/3/library/logging.html
import logging as LOG
log = LOG.getLogger( __name__ )

# montague imports
from globals import G_MAIN
import montague as MGUE
import object_manager as OM
import objects_interpreters as INT

# ----------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------

def main():
    # Adjust logging level here
    #logging_level = LOG.DEBUG
    logging_level = LOG.INFO
    LOG.basicConfig( filename='montague.log', level=logging_level, filemode="w", encoding="utf-8",
                        format="%(asctime)s:%(levelname)s:%(module)s:%(funcName)s - %(message)s" )
    log.info( 'Montague starting: logging configured' )

    log.info( 'Creating and initializing tkinter root' )
    app_root = TK.Tk()
    app_root.title( G_MAIN["APP_ROOT_TITLE"] ) 
    app_root.geometry( G_MAIN["APP_ROOT_DIMENSIONS"] )

    log.info( "Creating object manager" )
    obj_man = OM.ObjectManager()

    log.info( "Creating interpreter" )
    inter = INT.Interpreter()

    log.info( "Creating Montague application and assigning object manager and interpreter" )
    mgue = MGUE.Application( app_root, obj_man, inter )

    log.info( "Invoking the Montague mainloop" )
    app_root.mainloop()
    log.info( 'Montague exiting' )

# if this module is called first, call main()
if __name__ == "__main__":
    main()
