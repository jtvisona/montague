
# Sentimental Analysis
import pandas as pd

df = pd.read_csv( "./data/training.1600000.processed.noemoticon.csv", encoding='iso-8859-1' )
df.head()
df.info()
df.describe()