# web-scraping-challenge

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

Step 1 - Scraping
I completed my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

I created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of the scraping and analysis tasks. 

I scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. I assigned the text to variables that later referenced.

I visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. I used Pandas to convert the data to a HTML table string.

I then visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.

I saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name and used a Python dictionary to store the data using the keys img_url and title.

I appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

Step 2 - MongoDB and Flask Application

Using MongoDB with Flask templating, I created a new HTML page that displays all of the information that was scraped from the URLs above.


I started by converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that executes all of my scraping code from above and returns one Python dictionary containing all of the scraped data.

Next, I created a route called /scrape that imports my scrape_mars.py script and calls the scrape function. I then stored the return value in Mongo as a Python dictionary.

I created a root route / that queries my Mongo database and passes the mars data into an HTML template to display the data.

Finally, I created a template HTML file called index.html that takes the mars data dictionary and displays all of the data in the appropriate HTML elements.
