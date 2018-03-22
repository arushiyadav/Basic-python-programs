class csstudent():
    stream = "cse"
    def __init__(self,rollno):
        self.rollno = rollno
    def setaddr(self,addr):
            self.addr = addr
    def getaddr(self):
        return self.addr
a = csstudent(101)
b = csstudent(102)
a.setaddr("delhi")
b.setaddr("noida")
print(a.stream)
print(a.rollno)
print(a.getaddr())
print(csstudent.stream)
print(b.rollno)
print(b.getaddr())

        