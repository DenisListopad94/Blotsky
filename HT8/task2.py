class Counter:
    def __init__(self, count=4, min_count=2, max_count=200):
        self.count = count
        self.min_count = min_count
        self.max_count = max_count

    def count_starter_from_plus(self):
        if self.count < self.max_count:
            self.count += 1
        else:
            print("counter max")

    def count_starter_from_low(self):
        if self.count > self.min_count:
            self.count -= 1
        else:
            print("counter low")

    @property
    def current_status(self):
        return self.count


starter = Counter()
print("Current number:", starter.current_status)

starter.count_starter_from_plus()
print("Current number:", starter.current_status)

starter.count_starter_from_low()
print("Current number:", starter.current_status)

starter = Counter(5, 2, 10)
print("\nCurrent number after renumber:", starter.current_status)

starter.count_starter_from_plus()
print("Current number after renumber:", starter.current_status)

starter.count_starter_from_low()
print("Current number after renumber:", starter.current_status)
