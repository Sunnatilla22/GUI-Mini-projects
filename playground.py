def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(3,5,6,7))

#
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["mulpulty"]
#     print(n)
#
#
# calculate(2, add=3, mulpulty=5)
#
# class Car:
#     def __init__(self, **kw):
#         # self.make = kw["make"]
#         # self.model = kw["model"]
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#         self.seats = kw.get("seats")
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.seats)

