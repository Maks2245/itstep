class Dad:
    def __init__(self, name, height, weight, iq, job):
        self.name = name
        self.height = height
        self.weight = weight
        self.iq = iq
        self.job = job

class Mum:
    def __init__(self, name, height, weight, iq, job):
        self.name = name
        self.height = height
        self.weight = weight
        self.iq = iq
        self.job = job

class Daughter(Dad, Mum):
    def __init__(self, name, height, weight, iq, job):
        super().__init__(name, height, weight, iq, job)
        print(self.name, self.height, self.weight, self.iq, self.job)
        self.name = name
        self.height = height
        self.weight = weight
        self.iq = iq
        self.job = job




daughter = Daughter("Оля", 185, 70, 120, "Programmer")
mum = Mum("Оля", 170, 70, 110, "Programmer")
dad = Dad("Володя", 185, 90, 120, "Doctor")





