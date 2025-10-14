from multipledispatch import dispatch
from robot import Robot

class SectoresFabrica():
    def __init__(self,max):
        '''Crea un arreglo con max elementos, cada elemento
        representa un sector de la fábrica'''
        self.__listSec = [None]*max

    @dispatch(Robot,int)
    def asignar(self,rob,sec):
        '''Asigna el robot rob al sector sec. Requiere 0 <= sec <
        cantSectores()'''
        self.__listSec[sec] = rob
    
    @dispatch(Robot)
    def asignar(self,rob):
        '''asignar un Robot rob en un sector libre, requiere que
        haya al menos un sector libre'''
        i = 0
        while self.__listSec[i] != None:
            i += 1
        self.__listSec[i] = rob
    
    @dispatch(int)
    def desasignar(self,sec):
        '''Elimina la asignación del robot del sector sec.
        Requiere 0 <= sec < cantSectores()'''
        print("designar con sector")
        self.__listSec[sec] = None

    @dispatch(Robot)
    def desasignar(self,rob):
        '''Elimina la asignación del robot rob de todos los
        sectores a los que está asignado'''
        print("designar con robot")
        i = 0
        while i < self.cantSectores():
            if self.__listSec[i] == rob:
                self.__listSec[i] = None
            i += 1

    def cantSectores(self):
        # Retorna la cantidad de sectores de la fábrica
        return len(self.__listSec)

    def cantSectoresOcupados(self):
        # Calcula cuántos sectores estan asociados a un robot 
        i = 0 
        cont = 0
        while i < self.cantSectores():
            if self.__listSec[i] != None:
                cont += 1
            i += 1
        return cont

    def estaRobot(self,rob):
        '''Decide si algún sector tiene asignado un robot con la misma
        identidad que rob'''
        esta = False
        i = 0
        while i < self.cantSectores() and not esta:
            esta = self.__listSec[i] == rob
            i += 1
        return esta

    def existeSector(self,sec):
        return sec >= 0 and sec < self.cantSectores()

    def robotSector(self,sec):
        '''Retorna el Robot en un sector sec, requiere 0 <= sec <
        cantSectores()'''
        return self.__listSec[sec]

    def todosOcupados(self):
    # Decidir si todos los sectores tienen asignado un robot
        hayNone = False
        i = 0 
        while i < self.cantSectores() and not hayNone:
            hayNone = self.__listSec[i] == None
            i += 1
        return not hayNone
    
    def cantMasEnergia(self,g):
        '''Cuenta la cantidad de sectores asignados a robots con
        más de g unidades de energía'''
        cont = 0
        for i in range(self.cantSectores()):
            if self.__listSec[i] != None:
                if self.__listSec[i].obtenerEnergia() > g:
                    cont += 1
        return cont

    def cantSectoresPasos(self,g):
        '''Cuenta la cantidad de sectores asignados a robots con
        energía suficiente como para dar exactamente g pasos.'''
        cont = 0
        for i in range(self.cantSectores()):
            if self.__listSec[i] != None:
                if self.__listSec[i].cantPasos() == g:
                    cont += 1
        return cont
    
    def cantDiferentes(self):
        '''Cuenta la cantidad de robots diferentes asignados a
        sectores'''
        cont = 0
        for i in range(self.cantSectores()):
            if self.__listSec[i] != None:
                if not self.__estaAntes(self.__listSec[i],i):
                    cont += 1
        return cont

    def __estaAntes(self,rob,sec):
        '''Decide si el robot rob, que asume ligado, está asignado
        a alguno de los sectores anteriores a sec'''
        esta = False
        i = 0
        while i < sec and not esta:
            esta = self.__listSec[i] == rob 
            i += 1  
        return esta
    
    def alMenosNOcupados(self,n):
        '''Retorna true si la estructura mantiene al menos n sectores con
        robots asignados'''
        for i in range(self.cantSectores()):
            if n > 0:
                if self.__listSec[i] != None:
                    n -= 1
        return n == 0

    def nConsecutivosIguales(self,n):
        '''Decidir si la tabla mantiene al menos n sectores consecutivos
        asignados a un mismo robot.'''
        cont = 1
        for i in range(self.cantSectores()-1):
            if n > cont:
                if self.__listSec[i] != None and self.__listSec[i] == self.__listSec[i+1]:
                    cont += 1
            else:
                cont = 1
        return cont == n 