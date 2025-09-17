import math

class Punto():
    # método de inicialización
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    # comandos
    def establecerX(self,x):
        self.__x = x
    def establecerY(self,y):  
        self.__y=y
    def copy(self,punto):
        self.__x = punto.obtenerX()
        self.__y = punto.obtenerY()
    # consultas
    def obtenerX(self):
        return self.__x
    def obtenerY(self):  
        return self.__y
    def __str__(self):
        return '['+str(self.__x)+','+str(self.__y)+']'
    def distancia(self,punto):
        # requiere punto ligado
        base = self.__x - punto.obtenerX()
        altura = self.__y - punto.obtenerY()
        return math.sqrt(base*base+altura*altura)
    def equals(self,punto):
        return self.__x == punto.obtenerX() and self.__y == punto.obtenerY() 
    def clone(self):
        punto = Punto(self.__x,self.__y)       
        return punto