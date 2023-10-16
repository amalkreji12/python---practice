class pets:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class cat(pets):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} year old and I am {self.color}")


class dog(pets):
    def speak(self):
        print("Bark")


p=pets("Tim",19)
p.show()
c=cat("Jill",20,"Red")
c.show()
c.speak()
d=dog("Bill",22)
d.show()


