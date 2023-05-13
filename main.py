# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
#
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passenger = []
#
#     def add_passenger(self, human):
#         self.passenger.append(human)
#
#     def print_passengers_name(self):
#         if self.passenger != []:
#             print(f"Names of {self.brand} passengers: ")
#             for passenger in self.passenger:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
#
# vasya = Human("Vasya")
# sofi = Human("Sofi")
#
# car = Auto("Mercedes")
#
# car.add_passenger(vasya)
# car.add_passenger(sofi)
# car.print_passengers_name()
#
#
#
# _______________________SIMS_________________________________


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to.repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.selary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return

        if manage == 'fuel':
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print("Yay! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5


    def clean_home(self):
        self.gladness -= 5
        self.home.mess += 0

    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50

    def days_indexes(self,day):
        day = f"Today {day} of {self.name}'s life"
        print(f"{day:^50}","\n")
        human_indexes = self.name + "'s index"
        print(f"{human_indexes:^50}","\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}","\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f" {self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead..")
            return False
        if self.money <+ 500:
            print("Bankrupt...")
            return False

class Auto:
    pass


class House:
    pass


class Job:
    pass
