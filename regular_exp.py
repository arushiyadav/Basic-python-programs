import re 
s = """My name is Arushi.
     Arushi studied In IPEC"""
p = "$My"#$=end and ^=start
if re.match(p,s):
    print("My is found in string.")
else:
    print("not found")
p1 = "NAME"
if re.search(p1,s,re.I):
    print("name found in string")
else:
    print("not found")
if re.search("Ar.",s):
    print("found")
else:
    print("not found")
s1 = "She sells sea shells on the sea shores"
p2 = "sea"
repl = "ocean"
s2 = re.sub(p2,repl,s1,1)
print(s2)
pattern = r"[a-zA-Z]+ \d+" #pattern begin with one or more characters followed by space and then followed by one or more digits
string = "LXI 2013, VXI 2015, VDI 2018, Maruti Suzuki Cars available with us "
matches = re.findall(pattern,string)
for match in matches:
    print(match, end = " ") 
founds = re.finditer(pattern, string)
for found in founds:
    print("\nmatch found at starting index:", found.start())
    print("match found at ending index:", found.end())
    print("match found at starting and ending index:", found.span())
if re.search(r"\t"," 123\tabc"):
    print("found")
else:
    print("not found")
if re.search(r"2{1,4}$","112222"):
    print("found")
p2 = r"go(od)go(in)g"
t = re.search(p2,"goodgoinggoodgoing")
if t:
    print(t.group())
    print(t.group(1))
    print(t.group(2))
    print(t.groups())