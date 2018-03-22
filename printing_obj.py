class today():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
            return "today is %s-%s-%s" %(self.a,self.b,self.c)
    def __repr__(self):
            return "today day is %s, month is %s and year is %s" %(self.a,self.b,self.c)
obj = today(22,"march",2018)
print(obj)#calling __str__
print([obj])#calling __repr__

