# class ItalianCar:
#     WEELS = 4  # атрибут класса
#
#
#     def __init__(self, model: str = "fiat", fuel: int = 50, doors: int = 4) -> None:
#         self.model = model # публичный атрибут
#         self._fuel = fuel # защищённым атрибутам
#         self.__doors = doors # приватные атрибут
#
#     def _info_car(self) -> None:  # метод экземпляра класса
#         print(f"model: {self.model} wheels: {self.WEELS} count_doors: {self.__doors} count_fuel: {self._fuel}")
#         return ItalianCar.create_new_obj()
#
#     @staticmethod
#     def get_count_of_luggage(): # статиченский метод
#         print("You have a 10 kilo")
#
#     @classmethod
#     def create_new_obj(cls): # метод класса
#         car = cls()
#         return car
#
#
#     def __del__(self):
#         # print(f"{self}")
#         del self
#
#
#     # def set_count_of_doors(self, doors: int) -> None:
#     #     self.doors = doors  # создание атрибута экземпляра класса
#     #
#     # def set_fuel_value(self, fuel: int) -> None:
#     #     self.fuel = fuel
#     #
#     # def set_model(self, model: str) -> None:
#     #     self.model = model
#
#
# car_1 = ItalianCar(
#     model="ferrari",
#     doors=2
# )  # создание объекта
#
# print(car_1.model)
# print(car_1._fuel)
# print(car_1._ItalianCar__doors)
#
# car_1._info_car()
# car_1.info_car()
#
# car_2 = car_1.info_car()
#
# car_2.info_car()

# парадигмы
# - инкапсуляция(сокрытие данных,)


# car_1.get_count_of_luggage()
# ItalianCar.get_count_wheels()
# car_2 = ItalianCar()
# del car_1
# import time
# time.sleep(4)

# car_1.WEELS = 6
# print(car_1.WEELS)
# ItalianCar.info_car(car_1)

#
# car_2 = ItalianCar() # создание объекта
# print(car_2.WEELS)

# class Human:
#     def __init__(self, name: str = "Oleg", age: int = 30) -> None:
#         self._name = name
#         self._age = age
#
#     def info_human(self):
#         print(f"name: {self._name} age: {self._age}")
#
#
# class YearExpMixin:
#     def start_do_something(self, year_of_do_something):
#         year_start = 2023 - year_of_do_something
#         print(f"start year {year_start}")
#
#
# class Worker(Human, YearExpMixin):
#     def __init__(self, name: str = "Oleg", age: int = 30, year_of_work: int = 2) -> None:
#         super().__init__(
#             name=name,
#             age=age
#         )
#         self.year_of_work = year_of_work
#
#     def info_worker(self):
#         super().info_human()
#         print(f"year_of_work: {self.year_of_work}")
#
#
# class Car:
#     def __init__(self, model):
#         self.model = model
#
#
# class Taxist(Car, Worker):
#     def __init__(self, model: str, name: str = "Oleg", age: int = 30, year_of_work: int = 2):
#         super().__init__(model)
#         Worker.__init__(
#             self=self,
#             name=name,
#             age=age,
#             year_of_work=year_of_work
#         )
#
#
#
# daniel = Taxist(model="pegeout")
# daniel.info_human()

#
# oleg = Human()
# oleg.info_human()

# karl = Worker(
#     name="Karl",
#     age=24,
#     year_of_work=5
# )
# karl.info_human()
# karl.info_worker()
# karl.start_do_something(4)

from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def shoot(self):
        print("some works")


class Gun(Weapon):
    def shoot(self):
        print("bax")


class SublimateGun(Gun):
    def shoot(self):
        print("bax bax bax")


class Knife(Weapon):
    def shoot(self):
        print("vjooox")


class Player:
    def shoot(self, weapon: Weapon):
        weapon.shoot()


# weapon = Weapon()
# print(weapon)

tokarev = Gun()
ak_47 = SublimateGun()
knife = Knife()

player = Player()
player.shoot(tokarev)
