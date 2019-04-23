from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
url1 = "https://www.fundoodata.com/advance_search_results.php?&company_type_id[]=2&company_type_id[]=5&company_type_id[]=3&company_type_id[]=4&company_type_id[]=1&company_type_id[]=6&level_id=1&search_type=1"
raw_html = simple_get(url1)
html = BeautifulSoup(raw_html, 'html.parser')

for div in html.select('.search-result-left'):
    heading = div.select(".heading a")
    print("--------------------")
    print(heading)
    print("--------------------")