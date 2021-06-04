import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

def fetchData(query, category):
    """
    

    Parameters
    ----------
    query : str
        the query words that we want to search videos for
    
    category : str
        the category to which the video belongs to

    Returns
    -------
    None.

    """
    
    # basic link
    link = "https://www.youtube.com/results?search_query="
    
    # making the query words in proper format to append to the basic link
    query_words = query.split(" ")
    query_words = "+".join(query_words)
    query_link = link+query_words
    
    # making the query 
    driver = webdriver.Chrome()
    driver.get(query_link)
    time.sleep(60)
    element = driver.find_elements_by_xpath('//*[@id="video-title"]')
    
    # getting the list of all titles of the youtube videos on the queried page
    list_of_titles = list()
    link = list()
    for e in element:
        
        if e.get_attribute('href') == None:
            continue
        else:
            link.append(e.get_attribute('href'))
            list_of_titles.append(e.text)
    
    # getting the other attributes such as link, description
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    v_category = category
    
    count = 0
    for x in link:
        
        driver.get(x)
        
        # gets us the link id
        v_id = x.strip('https://www.youtube.com/watch?v=')
    
        v_description =  wait.until(EC.presence_of_element_located(
                                     (By.CLASS_NAME, "style-scope ytd-video-secondary-info-renderer"))).text
        df.loc[len(df)] = [v_id, list_of_titles[count], v_description, v_category]
        count += 1
        
        # lets us know the progress of scraping
        if count%20 == 0:
            print(count)

# initialising the dataframe to store all the data
df = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])
    
# travel vlogs
queries = ['america vlog', 'europe vlog', 'indian vlog', 'bali vlog']
for q in queries:
    fetchData(q, 'travel')

# food videos
queries = ['european food', 'indian food', 'american food', 'japanese food']
for q in queries:
    fetchData(q, 'food')

# art and music
queries = ['art painting', 'pop music', 'english songs', 'khan songs']
for q in queries:
    fetchData(q, 'art_music')
    
# history
queries = ['indian history', 'chinese history', 'european history']
for q in queries:
    fetchData(q, 'history')

# storing all the scraped data in a csv file
df.to_csv('youtube_videos.csv', index=False)
