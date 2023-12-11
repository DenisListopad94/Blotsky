import random


class City:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Transport:
    def __init__(self, name, cost_per_weight, speed):
        self.name = name
        self.cost_per_weight = cost_per_weight
        self.speed = speed


class Order:
    def __init__(self, weight, city_from, city_to, preferences):
        self.weight = weight
        self.city_from = city_from
        self.city_to = city_to
        self.preferences = preferences


class TransportAgency:
    def __init__(self, cities, transports):
        self.cities = cities
        self.transports = transports
        self.orders = []
        self.income = {city.name: {transport.name: 0 for transport in transports} for city in cities}
        self.delivery_times = {city.name: {transport.name: [] for transport in transports} for city in cities}

    def generate_order(self):
        weight = random.randint(1, 100)
        city_from = random.choice(self.cities)
        city_to = random.choice(self.cities)
        preferences = {"speed": random.uniform(0, 1), "cost": random.uniform(0, 1)}
        order = Order(weight, city_from, city_to, preferences)
        self.orders.append(order)

    def calculate_income(self, order, transport):
        cost = order.weight * transport.cost_per_weight
        self.income[order.city_from.name][transport.name] += cost
        return cost

    def deliver_order(self, order, transport):
        time = order.weight / transport.speed
        self.delivery_times[order.city_from.name][transport.name].append(time)

    def process_orders(self):
        for order in self.orders:
            possible_transports = [transport for transport in self.transports if
                                   order.city_from.size in ["large", "medium"] or
                                   order.city_to.size in ["large", "medium"] or
                                   transport.name == "truck"]
            selected_transport = min(possible_transports,
                                     key=lambda x: x.cost_per_weight * order.weight + (
                                         1 - order.preferences["speed"]) * x.speed)
            cost = self.calculate_income(order, selected_transport)
            self.deliver_order(order, selected_transport)


cities = [City("CityA", "large"), City("CityB", "medium"), City("CityC", "small")]
transports = [Transport("Truck", 10, 50), Transport("Train", 5, 30), Transport("Airplane", 20, 100)]

agency = TransportAgency(cities, transports)

for _ in range(10):
    agency.generate_order()

agency.process_orders()

print("Income:")
print(agency.income)

print("\nDelivery Times:")
print(agency.delivery_times)
