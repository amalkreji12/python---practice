class pets:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class cat(pets):
    def speak(self):
        print("Meow")

class dog(pets):
    def speak(self):
        print("Bark")


p=pets("Tim",19)
p.show()
c=cat("Jill",20)
c.show()
c.speak()
d=dog("Sim",21)
d.show()
d.speak()

