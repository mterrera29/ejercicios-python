from presionArterial import *

class TestPulso():
    def main(self):
        med1 = PresionArterial(60,115)
        med2 = PresionArterial(62,117) 
        pul1 = med1.obtenerPulso()
        pul2 = med2.obtenerPulso()
        print(f'Primera medición pulso: {pul1}')
        print(f'Segunda medición pulso: {pul2}')
    
if __name__ == '__main__':
    test = TestPulso()
    test.main()