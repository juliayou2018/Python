import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("http://www.google.com")
soup = BeautifulSoup(page)
print soup.prettify()
