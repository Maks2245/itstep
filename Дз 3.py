print(f"Ви вчитель, запишіть тих, хто присутні на уроці")
a = input(f"Запишіть тих, хто присутні на уроці: ")

class Students:
    def __init__(self, name = a):
        self.name = name
class Present:
    def __init__(self):
        self.students = []
    def add_student(self, *args):
        for student in args:
            self.students.append(student)
    def print_students_names(self):
        if self.students != []:
            print(f"Присутні на уроці: ")
            for student in self.students:
             print(student.name)
        else:
            print(f"Ніхто не прийшов на ваш урок")


names = Students(a)

present = Present()

present.add_student(names)
present.print_students_names()
