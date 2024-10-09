# %% [markdown]
# ## Sentimental Analysis

# %% [markdown]
# ### EDA

# %%
import pandas as pd

# %%
df = pd.read_csv("/data/training.1600000.processed.noemoticon.csv" ,encoding='iso-8859-1')

# %%
df.head()

# %%
df.info()

# %%
df.describe()

# %%
df.shape

# %% [markdown]
# #### Missing Values

# %%
[feature for feature in df.columns if df[feature].isnull().sum()>=1]

# %% [markdown]
# #### Insights from dataset

# %%
print(df.columns)
df.columns = df.columns.str.strip()

# %%
# different classes of target label
df['polarity of tweet'].value_counts()

# %%
# which columns are not important remove them 
df.head(2)

# %%
# except polarity of tweet and text of the tweet all other are not important column to us for sentimental analysis
df.drop(columns=['id of the tweet' , 'date of the tweet' , 'query' , 'user'],inplace=True)

# %%
df.head(2)

# %% [markdown]
# #### Imbalanced dataset

# %%
df['polarity of tweet'].value_counts()

# %%
# # spliting the data into independent feature and target label
# X = df['text of the tweet']
# Y = df['polarity of tweet']

# %%
# # Implementing Oversampling for Handling Imbalanced 
# from imblearn.combine import SMOTETomek
# smk = SMOTETomek(random_state=42)
# X_res,y_res=smk.fit_resample(X,Y)



# from collections import Counter
# print('Original dataset shape {}'.format(Counter(Y)))
# print('Resampled dataset shape {}'.format(Counter(y_res)))


# %%
# Y_bal.value_counts()

# %%
# we will doing down sampling in this case

# %% [markdown]
# ### 
# 
# Machine Learning Algorithm

# %%
# Supervised Learning -> Neural Network in tensorflow , NLP

# %% [markdown]
# #### Preprocess the text data 

# %%
# !pip install nltk

# %%
df.head(2)

# %%
import nltk

# %%
df['text of the tweet'][1]

# %%
nltk.download('stopwords')

# %%
from nltk.corpus import stopwords
print(stopwords.words('english'))

# %%
removed = []
stopword = stopwords.words('english')
print(len(stopword))
for i in stopword:
    if "n't" in i:
        # print(i)
        removed.append(i)
    if i == "not":
        # print(i)
        removed.append(i)
for i in removed:
    print(i)

# %%
for i in removed:
    stopword.remove(i)

# %%
print(stopword)
print(len(stopword))

# %%
nltk.download('wordnet')

# %%
# jtv - this bang is problematic; wonder why it's here from the export?
# !unzip /usr/share/nltk_data/corpora/wordnet.zip -d /usr/share/nltk_data/corpora/
# added import, but need to 
import unzip
# https://ioflood.com/blog/python-unzip/
#unzip "/usr/share/nltk_data/corpora/wordnet.zip -d /usr/share/nltk_data/corpora/

# %%
df.columns


# %%
import re
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
def preprocess(content):
    # sentence = nltk.sent_tokenize(i)
    sentence = re.sub(r'[^a-zA-Z\']',' ',content)
    sentence = re.sub(r'\s+', ' ', sentence).strip()
    sentence = sentence.lower()
    # sentence = nltk.word_tokenize(sentence)
    sentence = sentence.split()
    sentence = [lemmatizer.lemmatize(word) for word in sentence if not word in stopword]
    sentence = ' '.join(sentence)
    return sentence

# %%
df['preprocess_data'] = df['text of the tweet'].apply(preprocess)

# %%
df.head()

# %%
df['preprocess_data'][0]

# %%
df['text of the tweet'][0]

# %%
X = df['text of the tweet'].values
Y = df['polarity of tweet'].values

# %%
from sklearn.feature_extraction.text import TfidfVectorizer
tfid = TfidfVectorizer()
Xt = tfid.fit_transform(X)

# %%
# # Implementing Oversampling for Handling Imbalanced 
# from imblearn.combine import SMOTETomek
# smk = SMOTETomek(random_state=42)
# X_res,y_res=smk.fit_resample(X,Y)


# %%
# from collections import Counter
# print('Original dataset shape {}'.format(Counter(Y)))
# print('Resampled dataset shape {}'.format(Counter(y_res)))

"""
2024-10-09 The 'sklearn' PyPI package is deprecated, use 'scikit-learn' rather than 'sklearn' for pip commands.
"""

# %%
from sklearn.model_selection import train_test_split
## split train and test data
X_train,X_test,Y_train,Y_test = train_test_split(Xt,Y,test_size=0.2,stratify=Y,random_state=2)

# %%
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=100)
model.fit(X_train, Y_train)

# %%
y_pred = model.predict(X_test)

# %%
#Showing Model Summary
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
print('Classification Report:\n', classification_report(Y_test, y_pred))

# %%
#Visualizing Model Results
t1 = ConfusionMatrixDisplay(confusion_matrix(Y_test, y_pred))
t1.plot()

# %%
content = "@stellargirl I loooooooovvvvvveee my Kindle2. Not that the DX is cool, but the 2 is fantastic in its own right"
preprocessed_content = preprocess(content)
print(preprocessed_content)

# %%
final = tfid.transform([preprocessed_content])
model.predict(final)

# %%



