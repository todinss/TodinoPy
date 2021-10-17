# La classe retta

class retta:
    def __init__(self,a,b,c,):

    # un attributo privato si dichiara con il doppio underscore ( __ )    
        self.__a = a  
        self.__b = b
        self.__c = c
        self.__punti = []
    
    def __init__(self, p1, p2):
        '''
        questo costruttore deve generare una retta a partire da due punti.
        p1 e p2 sono tuple che identificano le coordinate dei punti a partire
        dai quali vanno ricavati a,b e c ed inizializzati gli attributi di istanza
        '''

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c

    def eqEsplicita(self):
        if self.__b == 0:
            return f"\nForma esplicita dell'equazione: \n L'equazione è impossibile"
        elif self.__a == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__c / self.__b}"
        elif self.__c == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__a / self.__b}"
        else:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__a / self.__b}x + {-self.__c / self.__b}"

    def eqImplicita(self):
        if self.__b == 0:
            return f"\nForma implicita dell'equazione:\n {self.__a}x + {self.__c} = 0"       
        elif self.__a == 0:
            return f"\nForma implicita dell'equazione:\n {self.__b}y + {self.__c} = 0"    
        elif self.__c == 0:
            return f"\nForma implicita dell'equazione:\n {self.a}x + {self.__b}y = 0"    
        else:   
            return f"\nForma implicita dell'equazione:\n {self.__a}x + {self.__b}y + {self.__c} = 0 "

    def trovaY(self, x):
         return f"\n Y: \n y = {-self.__a / self.__b}*x + {-self.__c / self.__b}"

    def punti(self, N, M):
        '''
        definire il metodo che a partire da N ed M genera tutte le coppie (tuple) di x e y 
        appartengono alla retta nell'intervallo N e M dell'asse X.
        '''

    def m(self):
        if self.__b == 0:
            return f"\nCoefficiente angolare: \n Il coefficiente angolare non è definito; la retta è parallela all'asse y"
        else:
            return f"\nCoefficiente angolare: \n m = {-self.__b / self.__a}"

    def intersezione(self, s):
        '''
        acquisita una retta s in input, questo metodo deve restituire il punto in comune 
        (sottoforma di tupla), verificandone l'esistenza. Restituire "null" se le rette sono 
        in parallelo oppure la lista __punti() se le rette dovessero coincidere. 
        '''
        return 0
