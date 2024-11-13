class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound."

    def describe(self):
        return f"{self.name} is {self.age} years old."


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

    def describe(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old."


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  
        self.color = color

    def speak(self):
        return f"{self.name} meows."

    def describe(self):
        return f"{self.name} is a {self.color} cat and is {self.age} years old."


class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age) 
        self.species = species

    def speak(self):
        return f"{self.name} chirps."

    def describe(self):
        return f"{self.name} is a {self.species} bird and is {self.age} years old."


dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Gray")
bird = Bird("Tweety", 1, "Canary")


print(dog.describe())
print(dog.speak())
print()

print(cat.describe())
print(cat.speak())
print()

print(bird.describe())
print(bird.speak())
