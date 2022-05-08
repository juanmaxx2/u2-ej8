class Conjunto:
    __lista=[]
    
    def __init__(self):
        self.__lista=[]
    
    def getConjunto(self):
        return self.__lista
    
    def AgregarNum(self,num):
        if num not in self.getConjunto():
            self.__lista.append(num) 
    
    def __add__(self,other):
        for i in range(len(other.getConjunto)):
            if not other.getConjunto()[i] in self.getConjunto():
                self.agregarNumero(other.getConjunto()[i])
        return self
    
    def __sub__(self,other):
        nuevoConjunto=Conjunto()
        for i in range(len(other.getConjunto)):
            if not other.getConjunto()[i] in self.getConjunto():
                nuevoConjunto.AgregarNum(other.getConjunto()[i])
    
    def __eq__(self,other):
        return self.__lista==other.__lista