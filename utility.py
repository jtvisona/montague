# ----------------------------------------------------------------
# get_substring
# ----------------------------------------------------------------

"""
Takes a string as a starting delimitter and ending delimitter and returns the substring between
"""

"""
# EXAMPLE
import utility as U

test_string = "'This is a test of the EBS' is a useful string."
print( U.get_substring( test_string, "'", "'") + "." )
"""

def get_substring( tmp_str, start_delim, end_delim ):
    substr_start = tmp_str.find( start_delim  ) + len( start_delim ) # start and end delimitters can be arbitrary long substringthemselves
    substr_end = tmp_str.find( end_delim, substr_start)
    return tmp_str[ substr_start : substr_end ]
