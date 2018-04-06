from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0
s = 0
l = soup('span')
for no in l:
    print(no.text)
    count=count+1
print("\n total numbers",count)
for i in l:
    j = int(i.text)
    s = s + j
print("\n sum is :",s) 
