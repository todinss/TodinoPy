# La classe retta

class retta:
    def __init__(self,a,b,c,):

    def __init__(self, tipo="param", p1=None, p2=None, p3=None, p4=None):
        if tipo == "param":
            self.__a = p1
            self.__b = p2
            self.__c = p3
            self.__punti = []
            self.__m = p4
    
    def __init__(self, p1, p2):
        '''
        questo costruttore deve generare una retta a partire da due punti.
        p1 e p2 sono tuple che identificano le coordinate dei punti a partire
        dai quali vanno ricavati a,b e c ed inizializzati gli attributi di istanza
        '''

 def getA(self):
        return f"\n a = {self.__a}"
    
    def getB(self):
        return f"\n b = {self.__b}"

    def getC(self):
        return f"\n c = {self.__c}"

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

    def Y(self, x):
         self.__x = float(x)
            if self.__b == 0:
            return f"\nla retta è parallela all'asse delle Y"
        elif self.__a == 0:
            return f" y = {-self.__c / self.__b}"
        elif self.__c == 0:
            return f" y = {-self.__a * self.__x / self.__b}" 
        else:
            return f"\n Y: \n y = {-self.__a / self.__b}*x + {-self.__c / self.__b}"

    def punti(self, N, M):
        self.__N = int(N)
        self.__M = int(M)
    
        for self.__N in range (self.__M):
            tupla = (self.__x, (-self.__a * self.__x) / self.__b + (-self.__c / self.__b))
            self.__x = self.__x + 1
            self.__punti.append(tupla)
        return f"\n Le coordinate dei punti appartenenti alla retta sono: \n {self.__punti}"

    def m(self):
        if self.__b == 0:
            return f"\nCoefficiente angolare: \n Il coefficiente angolare non è definito; la retta è parallela all'asse y"
        else:
            return f"\nCoefficiente angolare: \n m = {-self.__b / self.__a}"

    def intersezione(self, s):
         def instersezione(self, a1 , b1 , c1):
        self.__a1 = int(a1)
        self.__b1 = int(b1)
        self.__c1 = int(c1)
        if (-self.__b / self.__a) == (-self.__b1 / self.__a1):
            if self.__c == self.__c1:
                return f"\nLe rette sono coincidenti \n {self.__punti}"
            else:
                return f"Null"
        elif self.__c == self.__c1:
            return f"\nIl putnto di incontro delle due rette è: (0, {self.__c})" 
        else:
            return f"\nLe rette sono incidenti e la coordinata del punto d'incidenza è: ({((-self.__c / self.__b)+(self.__c1 / self.__b1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))}, {((-self.__b / self.__c)+(self.__b1 / self.__c1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))})"

print(valori.Implicita())
print(valori.Esplicita())
print(valori.m())
print(valori.trovaY(input('x = ')))
print(valori.instersezione(input('a1 = ' ), input('b1 = ' ), input('c1 = ' )))
