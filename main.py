import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.progress = 0.0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness += 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 10

    def to_chill(self):
        print("Rest time")
        self.gladness += 5

    def live(self, day):
        day_str = "Day " + str(day) + " of " + self.name + "'s life."
        print(f"{day_str:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

busya = Dog(name="Busya")

for day in range(365):
    if not busya.alive:
        break
    busya.live(day)