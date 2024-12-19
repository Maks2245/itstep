# my_list = [1, 2, 3]
#
# iterator = iter(my_list)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
from pkg_resources import working_set


# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise  StopIteration
#         return self.i
#
# count = Counter(5)
#
# for elem in count:
#     print(elem)
#
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(iter(count))
# print(next(count))


# def raise_to(number, max_degree):
#     i = 0
#     for _ in range(number):
#         yield number**i
#         i += 1
#
# res = raise_to(123456, 10)
# print(res)
# for _ in res:
#     print(_)

#
# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"1 - {self.work}, 2 - {work}"
#
# helper = Helper("Homework")
# print(helper("cleaning"))

#
# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"1 - {work}, 2 - {work_in_memory}"
#     return helper
# helper = helper("Homework")
#
# print(helper("cleaning"))

#
# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as exc:
#             print(exc)
#         else:
#             print(f"No problem - {result}")
#     return checker
#
# def calculate(expression):
#     return eval(expression)
#
# @checker
# def calculate(expression):
#     return eval(expression)
# calculate("2 + 3")




class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        while self.i < self.max_number:
            if self.i % 2 == 0:
                a = self.i
            return self.i
        raise  StopIteration


count = Counter(10)

for elem in count:
    print(elem)
#
# print(count.__next__())