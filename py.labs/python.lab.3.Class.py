import numpy as np

class Cylinder:
    def __init__(self, height, radius ):
        self.height = height
        self.radius = radius
        
    def get_volume(self):
        return np.pi * np.power(self.radius, 2) * self.height

height = int(input('Введіть висоту циліндру : '))
radius = int(input('Введіть радіус циліндру : '))


cylinder = Cylinder(height, radius)  
print("Об'єм циліндра:", cylinder.get_volume())
