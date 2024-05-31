class Employee:
    def __init__(self, name_pm, age_pm, exp_pm, salary_pm):
        self.name = name_pm
        self.age = age_pm
        self.__salary = salary_pm
        self.exp = exp_pm

    def set_salary(self, salary):
        if salary > 0:
            self.set_salary()

    def get_salary(self):
        return self.__salary


class Manager(Employee):
    def increase(self, employee_salary: Employee, increase_salary: int):
        if increase_salary > 0:
            employee_salary.__salary = increase_salary


person = Employee('Бека', 25, 7, 25000)
m1 = Manager('Айдар', 35, 15, 80000)
person.set_salary(40000)
print(person.get_salary())
person.set_salary(-56000)
print(person.get_salary())
m1.increase(person, 45000)
print(person.get_salary())