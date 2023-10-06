

class Cursor:
    def __init__(self, valor_atual):
        self.__valor_atual = valor_atual


    @property
    def valor_atual(self):
        return self.__valor_atual
    @valor_atual.setter
    def valor_atual(self, valor_atual):
        self.__valor_atual = valor_atual

    def avancarKPosicoes(self, k):
        for i in range(k):
            self.valor_atual = self.valor_atual.prox

    def retrocederKPosicoes(self, k):
        for i in range(k):
            self.valor_atual = self.valor_atual.ant

    def irParaPrimeiro(self):
        # if self.valor_atual==None:
        #     pass
        while self.valor_atual.ant!=None:
            self.valor_atual=self.valor_atual.ant

    def irParaUltimo(self):
        while self.valor_atual.prox!=None:
            self.valor_atual=self.valor_atual.prox
