import  colorama


def game():
    print("Hello")

a = "hello World"

class Student:
    def __init__(self, name = "Maks"):
        self.name = name


print(type(colorama))
print(colorama.__name__)
print(dir(colorama))
print(f"На мою думку найважливіші методи й атрибути - {dir(colorama)[0]}, {dir(colorama)[7]}, {dir(colorama)[10]}, {dir(colorama)[12]} та {dir(colorama)[19]}")

print(colorama.getmodule(a))
print(colorama.ismodule(a))
print(colorama.isfunction(game))
print(colorama.isclass(Student))
print(colorama.executable)
print(colorama.version)
print(colorama.platform)
print(colorama.args)