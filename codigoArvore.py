
"--------------------------Algoritmos--------------------------------"


class elemento:
    def __init__(self):
        self.valor = 0
        self.esquerda = None
        self.direita = None
        self.anterior = None
        self.proximo = None

class pilha:
    def __init__(self):
        self.topo = None   

    def empilha(self, chave):
        novo = elemento()
        novo.valor = chave
        novo.proximo = self.topo
        self.topo = novo
        return self.topo
    
    def desempilha(self):
      if(self.topo != None):
        guardaDesempilhado = self.topo.valor
        auxiliar = self.topo
        self.topo = self.topo.proximo
        del auxiliar
      else:
        print("A pilha está vazia")
      return guardaDesempilhado


def busca(pont, chave, pai=None):
    if (pont == None):
      F = 0
    else:
      if(pont.valor == chave):
        F = 1
      else:
        if(chave < pont.valor):
          if pont.esquerda == None:
            F = 2
          else:
            pai = pont
            pont = pont.esquerda
            pont,F , pai = busca(pont, chave,pai)
        else:
          if(pont.direita == None):
            F = 3
          else:
            pai = pont
            pont = pont.direita
            pont, F, pai = busca(pont,chave,pai)
    return pont, F, pai


class ArvoreDeBusca:
    def __init__(self):
        self.raiz = None
    def incluir(self, chave):
        pont = self.raiz
        pont, F,pai = busca(pont,chave)
        if (F == 1):
            print("O elemento já encontra-se na árvore.")
        else:
          novo = elemento()
          novo.valor = chave
          novo.esquerda = None
          novo.direita = None
          if (F == 0):
            self.raiz = novo
          else:
            if (F == 2):
              pont.esquerda = novo
            else:
              pont.direita = novo
        return self.raiz
    
    def excluir(self, chave):
        pont, F, pai = busca(self.raiz, chave)
        if (F == 1):
          if(pont.esquerda == None):
            if(pont == self.raiz):
              self.raiz = self.raiz.direita
            else:
              if(pont == pai.esquerda):
                pai.esquerda = pont.direita
              else:
                pai.direita = pont.direita
          else:
            if(pont.direita == None):
              if(pont == self.raiz):
                self.raiz = self.raiz.esquerda
              else:
                if(pont == pai.esquerda):
                  pai.esquerda = pont.direita
                else: 
                  if(pont == pai.esquerda):
                    pai.esquerda = pont.esquerda
                  else:
                    pai.direita = pont.esquerda
            else:
              pontAuxiliar = pont.direita
              paiAuxiliar = pont
              while (pontAuxiliar != None):
                paiAuxiliar = pontAuxiliar
                pontAuxiliar = pontAuxiliar.esquerda
              if(paiAuxiliar != pont):
                paiAuxiliar.esquerda = pontAuxiliar.direita
                paiAuxiliar.direita = pont.direita
              pontAuxiliar.esquerda = pont.esquerda
              if(pont == self.raiz):
                self.raiz = pontAuxiliar
              else:
                if(pai.esquerda == pont):
                  pai.esquerda = pontAuxiliar
                else:
                  pai.direita = pontAuxiliar
        else:
          print("O elemento não encontra-se na árvore, sendo assim, não é possível excluí-lo")
        del pont

    def preOrdem(self): 
        pont = self.raiz 
        Pilha = pilha()
        if(pont.valor == 0):
          print("A arvore encontra-se vazia")
        else:
            Pilha.empilha(pont) 
            while(Pilha.topo!= None):
                print(pont.valor)
                if(pont.direita != None):
                    Pilha.empilha(pont.direita)
                if(pont.esquerda != None):
                    pont = pont.esquerda
                else:
                    pont = Pilha.desempilha()

    def mostrarArvore(self, elemento, altura = 0):
        if (elemento != None):
            self.mostrarArvore(elemento.direita, altura + 1)
            print(" " * 4 * altura + f" {elemento.valor}")
            self.mostrarArvore(elemento.esquerda, altura + 1)


"-----------------------------------------MENU-------------------------------------------------------"

print("Esse programa demonstra o funcionamento de uma Árvore Binária de Busca.")

escolha = 0
arvore = ArvoreDeBusca()

while(escolha != "5"):
    print("\n----------------------- Menu de Acesso -----------------------------")

    print("Para começar, digite o número correspondente a opção desejada baixo:")

    print("_________________________________________________________________________________________")

    print("1 - Incluir || 2 - Excluir || 3 - Caminhamento Pré-ordem || 4 - Mostrar Árvore || 5 - Fim")

    print("_________________________________________________________________________________________")
    
    escolha = input("Digite o número correspondente a sua escolha desntre as opções acima: ")

    if (escolha == "1"):
        valor = int(input("Digite o valor referente à sua escolha para Inclusão: "))
        raiz = arvore.incluir(valor)

    elif (escolha == "2"):
        valor = int(input("Digite o valor referente à sua escolha para Exclusão: "))
        arvore.excluir(valor)

    elif (escolha == "3"):
        print("Caminhamento Pré-Ordem abaixo: ")
        arvore.preOrdem()

    elif escolha == "4":
        print("Segue abaixo a estrutura da Árvore Binária de Busca:")
        arvore.mostrarArvore(arvore.raiz)
        print("é necessário fazer a leitura pensando que o elemento mais a esquerda é o centro da árvore e os elementos acima do centro correspondem a direita e os abaixo do centro correspondem a esquerda (esse raciocínio vale também para os outros elementos, os de cima como filho direito e os de baixo como filho esquerdo)")

    elif (escolha == "5"):
        print("Programa finalizado")