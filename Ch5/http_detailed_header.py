#A little meh, but does the trick


import urllib

url = raw_input("Enter the url whose headers you want to know (http://www.example.com/) ")

page = urllib.urlopen(url)

headers = dir(page.headers)

for x in headers:
    info = 'page.headers.'+x
    resp =  x+': ' + str(eval(info))
    if "<" not in resp:
        print resp
