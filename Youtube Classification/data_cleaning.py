# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('youtube.csv')

# converting all the text data to lowercase
df['title'] = df['title'].apply(lambda x: x.lower())
df['description'] = df['description'].apply(lambda x: x.lower())

# removing punctuation marks, and numerical digits
cleaned_titles = list()
for title in df['title']:
    temp = ''
    for character in title:
        if character not in '.,|/\-#0123456789:;&%`()\'!@$?[]{}_*-~=':
            temp += character
    cleaned_titles.append(temp)
    
df['cleaned_title'] = cleaned_titles

cleaned_description = list()
for description in df['description']:
    temp = ''
    for character in description:
        if character not in '.,|/\-#0123456789:;&%`()\'!@$?[]{}_*-~=':
            temp += character
    cleaned_description.append(temp)
    
df['description'] = cleaned_description

# removing extra spaces between words
df['cleaned_title'] = df['cleaned_title'].apply(lambda x: " ".join(x.split()))
df['description'] = df['description'].apply(lambda x: " ".join(x.split()))

# now tokenization and removing the stop words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

# adding common words that youtube video descriptions have to the stop words
common_words = ['subscribe', 'subscribed', 'subscribers', 'credits', 'find', 'social', 'media',
                'k', 'notifications', 'notification', 'clicking', 'little', 'bell', 'icon',
                'show', 'more', 'less', 'instagram', 'twitter', 'facebook', 'gmail', 
                'contact', 'channel', 'isnt', 'share', 'email', '``', "''", '""']

for c in common_words:    
    stop_words.add(c)

word_tokens = word_tokenize(df['description'][0])

word_tokenize(df['description'][0])

cleaned_strings = list()
for d in df['description']:
    temp = list()
    for word in word_tokenize(d):
        if (word not in stop_words) and ('http' not in word) and ('gmail' not in word) and ('www' not in word):
            temp.append(word)
    string = " ".join(temp)
    cleaned_strings.append(string)

df['description'] = cleaned_strings


cleaned_strings = list()
for d in df['cleaned_title']:
    temp = list()
    for word in word_tokenize(d):
        if (word not in stop_words) and ('http' not in word) and ('gmail' not in word) and ('www' not in word):
            temp.append(word)
    string = " ".join(temp)
    cleaned_strings.append(string)

df['cleaned_title'] = cleaned_strings



# lemmatization
from nltk.stem import PorterStemmer

porter = PorterStemmer()

df['cleaned_title'] = df['cleaned_title'].apply(lambda x: porter.stem(x))
df['description'] = df['description'].apply(lambda x: porter.stem(x))


cleaned_strings = list()
for d in df['cleaned_title']:
    temp = list()
    for word in d.split():
        temp.append(porter.stem(word))
    string = " ".join(temp)
    cleaned_strings.append(string)

df['cleaned_title'] = cleaned_strings

cleaned_strings = list()
for d in df['description']:
    temp = list()
    for word in d.split():
        temp.append(porter.stem(word))
    string = " ".join(temp)
    cleaned_strings.append(string)

df['description'] = cleaned_strings

# dropping redundant column and storing data in a csv
df.drop('title', axis=1, inplace=True)

df.to_csv('cleaned_data.csv', index=False)