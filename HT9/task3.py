from abc import ABC, abstractmethod


class Alive(ABC):
    def __init__(self, age_limit):
        self.age = 0
        self.age_limit = age_limit
        self.alive = True

    @abstractmethod
    def eat(self, food_available):
        pass

    def check_status(self, food_available):
        self.age += 1
        if self.age >= self.age_limit or not food_available:
            self.alive = False


class Fox(Alive):
    def __init__(self):
        super().__init__(age_limit=5)

    def eat(self, food_available):
        if food_available:
            print("Fox is eating a rabbit.")
        else:
            print("Fox is hungry.")


class Rabbit(Alive):
    def __init__(self):
        super().__init__(age_limit=3)

    def eat(self, food_available):
        if food_available:
            print("Rabbit is eating a plant.")
        else:
            print("Rabbit is hungry.")


class Plant(Alive):
    def __init__(self):
        super().__init__(age_limit=10)

    def eat(self, food_available):
        if food_available:
            print("Plant is absorbing sunlight.")
        else:
            print("Plant is wilting.")


fox = Fox()
rabbit = Rabbit()
plant = Plant()

for year in range(1, 12):
    print(f"\nYear {year}:")

    fox.eat(food_available=True)
    fox.check_status(food_available=True)

    rabbit.eat(food_available=True)
    rabbit.check_status(food_available=True)

    plant.eat(food_available=True)
    plant.check_status(food_available=True)
