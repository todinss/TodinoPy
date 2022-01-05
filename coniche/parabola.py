class parabola:
    def __init__(self, tipo="param", p1=None, p2=None, p3=None, p4=None):
        if(tipo == "param"):
            self.__a = int(p1)
            self.__b = int(p2)
            self.__c = int(p3)
            self.__punti = []
        
        elif(tipo == "fuocoDiret"):
            self.__p1 = int(p1)
            self.__p2 = int(p2) 
            self.__p3 = int(p3)
            self.__a = 1/(2*self.__p2 - 2*self.__p3)
            self.__b = -2*self.__a * self.__p1
            self.__c = (4*self.__p2*self.__a + self.__b*self.__b - 1)/(4*self.__a)

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def fuoco(self, x, y):
         self.__x = (-self.__b) / (self.__a * 2)
         self.__y = (-(self.__b * self.__b) - 4 * self.__a * sefl.__c) / 4 * self.__a
        

    def direttrice(self, asse_simmetria = "x"):
        if (asse_simmetria=="x"):
            x = (-1 - ((self.__b * self.__b) - 4 * self.__a * sefl.__c)) / 4 * self.__a
        elif (asse_simmetria=="y"):
              y = (-1 - ((self.__b * self.__b) - 4 * self.__a * sefl.__c)) / 4 * self.__a

    
