# !pip install yfinance==0.1.67
# !mamba install bs4==4.10.0 -y
# !pip install nbformat==4.2.0

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#------------------------------------------------
# Question 1: Use yfinance to Extract Stock Data
#------------------------------------------------

# create a Ticker object for Tesla
tesla = yf.Ticker("TSLA")

# extract historical stock information and save it in a dataframe named tesla_data
tesla_data = tesla.history(period="max")

# reset the index of the dataframe
tesla_data.reset_index(inplace=True)

# display the first five rows of the dataframe
print(tesla_data.head())

#----------------------------------------------------------
# Question 2: Use Webscraping to Extract Tesla Revenue Data
#----------------------------------------------------------

# Download webpage and save the HTML content in a variable
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.content

# Parse the HTML data using Beautiful Soup
soup = BeautifulSoup(html_data, 'html.parser')

# Find the table with Tesla Quarterly Revenue
table = soup.find_all("tbody")[1]
rows = table.find_all('tr')
# Extract the data from the table and store it in a Dataframe
data =[]
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)
tesla_revenue = pd.DataFrame(data, columns=['Date', 'Revenue'])
# Remove the first row, which contains the column names
tesla_revenue = tesla_revenue.iloc[1:]
# Display the resulting Dataframe
print(tesla_revenue)


#----------------------------------------------------------
# Question 3: Use yfinance to Extract Stock Data
#----------------------------------------------------------

# Create a ticker object for GameStop with the ticker symbol "GME"
gme = yf.Ticker("GME")

# Use the history method to get historical stock data for GME
gme_data = gme.history(period="max")

# Reset the index of the dataframe
gme_data.reset_index(inplace=True)

#----------------------------------------------------------
# Question 4: Use Webscraping to Extract GME Revenue Data
#----------------------------------------------------------

# Define the URL of the webpage to download
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# Use the requests library to download the webpage
response = requests.get(url)

# Save the response text as a variable named html_data
html_data = response.text

# Find the table with Tesla Quarterly Revenue
table = soup.find_all("tbody")[1]
rows = table.find_all('tr')
# Extract the data from the table and store it in a Dataframe
data =[]
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)
gme_revenue = pd.DataFrame(data, columns=['Date', 'Revenue'])
# Remove the first row, which contains the column names
gme_revenue = gme_revenue.iloc[1:]
# Display the resulting Dataframe
print(gme_revenue)


