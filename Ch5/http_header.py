

import urllib

url = raw_input("Enter the URL (http://www.example.com/) ")
page = urllib.urlopen(url)

if page.code == 200:
    print page.headers

