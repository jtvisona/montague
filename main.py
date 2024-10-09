"""
Montague is an object-manipulation framework designed to support encoding arbitary formal systems.
It is named after Richard Montague, who along with Barbara Partee and others, advanced linguisitc formal semantics.

by Jonathan Visona 
jtvisona can be emailed at yahoo com
"""

# utility imports
import tkinter as TK
# https://docs.python.org/3/library/logging.html
import logging
logger = logging.getLogger( __name__ )

# montague imports
import montague as MGUE
import object_manager as OM
import objects_interpreters as INT

# ----------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------

def main():

    logging.basicConfig( filename='montague.log', level=logging.DEBUG, filemode="w", encoding="utf-8",
                        format="%(asctime)s:%(levelname)s:%(module)s:%(funcName)s - %(message)s" )
    logger.info( 'Montague starting' )

    logger.info( 'Creating and initializing tkinter root' )
    app_root = TK.Tk()
    app_root.title( "Montague Tool for Sentiment Analysis" )
    app_root.geometry( "825x525" )

    logger.info( "Creating object manager" )
    obj_man = OM.ObjectManager()

    logger.info( "Create interpreter" )
    inter = INT.Interpreter()

    logger.info( "Creating Montague application and assigning object manager" )
    mgue = MGUE.Application( app_root, obj_man, inter )

    logger.info( "Invoking the Montague mainloop" )
    app_root.mainloop()
    logger.info( 'Montague exiting' )

# if this module is called first, call main()
if __name__ == "__main__":
    main()
