import re
result = re.findall(r".","good morning")
print(result)
result1 = re.findall(r"^\w+","good evening")
print(result1)
res2 = re.findall(r"\w\w","good night")
print(res2)
res3 = re.findall(r"\b\w\w","helllo once again")
print(res3)
res4 = re.findall(r"\w+$","hi everyone")
print(res4)
res5 = re.findall(r"\d{2}-\d{2}-\d{4}","today is 20-03-2018")
print(res5)
res6 = re.findall(r"\d{4}","today is 20-03-2018")
print(res6)
res7 = re.findall(r"\b[aeiouAEIOU]\w+","today iam going to take my umbrella along with me")
print(res7)
res8 = re.findall(r"[789{1]\d{9}","7421241321 8375043182 24545241524 dt54541214 these are my no.s")
print(res8)
res9 = re.sub(r"[;,-]"," ","hello! my name-arushi.; my date of birth is 23-08-1997")
print(res9)
def pluralize(n):
    if re.search(r"[sxz]$",n):
        return re.sub("$","es",n)
    elif re.search(r"[^aeioudgkprt]h$",n):
        return re.sub("$","es",n)
    elif re.search(r"[^aeiou]y$",n):
        return re.sub("y$","ies",n)
    else:
        return re.sub("$","s",n)
list = ["toy","fox","cat","brush"]
for i in list:
    print(i,"-",pluralize(i))
