# metis-project5-coronavirus
Project 5 (Kojak) Repo

# Objective
**Understanding People’s Sentiment of Coronavirus using Tweets**

# Files
* EDA: 0-eda.ipynb for initial Exploratory Data Analysis of https://github.com/CSSEGISandData/COVID-19
* Data Collection: *1-tweepyScraper.ipynb*
* Data Compression: Extract from Tweet JSON relevant data only to compress file size for original scraped data *2-compressData.ipynb*
* Data Update: If you scrape any new tweets, also compresses this data, and appends tweets *3-updateData.ipynb*
* Data Preprocessing: Clean tweets and also calculates sentiment for each tweet using VADER *4-processData.ipynb*
* Topic Modeling: NMF and LDA on Tweet data, ran multiple times to see which number of topics made most sense *5-topicModel.ipynb*
* Visualizations: Graphs of Sentiment over Time and Coronavirus Cases over Time for various states *6-visualizations.ipynb*
* Code Testing: Testing code before putting in to other files *7-codeTesting.ipynb*
* scrapeOlderTweets.ipynb: Tried various methods of scraping tweets from the past, but various issues with lack of location data / issues with geofencing and tweet download limitation prevented me from moving forward in the limited time I had.
* cities_list: List of cities in each state to put into stop words
