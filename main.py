from lista import ListaDuplamenteEncadeada

if __name__ == "__main__":

    l1=ListaDuplamenteEncadeada(10)


    print(l1.lista) #Exibindo tamanho da lista atual (0)

    l1.InserirAntesDoAtual(10)
    l1.InserirAntesDoAtual(24)

    print('----------------------------------------')
    l1.excluirDaPos(11) #Posição inválida


    l1.InserirAposAtual(30)
    l1.InserirComoPrimeiro(40)
    l1.InserirComoPrimeiro(500)
    l1.InserirComoUltimo(89)
    l1.InserirNaPosicao(2,65)

    print('----------------------------------------')
    l1.InserirNaPosicao(11,8) #Posição inválida
    print('----------------------------------------')

    l1.InserirComoUltimo(54)
    
    l1.buscar(10)
    l1.buscar(24)
    l1.buscar(40)

    print('----------------------------------------')
    l1.buscar(30)
    l1.excluirElem(30)
    l1.buscar(30)
    print('----------------------------------------')

    l1.buscar(500)
    l1.excluirUlt() #Ultimo elemento até entao: 54
    l1.buscar(54)
    print('----------------------------------------')
    
    l1.excluirPrim() #Primeiro elemento até então:500
    l1.buscar(500)
    print('----------------------------------------')

    l1.buscar(100)
    l1.excluirDaPos(2)
    l1.buscar(65)

    print('----------------------------------------')
    print(l1.lista) #exibindo tamanho da lista após realizar operações
 
