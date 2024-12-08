class Dad:
    def dad(self):
        print("Від Тата:")
        self.name = "Володя"
        self.height = 185
        print(f" Зріст - {self.height} см")
        self.weight = 90
        self.iq = 120
        print(f" IQ - {self.iq}")
        self.job = "Doctor"

class Mum:
    def mum(self):
        print("Від Мами:")
        self.name = "Оля"
        print(f" Ім'я - {self.name}")
        self.height = 170
        self.weight = 70
        print(f" Вага - {self.weight} кг")
        self.iq = 110
        self.job = "Programmer"
        print(f" Робота - {self.job}")

class Daughter(Dad, Mum):
    pass

daughter = Daughter()

daughter.dad()
daughter.mum()
