class ElementoDaListaSimples:
    def __init__(self, dado, cor):
        self.dado = dado
        self.cor = cor
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None:
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples(dado=elem)
                nodo = nodo.proximo

    def inserirNoFinal(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo
        return
        
    def inserirPrioridade(self, nodo): #Define a função para inserir prioridade na cor "A" na lista.
        if self.head is None: #Caso a lista esteja vazia, insere o nodo como o primeiro elemento.
            self.head = nodo
            return
        
        #Se o primeiro elemento não for da cor "A" ou tiver um dado maior que o nodo a ser inserido, insere o nodo no início da lista.
        if self.head.cor != "A" or self.head.dado > nodo.dado or self.head.proximo is None:
            nodo.proximo = self.head
            self.head = nodo
            return
        
        #Procura a posição adequada para inserção, mantendo a ordem crescente dos dados.
        no_atual = self.head
        while no_atual.proximo and no_atual.proximo.cor == "A":
            if no_atual.proximo.dado > nodo.dado:
                break
            no_atual = no_atual.proximo

        #Insere o nodo na posição encontrada.
        nodo.proximo = no_atual.proximo
        no_atual.proximo = nodo

    def inserir(self, dado, cor):
        nodo = ElementoDaListaSimples(dado, cor)
        if self.head is None:
            self.head = nodo
            return
        else:
            if nodo.cor == "V":
                self.inserirNoFinal(nodo)
            else:
                self.inserirPrioridade(nodo)
            return
        
    def imprimirLista(self): #Define a função para imprimir as informações do paciente (número e cor do cartão).
        nodo_atual = self.head
        while nodo_atual is not None:
            print(f"Paciente: {nodo_atual.dado} - {nodo_atual.cor}")
            nodo_atual = nodo_atual.proximo
        print()  
        
def adicionarPaciente(lista, dado, cor):  #Define a função para adicionar um novo paciente na lista.
    lista.inserir(dado, cor)

def menuAdicionar(lista): #Define a função para exibir o menu de adicionar paciente na lista.
    while True:
        print("Adicionando novo paciente:") #Solicitação de informações do paciente ao usuário.
        dado = input("Digite o número do paciente: ")
        cor = input("Digite a cor do cartão do paciente, sendo V = verde ou A = amarelo: ").upper()
        adicionarPaciente(lista, dado, cor)
        print("Paciente adicionado com sucesso!")
        break

def menuFila(lista): #Define a função para exibir a lista de pacientes.
    if lista.head is None: #Verifica se a lista está vazia.
        print("A fila está vazia!")
    else:
        print("Fila de pacientes:") #Se a lista não estiver vazia, imprime a lista de pacientes.
        lista.imprimirLista() 

def main(): #Função principal do programa.
    lista_triagem = ListaEncadeadaSimples() #Instância de ListaEncadeadaSimples.

    while True:
        print("\n---Atendimento de Pacientes:---") #Exibe o menu de atendimento para pacientes.
        print("1. Adicionar Novo Paciente")
        print("2. Ver Fila de Pacientes")
        print("0. Fechar Programa")

        op = input("Escolha uma opção: ") # Solicita ao usuário que escolha uma opção.

        if op == '1':
            menuAdicionar(lista_triagem) #Solicita a função de adicionar paciente.
        elif op == '2':
            menuFila(lista_triagem)  #Solicita a função de ver a fila de pacientes.
        elif op == '0':
            print("Programa fechado.")
            break #Encerra o loop e termina a execução do programa.
        else:
            print("Opção inválida.")

if __name__ == "__main__": #Verifica se o script está sendo executado.
    main()  #Chama a função principal para iniciar a execução.