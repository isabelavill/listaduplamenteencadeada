# inicio(elemento)
# fim(elemento)
# tamanho
from elemento import Elemento
from cursor import Cursor

class ListaDuplamenteEncadeada:
    def __init__(self, tamanho):
        self.__cursor = Cursor(None)
        self.__lista = 0
        self.__tamanho = tamanho


    def listaVazia(self):
        if self.__lista == 0:
            return True
        return False

    def listaCheia(self):
        if self.__lista == self.__tamanho:
            return True
        return False
    
    def acessarAtual(self):
        return self.__cursor.valor_atual

    def InserirAntesDoAtual(self, novo):

        novo_elemento = Elemento(novo)

        if self.listaVazia():
            self.__cursor.valor_atual=novo_elemento
            self.__lista+=1

        elif self.listaCheia():
            print ("Lista cheia, não é possível inserir mais elementos.")

        elif self.__cursor.valor_atual.ant is None:
            self.__cursor.valor_atual.ant = novo_elemento
            novo_elemento.prox = self.__cursor.valor_atual
            self.__lista += 1
            
        else:
            self.cursor.retrocederKPosicoes(1)
            novo_elemento.prox = self.cursor.valor_atual.prox
            self.cursor.valor_atual = novo_elemento
            self.__lista += 1


    def InserirAposAtual(self,novo):
        novo_elemento = Elemento(novo)

        if self.listaVazia():
            self.__cursor.valor_atual=novo_elemento
            self.__lista+=1

        elif self.listaCheia():
            print ("Lista cheia, não é possível inserir mais elementos.")

        elif self.__cursor.valor_atual.prox is None:
            self.__cursor.valor_atual.prox = novo_elemento
            novo_elemento.ant = self.__cursor.valor_atual
            self.__lista += 1
        else:
            novo_elemento.prox = self.cursor.valor_atual.prox
            novo_elemento.ant = self.__cursor.valor_atual
            self.__lista += 1


    def InserirComoUltimo(self,novo):
        if self.listaVazia():
            novo_elemento=Elemento(novo)
            self.__cursor.valor_atual=novo_elemento
            self.__lista+=1
        elif self.listaCheia():
            print ("Lista cheia, não é possível inserir mais elementos.")
        else:
            self.cursor.irParaUltimo()
            self.InserirAposAtual(novo)


    def InserirComoPrimeiro(self,novo):
        if self.listaVazia():
            novo_elemento=Elemento(novo)
            self.__cursor.valor_atual=novo_elemento
            self.__lista+=1
        elif self.listaCheia():
            print ("Lista cheia, não é possível inserir mais elementos.")
        else:
            self.cursor.irParaPrimeiro()
            self.InserirAntesDoAtual(novo)

    def InserirNaPosicao(self,k,novo): 
        novo_elemento=Elemento(novo)
    
        if self.listaVazia():
            self.__cursor.valor_atual=novo_elemento
            self.__lista+=1
        if self.listaCheia():
            print ("Lista cheia, não é possível inserir mais elementos.")
        elif k > self.tamanho:
            print("Posição inválida")
        else:
            self.cursor.irParaPrimeiro()
            self.cursor.avancarKPosicoes(k+1)
            self.InserirAntesDoAtual(novo)
            

    def excluirAtual(self):
        if self.listaVazia():
            print("Não há elementos para serem excluidos")
        elif self.cursor.valor_atual.ant==None and self.cursor.valor_atual.prox==None:
            self.cursor.valor_atual=None
            self.__lista-=1
        elif self.cursor.valor_atual.ant==None:
            self.cursor.valor_atual.prox.ant=None
            self.cursor.valor_atual=self.cursor.valor_atual.prox
            self.__lista-=1
        elif self.cursor.valor_atual.prox==None:
            self.cursor.valor_atual.ant.prox=None
            self.cursor.valor_atual=self.cursor.valor_atual.ant
            self.__lista-=1
        else:
            self.cursor.valor_atual.ant.prox = self.cursor.valor_atual.prox
            self.cursor.valor_atual.prox.ant = self.cursor.valor_atual.ant
            self.cursor.valor_atual = self.cursor.valor_atual.prox
            self.__lista-=1

    def excluirPrim(self):
        if self.listaVazia():
            print("Não há elementos para serem excluidos")
        else:
            self.cursor.irParaPrimeiro()
            print(f'Primeiro elemento excluído.')
            self.excluirAtual()

    def excluirUlt(self):
        if self.listaVazia():
            print("Não há elementos para serem excluidos")
        else:
            self.cursor.irParaUltimo()
            print(f'Último elemento excluído.')
            self.excluirAtual()

    def excluirElem(self, chave):
        if self.listaVazia():
            print("Não há elementos para serem excluidos")
        else:
            existe = self.buscarParaExcluir(chave)
            if existe:
                self.excluirAtual()
                print(f'Elemento {chave} excluído.')
            else:
                print("Esse elemento não existe")
            
    
    def excluirDaPos(self,k): 
        if self.listaVazia():
            print("Não há elementos para serem excluidos")
        elif k > self.tamanho:
            print("Posição inválida")
        else:
            self.cursor.irParaPrimeiro()
            self.cursor.avancarKPosicoes(k)
            self.excluirAtual()
            print(f"Elemento excluido da posição {k}.")

    def buscar(self,chave):
        if self.listaVazia():
            print("Não há elementos nesta lista.")
        else:
            self.__cursor.irParaPrimeiro()
            elemento_encontrado = self.__cursor.valor_atual
            
            while elemento_encontrado.valor!=chave:
                if self.__cursor.valor_atual.prox == None:
                    print(f"Elemento {chave} não encontrado.")
                    return False
                else:
                    self.__cursor.avancarKPosicoes(1)
                    elemento_encontrado=self.cursor.valor_atual
            print(f"Elemento {chave} encontrado.")
            return True

    def buscarParaExcluir(self,chave):
            self.__cursor.irParaPrimeiro()
            elemento = self.__cursor.valor_atual
            
            while elemento.valor!=chave:
                self.__cursor.avancarKPosicoes(1)
                elemento=self.cursor.valor_atual
                if self.__cursor.valor_atual== None:
                    return False
            return True

    @property
    def inicio(self):
        return self.__inicio
    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim
    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    @property
    def tamanho(self):
        return self.__tamanho
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @property
    def cursor(self):
        return self.__cursor
    @cursor.setter
    def cursor(self, cursor):
        self.__cursor = cursor

    @property
    def lista(self):
        return self.__lista
    @lista.setter
    def lista(self, lista):
        self.__lista =lista

