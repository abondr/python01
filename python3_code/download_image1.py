import urllib.request

local_path = "local-filename.jpg"
url1 = "https://m.media-amazon.com/images/M/MV5BMjIyMDJkNzYtOTlhYy00ZGQzLWI0MjctMjA3MGFmZTc0ZmQ5XkEyXkFqcGdeQXVyMTk3NDI2Njc@._V1_QL50_SY1000_CR0,0,677,1000_AL_.jpg"
urllib.request.urlretrieve(url1, local_path)
