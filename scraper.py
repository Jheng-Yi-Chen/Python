# Scraper Using Python
# Jheng Yi Chen
# 2017/9/6

from bs4 import BeautifulSoup
from urllib.request import urlopen
# import urllib.request
# html = urllib.request.urlopen("https://www.tstartel.com/CWS/newsList.php").read()
# html = urlopen("https://www.tstartel.com/CWS/")
html = urlopen("https://www.tstartel.com/CWS/newsList.php")
tstar = BeautifulSoup(html.read(), "html.parser")
print(tstar)
print(tstar.title)
print(tstar.li)


