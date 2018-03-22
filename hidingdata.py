#private method are accessible outside class just not easily accessible
#nothing in python is truly private
class A():
    __age = 10#double_ var cannot be viewed outside directly
    
    def __init__(self,increment):
        self.increment = increment
    def add(self):
        self.__age+=self.increment
        print(self.__age)#can be viewed
obj = A(2)
obj.add()
print(obj._A__age)#tricky syntax
print(obj.__age)#error cannot be viewed outside class
    