from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('enter')
for i in range(7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count + 1
        if(count==18):
            print(tag.get('href', None))
            url  = str(tag.get('href',None))
            print(tag.contents[0])
            
       

