class Student:
    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        self.age = age_pm

    def say_here(self):
        print(f'Я {self.name} здесь')


nur = Student('Нуржигит', 20)
nur.say_here()



