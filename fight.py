"""
создать класс плейер с атрибутами кол-во жизней
и методы которые наносят урон другому плейеру и отнимает жизнь
"""

class Player:
    def __init__(self, name_pm, lives_pm):
        self.name = name_pm
        self.lives = lives_pm

    def damage(self, whom, how_mach):
        whom.lives = whom.lives - how_mach


p1 = Player('Artur', 150)
p2 = Player('Aldos',150)
p1.damage(p2, 100)
p2.damage(p1, 73)
print(p2.lives)
print(p1.lives)