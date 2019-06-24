from bs4 import BeautifulSoup
import urllib.request
import requests
import re
website = "http://www.imdb.com"
# Download IMDB's Top 250 data
url = website+'/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
for link in links:
    movieSiteResponse = requests.get(website+link)
    soupMovieSite = BeautifulSoup(movieSiteResponse.text, 'lxml')
    linksMovieSite = [a.attrs.get('href')
                      for a in soupMovieSite.select('div.poster a')]
    for galaryLink in linksMovieSite:
        PosterSiteResponse = requests.get(website+galaryLink)
        soupPosterSite = BeautifulSoup(movieSiteResponse.text, 'lxml')
        srcArr = [img.attrs.get('src')
                  for a in soupPosterSite.select('pswp__img')]
        for onlyImage in srcArr:
            print(onlyImage)
