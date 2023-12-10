class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins_count = 0

    def can_add(self, v):
        return self.coins_count + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins_count += v
        else:
            print("Cannot add more coins. Capacity exceeded.")


money_box = MoneyBox(10)

print("Can add 5 coins:", money_box.can_add(5))
print("Can add 7 coins:", money_box.can_add(7))

money_box.add(5)
print("Coins count after adding 5 coins:", money_box.coins_count)

money_box.add(7)
print("Coins count after adding 7 coins:", money_box.coins_count)

money_box.add(3)  #
