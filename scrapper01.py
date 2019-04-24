import urllib
from bs4 import BeautifulSoup
import scrappyLib01

for pageNo in range(1, 2):
    urlParams = {'company_type_id[]': [1, 2, 3, 4, 5, 6], 'level_id': 1, 'tot_rows': 100000,
                 'pageno': pageNo, 'search_type': 1, 'no_of_offices': 0, 'total_results': 101132}
    params = urllib.parse.urlencode(urlParams, True)
    url1 = "https://www.fundoodata.com/advance_search_results.php?&" + params
    raw_html = scrappyLib01.simple_get(url1)
    html = BeautifulSoup(raw_html, 'html.parser')
    for aHref in html.select('.search-result-left .heading'):
        print("--------------------")
        for curLink in aHref:
            links = BeautifulSoup(curLink, 'html.parser')
            for a in links.find_all('a', href=True):
                print(a['href'])
        print("--------------------")
