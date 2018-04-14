import urllib.request,urllib.parse,urllib.error
import json
url = 'http://py4e-data.dr-chuck.net/comments_80968.json'
print('retrieving',url)
uh = urllib.request.urlopen(url).read()
info = json.loads(uh)
data = info['comments']
s = 0
counts = 0
for i in data:
    print(i['count'])
for j in data:
    s = s + int((j['count']))
    counts += 1
print("COUNT",counts)
print("sum is",s)
