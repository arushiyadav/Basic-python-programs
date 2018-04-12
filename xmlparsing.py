import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_80967.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url).read()
tree = ET.fromstring(uh)
results = tree.findall('.//count')
s = 0
count = 0
for i in results:
    print(i.text)
for item in results:
    s = s + int(item.text)
    count += 1
print("count",count)
print("sum is:",s)
          
