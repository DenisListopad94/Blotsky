class Passenger:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Ticket:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight


class Flight:
    def __init__(self, flight_number, origin, destination, date):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.date = date
        self.reserved_tickets = []

    def reserve_ticket(self, passenger):
        ticket = Ticket(passenger, self)
        self.reserved_tickets.append(ticket)
        return ticket

    def cancel_reservation(self, ticket):
        if ticket in self.reserved_tickets:
            self.reserved_tickets.remove(ticket)
            return True
        else:
            return False

    def show_reserved_tickets(self):
        for ticket in self.reserved_tickets:
            print(f"Flight {self.flight_number}: {ticket.passenger.first_name} {ticket.passenger.last_name}")


class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def create_flight(self, flight_number, origin, destination, date):
        flight = Flight(flight_number, origin, destination, date)
        self.flights.append(flight)
        return flight


airline = Airline("Awesome Airlines")

flight1 = airline.create_flight("AA101", "New York", "Los Angeles", "2023-01-15")
flight2 = airline.create_flight("AA202", "Chicago", "Miami", "2023-02-01")

passenger1 = Passenger("John", "Doe")
passenger2 = Passenger("Jane", "Smith")

ticket1 = flight1.reserve_ticket(passenger1)
ticket2 = flight2.reserve_ticket(passenger2)

print("Reserved Tickets for Flight AA101:")
flight1.show_reserved_tickets()

print("\nReserved Tickets for Flight AA202:")
flight2.show_reserved_tickets()

flight1.cancel_reservation(ticket1)

print("\nUpdated Reserved Tickets for Flight AA101:")
flight1.show_reserved_tickets()
