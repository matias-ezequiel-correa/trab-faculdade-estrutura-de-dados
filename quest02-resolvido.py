class FilaDeAtendimento: #Define uma classe para representar a fila de caminhoneiros.
    def __init__(self):
        self.fila = [] #Inicia a lista vazia.

    def adicionar(self, caminhoneiro): #Define a função para adicionar um novo caminhoneiro à fila de atendimento.
        if len(self.fila) < 10:
            self.fila.append(caminhoneiro) #Acresenta o caminhoneiro no fim da fila.
            print(f"{caminhoneiro} está aguardando na fila...")
        else:
            print("Fila de caminhoneiros está cheia. Não é possível adicionar mais caminhoneiros.")

    def listar_fila(self): #Define a função para listar os caminhoneiros na fila de atendimento.
        if self.fila:
            print("Os Caminhoneiros que estão aguardando na fila:")
            for i, caminhoneiro in enumerate(self.fila, start=1):
                print(f"{i}. {caminhoneiro}") #Lista a fila de atendimento.
        else:
            print("Fila vazia. Ninguem está na fila!")

    def atenderCaminhoneiro(self): #Define a função para atender o próximo caminhoneiro.
        if self.fila:
            caminhoneiro_atendido = self.fila.pop(0) #Atende o primeiro caminhoneiro e retira-o da fila.
            print(f"{caminhoneiro_atendido} foi atendido com sucesso!")  #Informa que o caminhoneiro foi atendido.
        else:
            print("Nenhum caminhoneiro para atender!")


def main(): #Função principal do programa para gerenciar a fila de caminhoneiros.
    fila_atendimento = FilaDeAtendimento() #Instância de FilaDeAtendimento.

    while True:
        print("\n---Atendimento de caminhoneiro:---") #Exibe o menu de atendimento para caminhoneiros.
        print("1. Adicionar Caminhoneiro")
        print("2. Ver Fila de Atendimento")
        print("3. Atender Seguinte Caminhoneiro")
        print("0. Fechar Programa")

        op = input("Escolha uma opção: ") # Solicita ao usuário que escolha uma opção.

        if op == '1':
            caminhoneiro = input("Nome do caminhoneiro: ")
            fila_atendimento.adicionar(caminhoneiro) #Solicita a função de adicionar caminhoneiro.
        elif op == '2':
            fila_atendimento.listar_fila() #Solicita a função de listar a fila de Atendimento.
        elif op == '3':
            fila_atendimento.atenderCaminhoneiro() #Solicita a função de atender caminhoneiro.
        elif op == '0':
            print("Programa fechado.") 
            break #Encerra o loop e termina a execução do programa.
        else:
            print("Opção inválida.")

if __name__ == "__main__": #Verifica se o script está sendo executado.
    main()  #Chama a função principal para iniciar a execução.
