class Instrument:
    def __init__(self, name_pm: str, price_pm: int):
        self.name = name_pm
        self.price = price_pm

class Guitar(Instrument):
    def __init__(self):

    def play(self):
        print('Играется гитара')

g1 = Instrument('Сакура', 20000)
