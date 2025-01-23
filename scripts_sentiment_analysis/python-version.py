# %% [markdown]
# # Multi-Model Sentiment Analysis Prototype
# ## Jonathan Visona
# ### CPSC 8985-02 - FA2024

# %% [markdown]
# ### ML References

# %% [markdown]
# #### Jupyter and ML

# %%
# https://www.ibm.com/docs/en/watson-studio-local/1.2.3?topic=notebooks-markdown-jupyter-cheatsheet
# https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research

# %% [markdown]
# #### Python-Centric

# %%
# O'Reilly: Natural Language Processing with Python
    # https://tjzhifei.github.io/resources/NLTK.pdf

# %% [markdown]
# ## Imports

# %%
## 1 ##

"""
visona-sentiment-analysis-prototype.ipynb
Jonathan Visona
CPSC 8985-02 - FA2024
"""

# utility imports
    # https://docs.python.org/3/c-api/index.html

#import string # unused?
from string import punctuation as STR_punctuation
import re as REGEX
import warnings as WARN

# visualization imports
    # https://matplotlib.org/stable/api/index.html
    # https://seaborn.pydata.org/api.html

import matplotlib.pyplot as MPLTLIB_pyplt
#import seaborn as sb # affects some aesthetic defaults of matplotlib without invocation

# math and data science imports
    # https://numpy.org/doc/2.1/reference/index.html
    # https://pandas.pydata.org/docs/reference/index.html

#import numpy as np # included for expansible functionality
import pandas as PNDS

# nltk imports
    # https://www.nltk.org/api/nltk.html

from nltk.tokenize import word_tokenize as NLTK_word_tokenize
from nltk.stem import LancasterStemmer as NLTK_lancaster_stemer
from nltk.corpus import stopwords as NLTK_stopwords
from nltk.stem.wordnet import WordNetLemmatizer as NLTK_wordnet_lemmatizer
from nltk.probability import FreqDist as NLTK_freq_dist

# sci-kit imports
    # https://scikit-learn.org/stable/api/index.html

#from sklearn.metrics import accuracy_score # unused
from sklearn.metrics import accuracy_score as SKLN_accuracy_score
from sklearn.metrics import classification_report as SKLN_classification_report
from sklearn.metrics import ConfusionMatrixDisplay as SKLN_confusion_matrix_display
from sklearn.model_selection import train_test_split as SKLN_train_test_split
from sklearn.linear_model import LogisticRegression as SKLN_logistic_regression
from sklearn.ensemble import RandomForestClassifier as SKLN_random_forest_classifier
from sklearn.feature_extraction.text import TfidfVectorizer as SKLN_tfidf_vectorizer
from sklearn.tree import DecisionTreeClassifier as SKLN_decision_tree_classifier

# %% [markdown]
# ## Global Data

# %%
## 2 ##

# This data is provided by Kaggle at https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset
WARN_OFF = False # Turn off after finished debugging
if( WARN_OFF ):
    WARN.filterwarnings( 'ignore' )

ENCODING = 'latin1'
REL_PATH = '../data/'
TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'
MAX_COLS = 10
MAX_ROWS = 3_000_000
HEAD_SIZE = 25

PNDS.set_option( 'display.max_columns', MAX_COLS )
PNDS.set_option( 'display.max_rows', MAX_ROWS )

# %% [markdown]
# ## Training and Testing Data

# %%
## 3 ##

# Build training and test data from SA Kaggle data
training_data = PNDS.read_csv( REL_PATH + TRAIN_FILE, encoding=ENCODING );
test_data = PNDS.read_csv( REL_PATH + TEST_FILE, encoding=ENCODING );

# %%
## 4 ##

# combine the training and teseting data
dframe = PNDS.concat( [ training_data, test_data ] )

# %%
## 5 ##

# Show the top rows of the data
dframe.head( n=HEAD_SIZE )

# %%
## 6 ##

# Provide general information on current dataset
dframe.info( verbose=True )

# %% [markdown]
# ## Primary Dataframe Construction and Development

# %%
## 7 ##

# Drop irrelevant data from dframe
dframe = dframe.drop( columns=[ 'textID','Time of Tweet', 'Age of User', 'Country', 'Population -2020', 'Land Area (Km²)', 'Density (P/Km²)' ] )

# %%
## 8 ##

# Solve gaps in data by dropping NaNs on current Dataframe with counts pre- and post-process
nan_count_per_column = dframe.isna().sum()
print( nan_count_per_column )

# %%
## 9 ##
 
# Drop NaNs and revist data
dframe.dropna( inplace=True )
nan_count_per_column = dframe.isna().sum()
print(nan_count_per_column)

# %%
## 10 ##

# peek at current cols
column_list = dframe.columns.tolist()
print( column_list ); print()
dframe.info( verbose=True )


# %% [markdown]
# # Data Conditioning

# %% [markdown]
# ### Regex

# %%
## 11 ##

# https://docs.python.org/3/library/re.html
# clean up text to deal with links, non-alphanumerics, URLs, whitespace, etc.
def alphanumericize( txt: str ) -> str:
    txt = str( txt )
    try: 
        pattern_replacement_pairs = {
            r'<.*?>': '', # SGML-style tags
            r'https?://\S+|www\.\S+': '', # URLs with http/https
            r'\n': '', # end of lines
            r'[%s]' % REGEX.escape( STR_punctuation ): '', 
            r'\s+': ' ', # reduce white-space
            r'[^a-zA-Z0-9\s]': '', # non alphanumerics
            r'\w*\d\w*': '' # lone digits
        }
        for pattern, replacement in pattern_replacement_pairs.items():
            txt = REGEX.sub( pattern, replacement, txt.lower().strip() )
            print( f"{type(txt)=} {txt=}" )
        return txt
    except Exception as e:
        print( f"Error alphanumericizing: {e}" )
        return ""
    return 
dframe[ 'alphanumeric' ] = dframe[ 'text' ].apply( alphanumericize )

# %% [markdown]
# ### Tokenization

# %%
## 12 ##

# tokenize the sentences so they can be processed further in the application
def tokenize( txt:str ) -> list:
    try:
        return NLTK_word_tokenize( str( txt ) )
    except Exception as e:
        print( f"Error tokenizing: {e}" )
        return ""
dframe[ 'tokens' ] = dframe[ 'alphanumeric' ].apply( tokenize )

# Take a look at the results of tokenization
#NB currently contains , '*', fragment of URL, breaks up contractions (I've, I'd, couldn't, etc.), shows NaNs
print( dframe[ 'tokens' ] )

# %% [markdown]
# ### Stopword Removal

# %%
## 13 ##

# https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
# https://en.wikipedia.org/wiki/Stop_word
# Remove stopwords using a comprehension by checking the nltk corpus for stopwords
def remove_stopwords( txt: str ) -> str:
    txt = str( txt )
    try:
        words = txt.split()      
        filtered_words = [ word for word in words if word.lower() not in NLTK_stopwords.words( 'english' ) ]
        filtered_text = ' '.join( filtered_words )
    except Exception as e:
        print( f"Error removing stopwords: {e}" )
        return ""
    return filtered_text
dframe[ 'no_stopwords' ] = dframe[ 'tokens' ].apply( remove_stopwords )

# %% [markdown]
# ### Lancaster Stemming

# %%
## 14 ##

# https://www.nltk.org/api/nltk.stem.lancaster.html
# https://en.wikipedia.org/wiki/Stemming
# use Lancaster stemmer
stuff_to_be_removed = list( NLTK_stopwords.words( 'english' ) ) + list( STR_punctuation )
stemmer = NLTK_lancaster_stemer()
dframe[ 'lancaster' ] = dframe[ 'no_stopwords' ].tolist()
#print( len( text_list ) )
#for each_txt in text_list:
#    print( each_txt )
print( dframe[ 'lancaster' ] )

# %% [markdown]
# ## Data Conditioning Evaluation

# %%
## 15 ##

# provide memory usage of columns
dframe.memory_usage()

# %%
## 16 ##

# Examine the tally of neutral, positive, and negative sentiments
dframe[ 'sentiment' ].value_counts()

# %%
## 17 ## 

# Look at bar chart see counts as well as relative size
dframe[ 'sentiment' ].value_counts().plot( kind='bar' )

# %%
## 18 ##

# Look at a pie graph to get relative size of three polarities
dframe[ 'sentiment' ].value_counts().plot( kind='pie' );

# %%
## 19 ##

# Show word frequency data
word_frq = NLTK_freq_dist( NLTK_word_tokenize( ' '.join(dframe[ 'sentiment' ] ) ) )
MPLTLIB_pyplt.figure( figsize=( 10, 6 ) )
word_frq.plot( 20, cumulative=False )
MPLTLIB_pyplt.title( 'Word Frequency Distribution' )
MPLTLIB_pyplt.xlabel( 'Word')
MPLTLIB_pyplt.ylabel( 'Frequency' )
MPLTLIB_pyplt.show()

# %% [markdown]
# ## Train and Test Split Model

# %%
## 20 ##

# https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split
# https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets
X = dframe[ 'lancaster' ]
Y = dframe[ 'sentiment' ]
X_train, X_test, Y_train, Y_test = SKLN_train_test_split( X, Y, test_size=0.2, random_state=42 )

X2 = dframe[ 'selected_text' ]
Y2 = dframe[ 'sentiment' ]
X2_train, X2_test, Y2_train, Y2_test = SKLN_train_test_split( X2, Y2, test_size=0.2, random_state=42 )

# %%
## 21 ##

# https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
# https://en.wikipedia.org/wiki/Tf%E2%80%93idf
vectorizer = SKLN_tfidf_vectorizer()
X_val_train = vectorizer.fit_transform( X_train )
X_val_test = vectorizer.transform( X_test )

vectorizer = SKLN_tfidf_vectorizer()
X2_val_train = vectorizer.fit_transform( X2_train )
X2_val_test = vectorizer.transform( X2_test )


# %%
## 22 ##

# https://scikit-learn.org/1.5/modules/model_evaluation.html
score_baseline = dframe[ 'sentiment' ].value_counts( normalize=True ).max()
print( f"{score_baseline=}" )


# %% [markdown]
# ## Logistic Regression Model

# %%
## 24 ##

# https://scikit-learn.org/1.5/modules/linear_model.html#logistic-regression
# https://en.wikipedia.org/wiki/Logistic_regression
log_reg = SKLN_logistic_regression( n_jobs=-1 )
log_reg.fit( X_val_train, Y_train )
pred_log_reg = log_reg.predict( X_val_test )
score_log_reg = SKLN_accuracy_score( Y_test, pred_log_reg )

log_reg2 = SKLN_logistic_regression( n_jobs=-1 )
log_reg2.fit( X2_val_train, Y2_train )
pred_log_reg2 = log_reg2.predict( X2_val_test )
score_log_reg2 = SKLN_accuracy_score( Y2_test, pred_log_reg2 )

print( f"{score_log_reg=} {score_log_reg2=}" )


# %% [markdown]
# ### Classification Report

# %%
## 25 ##

# https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report
# https://en.wikipedia.org/wiki/Statistical_classification
# Y test and logistic regression
print( 'LANCASTER' )
print( SKLN_classification_report( Y_test, pred_log_reg ) )
print( 'SELECTED_TEXT' )
print( SKLN_classification_report( Y2_test, pred_log_reg2 ) )

# %% [markdown]
# ### Confusion Matrix Display

# %%
## 26 ##

# https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay
# https://en.wikipedia.org/wiki/Confusion_matrix
# Confusion matrix with logicistic regression

print( 'LANCASTER' )
SKLN_confusion_matrix_display.from_predictions( Y_test, pred_log_reg )
print( 'SELECTED_TEXT' )
SKLN_confusion_matrix_display.from_predictions( Y2_test, pred_log_reg2 )

# %% [markdown]
# ## Decision Tree Classifier Model

# %%
## 27 ##

# https://scikit-learn.org/1.5/modules/tree.html
# https://en.wikipedia.org/wiki/Decision_tree_learning
decsn_tree = SKLN_decision_tree_classifier()
decsn_tree.fit( X_val_train, Y_train )
pred_decsn_tree = decsn_tree.predict( X_val_test )
score_decsn_tree = decsn_tree.score( X_val_test, Y_test )

decsn_tree2 = SKLN_decision_tree_classifier()
decsn_tree2.fit( X2_val_train, Y2_train )
pred_decsn_tree2 = decsn_tree2.predict( X2_val_test )
score_decsn_tree2 = decsn_tree2.score( X2_val_test, Y2_test )

print( 'LANCASTER' )
print( f"{score_decsn_tree=}" )
print( 'SELECTED_TEST' )
print( f"{score_decsn_tree2=}" )

# %% [markdown]
# ### Classification Report

# %%
## 28 ##

# https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report
# https://en.wikipedia.org/wiki/Statistical_classification
# Y test and decision tree
print( 'LANCASTER' )
print( SKLN_classification_report( Y_test, pred_decsn_tree ) )
print( 'SELECTED_TEXT' )
print( SKLN_classification_report( Y2_test, pred_decsn_tree2 ) )

# %% [markdown]
# ### Confusion Matrix Display

# %%
## 29 ##

# https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay
# https://en.wikipedia.org/wiki/Confusion_matrix
# Confusion matrix with logicistic regression
print( "LANCASTER" )
SKLN_confusion_matrix_display.from_predictions( Y_test, pred_decsn_tree )
print( "SELECTED_TEXT" )
SKLN_confusion_matrix_display.from_predictions( Y_test, pred_decsn_tree2 )

# %% [markdown]
# ## Random Forest Classifier Model

# %%
## 30 ##

# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
# https://en.wikipedia.org/wiki/Random_forest
rnd_forst_class = SKLN_random_forest_classifier( random_state=0 )
rnd_forst_class.fit( X_val_train, Y_train )
pred_rnd_forst_class = rnd_forst_class.predict( X_val_test )
score_rnd_forst_class = rnd_forst_class.score( X_val_test, Y_test )

rnd_forst_class2 = SKLN_random_forest_classifier( random_state=0 )
rnd_forst_class2.fit( X2_val_train, Y2_train )
pred_rnd_forst_class2 = rnd_forst_class2.predict( X2_val_test )
score_rnd_forst_class2 = rnd_forst_class2.score( X2_val_test, Y2_test )

print( 'LANCASTER' )
print( f"{score_rnd_forst_class}" )
print( 'SELECTED_TEXT' )
print( f"{score_rnd_forst_class2}" )

# %%
## 31 ##

# https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report
# https://en.wikipedia.org/wiki/Statistical_classification
print( 'LANCASTER' )
print( SKLN_classification_report( Y_test, pred_rnd_forst_class ) )
print( 'SELECTED_TEXT' )
print( SKLN_classification_report( Y2_test, pred_rnd_forst_class2 ) )

# %%
## 32 ##

# https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay
# https://en.wikipedia.org/wiki/Confusion_matrix
# Confusion matrix with random forest class
print( 'LANCASTER' )
SKLN_confusion_matrix_display.from_predictions( Y_test, pred_rnd_forst_class )
print( 'SELECTED_TEXT' )
SKLN_confusion_matrix_display.from_predictions( Y2_test, pred_rnd_forst_class2 )

# %% [markdown]
# ## Cross-Model Evaluation

# %%
## 33 ##

# Compare the scores across various models starting with logistic regression
print( 'LANCASTER EVALUATION\n',
        f'Baseline model = {score_baseline}\n',
        f'Logistic regression = {score_log_reg}\n',
        f'Decision Tree Classification = {score_decsn_tree}\n',
        f'Random Forest Classifier = {score_rnd_forst_class}\n' )

print( 'SELECTED_TEXT EVALUATION\n',
        f'Baseline model = {score_baseline}\n',
        f'Logistic regression = {score_log_reg2}\n',
        f'Decision Tree Classification = {score_decsn_tree2}\n',
        f'Random Forest Classifier = {score_rnd_forst_class2}' )

# %% [markdown]
# ## Test and Validation Set on Models

# %%
## 34 ##


# Testing of New Samples

# utility function
def to_lower( txt: str ) -> str:
    return txt.lower()

def test_items( items: list ):
    dframe = PNDS.DataFrame( {'test': items } )
    dframe[ 'lower' ] = dframe[ 'test' ].apply(to_lower)
    new_x_val_test = vectorizer.transform( dframe[ 'lower' ] )
    return new_x_val_test

print(test_items(["I am happy", "I am here", "I am sad"]))


