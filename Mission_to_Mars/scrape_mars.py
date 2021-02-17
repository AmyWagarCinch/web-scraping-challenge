#Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter...
#use this to complete all of your scraping and analysis tasks.
# Dependencies

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():   
    
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    title, paragraph=titles(browser)
        
    data = {"news_title": title,        
            "news_paragraph": paragraph,         
            "facts": table(),        
            "hemispheres": hemispheres(),        
            "last_modified": dt.datetime.now()    
           }
    browser.quit()
    return data

#creating function for flask

def titles(browser):
    #define URL
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    #parsing HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    quotes = soup.find_all('span', class_='text')
    
    #Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables 
    #that you can reference later.
    
    results = soup.find('div', class_="image_and_description_container").get_text()
    
    #obtain title
    results1 = soup.find_all('div', "content_title")
    title = results1[1].text
    #print(title)
    
    #obtain paragraph
    results1 = soup.find_all('div', "article_teaser_body")
    paragraph = results1[0].text
    #print(paragraph)
    
    return title, paragraph

def table():

    url = 'https://space-facts.com/mars/'
    
    #
    tables = pd.read_html(url)
    #tables[1]
    
    #
    return tables[1].to_html()

def hemispheres():
    
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    ]
    return hemisphere_image_urls
    