# ant 
# prox    
# elemento

class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__prox = None
        self.__ant = None

        
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self, valor):
        self.__prox = valor

    @property
    def ant(self):
        return self.__ant
    @ant.setter
    def ant(self, valor):
        self.__ant = valor
