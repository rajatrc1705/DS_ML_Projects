# Youtube Video Classification 📽[WIP]

## Dataset 💾

I could have used a ready made API, but just for the fun of it, I scraped the data from [Youtube](https://www.youtube.com/) using <b>Selenium</b>. The total number of videos scraped was <b>3600</b>. 
I scraped the following things from each video:
 - Link
 - Title
 - Description

I queried the videos for 4 categories:<br>

 - Travel Vlogs
 - Food
 - Art and Music
 - History

## Data Cleaning 🧹

 1. Converting to lower case, and removed all punctuations and numeric data
 2. Removed extra spaces and tokenized the data
 3. Added common words like "subscribe", "instagram", "facebook", "contact" to the <b>stopwords</b> set, and removed all the stop words.
 4. Removing words containing "http", "gmail", "email" and the like
 5. Lemmatization using <b>Porter Scanner</b>

## Data Preprocessing 

