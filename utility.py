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

squote = lambda s: f"'{s}'"
dquote = lambda s: f'"{s}"'
bracket = lambda s: f"[{s}]"
brace = lambda s: f"[{s}]"
backtick = lambda s: f"`{s}`"
stop = lambda s: f"{s}."
sandwich_with = lambda s, delim: f"{delim}{s}{delim}"
capitalize = lambda s: f"{s[0].upper()}{s[1:len(s)]}"
cap_and_stop = lambda s: f"{s[0].upper()}{s[1:len(s)]}."
cap_and_bang = lambda s: f"{s[0].upper()}{s[1:len(s)]}!"
cap_and_huh = lambda s: f"{s[0].upper()}{s[1:len(s)]}?"
cap_and_also = lambda s: f"{s[0].upper()}{s[1:len(s)]};"
uncap_and_drop = lambda s: f"{s[0].lower()}{s[1:len(s)-1]}"