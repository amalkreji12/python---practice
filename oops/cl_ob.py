

class dog:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        #print(name)
    

    def bark(self):
        print("Bark")

    def hello(self):
        print("Hello World")

    def add(self,x):
        for i in range(0,x):
            print(i)


d=dog('Hello','10')
print(d.name)
print(d.age)
d1=dog('world','15')
print(d1.name)
print(d1.age)


#d.bark()
#d.hello()
#d.add(5)
