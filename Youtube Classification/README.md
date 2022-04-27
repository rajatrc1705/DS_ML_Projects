# Youtube Video Classification 📽[WIP]

Scraped data from Youtube (~3600 videos) using Selenium. <br>Sanitized the data, tokenized, lemmatized it. <br>Used TfidfVectorizer to extract features from descriptions and built different classifier models. <br>Accuracy metrics used: Log loss, F1 Score. <br>Best model by Log loss is Naive Bayes.

## Dataset 💾

[Kaggle Link For Dataset](https://www.kaggle.com/datasets/rajatrc1705/youtube-videos-dataset)

I could have used a ready made API, but just for the fun of it, I scraped the data from [Youtube](https://www.youtube.com/) using <b>Selenium</b>. The total number of videos scraped was <b>3600</b>. 
I scraped the following things from each video:
 - Link
 - Title
 - Description

I queried the videos for 4 categories:<br>

 - Travel Vlogs 🧳
 - Food 🥑
 - Art and Music 🎨 🎻
 - History 📜

## Data Cleaning 🧹

 1. Converting to lower case, and removed all punctuations and numeric data
 2. Removed extra spaces and tokenized the data
 3. Added common words like "subscribe", "instagram", "facebook", "contact" to the <b>stopwords</b> set, and removed all the stop words.
 4. Removing words containing "http", "gmail", "email" 📧 and the like
 5. Lemmatization using <b>Porter Scanner</b>

## Data Preprocessing and Model Building 👷‍♂️

 - Selected the <b>Descriptions</b> attribute as a feature. 
 - Split the data into 75:25 split ratio. 
 - Fitted <b>TfidfVectorizer</b> to train set and transformed train and test set.
 <br>
 
 Model Building
  
  | Model | Log Loss | F1 Score |
  | --- | --- | --- |
  | Logistic Regression | 0.39040 | 0.91403 |
  | Naive Bayes | 0.36674 | 0.90223 |
  | Bagging Classifier (Decision Tree) | 1.02261 | 0.87389 |
  | Bagging Classifier (SVC) | 2.06138 | 0.91447 |
  
## 📒 To Do :  
  - Train an LSTM model.
  - Productionize with Flask API
  - Put out code for model 
