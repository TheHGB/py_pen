import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter the objetive url (http://example.com/) ")
page = urllib.urlopen(url)
html = page.read()

text = BeautifulSoup(html,"html.parser")

for link in text.find_all('a'):
    print(link.get('href'))
