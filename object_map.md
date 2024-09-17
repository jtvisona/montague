	- [ ] Write routine to automate this
	- [ ] Write routines to build templates
	- [ ] Use basic python logging found at https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
	- [ ] Learn about python virtual environment
	- [ ] Learn about Pydoc

objects_base.py
	@dataclass Object
		__uuid : str
		__type : str
		__name : str
		__delim : str
		
		__init__ ( self, name = "" ):
		@property uuid( self ):
		@uuid.setter uuid( self, uuid ):
		genUuid( self ):
		@property type( self ):
		@property name( self ):
		@name.setter name( self, name ):
		@property delim( self ):
		@delim.setter delim( self, delim ):
		toString( self ):

	ObjectManager
		__objectList : dict

		__init__():
		addObject( self, obj ):
		@property all( self ):

################################################################

objects_function.py


################################################################

objects_logic.py


################################################################

objects_number.py


################################################################

objects_text.py
	@dataclass Proposition( Object ):
    __prop : str
    __lang : str

    __init__ ( self, prop = "", lang = "" ):
    @property prop( self ):
    @prop.setter prop( self, prop ):
    toString( self ):

