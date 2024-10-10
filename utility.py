import logging as LOG
log = LOG.getLogger( __name__ )

# ----------------------------------------------------------------
# WRITE_TEXT_TO_FILE
# ----------------------------------------------------------------

"""
EXAMPLE
    cur_dir = os.getcwd()
    print( f"{cur_dir=}" )
    text = "empty"
    text2 = "We all live on a yellow submarine.\n"
    tmp_filename = "test.txt"
    path_and_file = filename = cur_dir + "\\" + tmp_filename
    utility.write_text_to_file( text2, path_and_file )
"""

def write_text_to_file( text: str = "", path_and_filename: str = "" ):
    log.debug( f"'{text[:5]=}'... {path_and_filename=}" )
    #print( f"'{text[:5]=}'... {path_and_filename=}" )

    try:
        with open( path_and_filename, "w" ) as file:
            file.write( text )
    except:
        log.error( f"Failed to write {path_and_filename}" )

# ----------------------------------------------------------------
# READ_FILE_TO_TEXT
# ----------------------------------------------------------------

"""
EXAMPLE
    cur_dir = os.getcwd()
    print( f"{cur_dir=}" )
    text = "empty"
    text2 = "We all live on a yellow submarine.\n"
    tmp_filename = "test.txt"
    path_and_file = filename = cur_dir + "\\" + tmp_filename
    text = U.read_file_to_text( path_and_file )
    print( text )
"""

"""
from typing import Tuple
def get_coordinates() -> Tuple[float, float]:
    return 1.0, 2.0
"""

def read_file_to_text( path_and_filename: str ) -> str:
    log.debug( f"{path_and_filename=}" )
    #print( f"{path_and_filename=}" )
    success_flag = True
    return_string = ""
    try:
        with open( path_and_filename ) as file:
            return_string = file.read()
    except Exception as e:
        log.error( e )
        success_flag = False
        return_string = str( e )
    return success_flag, return_string

# ----------------------------------------------------------------
# GET_SUBSTRING
# ----------------------------------------------------------------
"""
Takes a string as a starting delimitter and ending delimitter and returns the substring between

EXAMPLE:

    import utility as U

    test_string = "'This is a test of the EBS' is a useful string."
    print( U.get_substring( test_string, "'", "'") + "." )
"""
def get_substring( tmp_str, start_delim, end_delim ) -> str:
    substr_start = tmp_str.find( start_delim  ) + len( start_delim ) # start and end delimitters can be arbitrary long substringthemselves
    substr_end = tmp_str.find( end_delim, substr_start)
    return tmp_str[ substr_start : substr_end ]

# ----------------------------------------------------------------
# LAMBDAS
# ----------------------------------------------------------------

# punctuation
squote = lambda s: f"'{s}'"
dquote = lambda s: f'"{s}"'
bracket = lambda s: f"[{s}]"
brace = lambda s: f"[{s}]"
backtick = lambda s: f"`{s}`"
sandwich_with = lambda s, delim: f"{delim}{s}{delim}"

# whitespace
add_nl = lambda s: f"{s}\n"
drop_nl = lambda s: f"{s[0:len(s)-1]}" if s[len(s)-1] == "\n" else s

# natural language
stop = lambda s: f"{s}."
bang = lambda s: f"{s}!"
huh = lambda s: f"{s}?"
thus = lambda s: f"{s};"
drop = lambda s: f"{s[0:len(s)-1]}"

# case and sentence punctuation
capitalize = lambda s: f"{s[0].upper()}{s[1:len(s)]}"
cap_and_stop = lambda s: f"{s[0].upper()}{s[1:len(s)]}."
cap_and_bang = lambda s: f"{s[0].upper()}{s[1:len(s)]}!"
cap_and_huh = lambda s: f"{s[0].upper()}{s[1:len(s)]}?"
cap_and_thus = lambda s: f"{s[0].upper()}{s[1:len(s)]};"
uncap_and_drop = lambda s: f"{s[0].lower()}{s[1:len(s)-1]}"
