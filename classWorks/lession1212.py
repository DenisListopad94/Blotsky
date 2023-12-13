# class Iterator:
#     def __init__(self, counter):
#         self.counter = counter
# 
#     def __iter__(self):
#         return self
# 
#     def __next__(self):
#         self.counter += 3
# 
#         if self.counter > 30:
#             raise StopIteration
#         return self.counter
# 
# 
# my_iterator = Iterator(0)
# 
# map_iterator = map(lambda x: x ** 2, my_iterator)
# for value in map_iterator:
#     print(value)


def generator_fun():
    animals = ["fox", "rabbit", "cat", "dog"]
    for animal in animals:
        print("before yield...")
        data = yield animal
        print(f"I yield.{animal}..{data}")
    print("end fo loop")

    yield "end generator"


generator = generator_fun()
next(generator)
next(generator)

