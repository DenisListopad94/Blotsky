class Ver:
    def __init__(self, a=15, b=30):
        self.a = a
        self.b = b

    def vivod1(self) -> None:
        print(self.a, self.b)

    def vivod2(self, new_a=1, new_b=2):
        self.a = new_a
        self.b = new_b

    def vivod3(self):
        summ = self.a + self.b
        return summ

    def vivod_max(self):
        return max(self.a, self.b)


show1 = Ver()

show1.vivod1()

show1.vivod2(1, 2)
print("\nNew: ", end='')
show1.vivod1()

print("\nView summ:", show1.vivod3())
print("\nView summ:", show1.vivod_max())
