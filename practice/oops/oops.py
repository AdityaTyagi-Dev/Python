class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def speak(self):
        print(f"{self.__name} speaks")
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def __str__(self):
        return f"{self.__name} ({self.__age})"
    
class Dog(Animal):
    def speak(self):
        print(f"{self.get_name()} barks")

a1 = Animal("Buddy", 5)
d1 = Dog("Tommy", 3)

print(a1)
print(d1)

a1.speak()
d1.speak()

print(a1.get_age())
print(d1.get_age())

# print(a1.__age) -> this will give an error