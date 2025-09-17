from presionArterial import *

class TestPresion():
    def main(self):
        med6am = PresionArterial(75,115)
        med6pm = PresionArterial(75,115) 
        if med6am == med6pm:
            print('Es la misma medición')
        if med6am.equals(med6pm):
            print('Mediciones equivalentes')
        
if __name__ == '__main__':
    test = TestPresion()
    test.main()