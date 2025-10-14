class Planilla():
    def __init__(self,m5,m10,m15):
        self.__menor5=m5
        self.__menor10=m10
        self.__menor15=m15
    
    def establecerMenor5(self,m5):
        self.__menor5=m5
    def establecerMenor10(self,m10):
        self.__menor10=m10
    def establecerMenor15(self,m15):
        self.__menor15=m15
    def obtenerMenor5(self):
        return self.__menor5
    def obtenerMenor10(self):
        return self.__menor10
    def obtenerMenor15(self):
        return self.__menor15
    def obtenerPorcentaje(self,aniosAnt):
        # Requiere aniosAnt < 15
        if aniosAnt < 5:
            porc = self.__menor5
        else:
            if 5 <= aniosAnt < 10:
                porc = self.__menor10
            else:
                porc = self.__menor15
        return porc