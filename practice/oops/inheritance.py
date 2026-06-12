class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self, name, breed):  # child constructor using super()
        super().__init(name)
        self.breed = breed

    def bark(self):
        print("WOOF!")

    def eat(self):  # method overriding
        super().eat()  # call eat() of parent class
        print("Dog is eating")

class Cat(Animal):

    def speak(self):
        print("Meow!")


a = Animal("Lion")
d = Dog("Dog", "Labrador")
c = Cat("Cat")


print(a.name)
print(d.name, d.breed)
print(c.name)

a.eat()
d.eat()
c.eat()

# a.bark() -> cannot be accessed
d.bark()

# a.speak() -> cannot be accessed
c.speak()