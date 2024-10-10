
# Sentimental Analysis
import pandas as pd
file = "./data/training.1600000.processed.noemoticon.csv"
try:
    print( f"Attempting to load '{file}' into DataFrame" )
    df = pd.read_csv( file, encoding='iso-8859-1' )
    df.head()
    df.info()
    df.describe()
except Exception as e:
    print( str( e ) )
