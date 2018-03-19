import re
pattern = r"[\w.-]+@[\w.-]+"
string = " feedback at arushiyadav551@gmail.com"
match = re.search(pattern,string)
if match:
    print("email to:",match.group())
else:
    print("no match")