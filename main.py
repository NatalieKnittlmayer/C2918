class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def sound(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} is fetching.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")
        self.name = name

    def sound(self):
        print("Meow!")

    def scratch(self):
        print(f"{self.name} is scratching.")


class Bird(Animal):
    def __init__(self, name):
        super().__init__("Bird")
        self.name = name

    def sound(self):
        print("Chirp!")

    def fly(self):
        print(f"{self.name} is flying.")

dog = Dog("Buddy")
dog.sound()  # Виведе "Woof!"
dog.fetch()  # Виведе "Buddy is fetching."

cat = Cat("Whiskers")
cat.sound()  # Виведе "Meow!"
cat.scratch()  # Виведе "Whiskers is scratching."

bird = Bird("Polly")
bird.sound()  # Виведе "Chirp!"
bird.fly()  # Виведе "Polly is flying."