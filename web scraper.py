import bs4 as bs
import pandas as pd
# import numpy as np
# import selenium as sel
import requests as req

from requests import get
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_animated_films"

results = req.get(url)

soup = BeautifulSoup(results.text, "html.parser")

#table=soup.find_all('table')[1]
table=soup.find('table', class_='wikitable sortable plainrowheaders')

movie_titles=table.find_all('th')

movie_title_table = [title.text.strip() for title in movie_titles][:4] #index 5 is the references, which we don't want to include. otherwise we don't need the movie titles just yet


dataframe=pd.DataFrame(columns = movie_title_table)


column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data=row.find_all('td')
    row_title=row.find('th').text.strip() #this is needed since the titles are under a different html tag
    individual_row_data = [data.text.strip() for data in row_data][:3] #disinclude the references column
    individual_row_data.insert(1,row_title)
    
    length = len(dataframe)
    dataframe.loc[length] = individual_row_data

#print(dataframe)

dataframe.to_csv(r'D:\GitHub\web scraper\animated_movies.csv', index=False)