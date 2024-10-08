"""
Montague is an object-manipulation framework designed to support encoding arbitary formal systems.
It is named after Richard Montague, who along with Barbara Partee and others, advanced linguisitc formal semantics.

by Jonathan Visona 
jtvisona can be emailed at yahoo com
"""

#https://docs.python.org/3/library/logging.html

import montague as MGUE
import object_man as OM
import tkinter as TK
import logging
logger = logging.getLogger( __name__ )

def main():

    logging.basicConfig( filename='montague.log', level=logging.DEBUG, filemode="w", encoding="utf-8",
                        format="%(asctime)s:%(levelname)s:%(module)s - %(message)s" )
    logger.info( 'main()' )
    logger.info( 'Montague starting' )
    
    logger.info( 'Creating and initializing tkinter root' )
    app_root = TK.Tk()
    app_root.title( "Montague Tool for Sentiment Analysis" )
    app_root.geometry( "825x525" )

    logger.info( "Creating object manager" )
    obj_man = OM.ObjectManager()

    logger.info( "Creating Montague application and assigning object manager" )
    mgue = MGUE.Application( app_root, obj_man )

    logger.info( "Invoking the Montague mainloop" )
    app_root.mainloop()
    logger.info( 'Montague exiting' )

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
