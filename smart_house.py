class SmartHouse:
    def __init__(self, temperature_pm: int, light_pm: bool):
        self.light = light_pm
        self.temperature = temperature_pm

    def increase_temperature(self):
       if self.temperature < 40:
            self.temperature += 1

    def decrease_temperature(self):
        if self.temperature > 5:
            self.temperature -= 1

    def install_temperature(self, how_mach: int):
        self.temperature = how_mach

    def on_light(self):
        self.light = True

    def off_light(self):
        self.light = False


house1 = SmartHouse(25, True)
house1.install_temperature(10)
house1.off_light()
print(house1.temperature)
print(house1.light)
house1.decrease_temperature()
house1.decrease_temperature()
house1.decrease_temperature()
house1.install_temperature(16)
house1.decrease_temperature()
house1.decrease_temperature()
house1.on_light()
house1.decrease_temperature()
print(house1.temperature)
print(house1.light)