from punto import Punto
from math import pi
class Figura:
    def __init__(self, punto1,punto2):
        self.origen=punto1
        self.fin=punto2
        self.area=0
        self.perimetro=0

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def informar_propiedades(self):
        print("tipo figura ", str(type(self)).split(".")[1][:-2])
        print("el area es ",self.area)
        print("el perimetro es ", self.perimetro)

class Cuadrado(Figura):
    def calcular_area(self):
        lado =self.origen.calcular_distancia(self.fin)
        self.area = lado*lado
    def calcular_perimetro(self):
        lado =self.origen.calcular_distancia(self.fin) 
        self.perimetro = 4*lado

class Rectangulo(Figura):
    def calcular_area(self):
        interseccion=Punto(self.origen.x,self.fin.y)
        self.area=(self.origen.calcular_distancia(interseccion)*interseccion.calcular_distancia(self.fin))
    def calcular_perimetro(self):
    
    .



