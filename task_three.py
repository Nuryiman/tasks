class Employee:
    def __init__(self, exp_pm: int, name_pm: str):
        self.name = name_pm
        self.exp = exp_pm

    def staff(self):
        print(f'Меня зовут {self.name}, и у меня {self.exp} лет стажа работы')

    def promotion(self):
        expp = self.exp + 1
        self.exp = self.exp + 1
        return expp


class Manager(Employee):

    def fire(self):
        print(f'Сотрудник {self.name} был уволен менеджером {self.name}')


e1 = Employee(10, 'Саня')

e1.staff()
e1.promotion()
print(e1.promotion())
e1.promotion()
print(e1.exp)
e1.staff()
m1 = Manager(30, 'Asan')
m1.fire()

"""
создать класс плейер с атрибутами кол-во жизней
и методы которые наносят урон другому плейеру и отнимает жизнь
"""
