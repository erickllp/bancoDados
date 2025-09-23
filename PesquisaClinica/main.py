
from BancoDeDados import BancoDeDados

def menu():
    while True:
        print("Bem vindo ao nosso site\n\nO que Deseja:"
            "\n1 - Deseja se cadastrar para participação de nossa pesquisa?"
            "\n2 - Consultar resultado do seu teste?\n")
        cadastro = input("Insira o número desejado: ")

        if cadastro == "1":
            print("")
            nome = input("Informe seu nome: ")
            idade = input("Informe sua idade: ")
            paciente = BancoDeDados(nome, idade)

            if BancoDeDados.verificacao(nome):
                print(f"{nome}, você já está cadastrado!")
                print("-----------------------------------")
            else:
                paciente.cadastrar()
                print("-----------------------------------")

        elif cadastro == "2":
            nome = input("Digite seu nome para verificar cadastro: ")
            if BancoDeDados.verificacao(nome):
                print(f"{nome}, seu resultado será disponibilizado em breve.")
                print("-----------------------------------")
            else:
                print("Cadastro não encontrado!")
                print("-----------------------------------")
        print("retornamos a tela inicial!!\n")


if __name__ == "__main__":
    menu()



                        


