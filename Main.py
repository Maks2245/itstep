print("Добрий день, Владиславе!")

class Cat:
    def __init__(self, name):
        self.name = name
        self.breed = "Британський короткошерстий"
        self.age = 3
        self.time_sleep = 18
        self.play = 3
        self.another_actions = 3
    def Cat_info(self):
        return f"Ім'я котика - {self.name}, Порода котика - {self.breed}, Вік котика - {self.age} роки"
    def Cat_routine(self):
        return f"Час спання - {self.time_sleep} годин, Ігри - {self.play} години, Інші дії котика  - {self.another_actions} години"


name_Cat = input("Назвіть свого котика -")
cat = Cat(name_Cat)
print(cat.Cat_info())
print("Як проводить час котик:")
print(cat.Cat_routine())
