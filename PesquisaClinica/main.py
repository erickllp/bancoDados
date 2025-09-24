from usuarios import login, usuarios
from BancoDeDados import BancoDeDados
from gestao_ambiental import registrar_aspecto, criar_plano

def menu():
    usuario = None
    while not usuario:
        usuario = login()  # Login obrigatório

    while True:
        print("\n=== MENU ===")
        if usuario["tipo"] == "paciente":
            print("1 - Consultar cadastro / resultados")
        elif usuario["tipo"] == "medico":
            print("1 - Cadastrar paciente")
            print("2 - Consultar paciente")
            print("3 - Atender paciente e registrar impacto")
        elif usuario["tipo"] == "admin":
            print("1 - Cadastrar usuário")
            print("2 - Consultar paciente")
        
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do sistema...")
            break

        # ----------------- ADMIN -----------------
        if usuario["tipo"] == "admin":
            if opcao == "1":
                nome = input("Nome do novo usuário: ")
                senha = input("Senha: ")
                tipo = input("Tipo (admin/medico/paciente): ").lower()
                if tipo not in ["admin", "medico", "paciente"]:
                    print("Tipo inválido!")
                else:
                    usuarios.append({"nome": nome, "senha": senha, "tipo": tipo})
                    print(f"Usuário {nome} ({tipo}) cadastrado!")
            elif opcao == "2":
                nome = input("Digite o nome do paciente: ")
                for p in BancoDeDados.pacientes:
                    if p.nome == nome:
                        p.consultar_paciente()
                        break
                else:
                    print("Paciente não encontrado!")

        # ----------------- MÉDICO -----------------
        elif usuario["tipo"] == "medico":
            if opcao == "1":
                nome = input("Nome do paciente: ")
                idade = int(input("Idade: "))
                paciente = BancoDeDados(nome, idade)
                paciente.cadastrar()
            elif opcao == "2":
                nome = input("Digite o nome do paciente: ")
                for p in BancoDeDados.pacientes:
                    if p.nome == nome:
                        p.consultar_paciente()
                        break
                else:
                    print("Paciente não encontrado!")
            elif opcao == "3":
                if BancoDeDados.fila.empty():
                    print("Nenhum paciente na fila.")
                else:
                    prioridade, paciente = BancoDeDados.fila.get()
                    print(f"\nAtendendo paciente: {paciente.nome} (risco: {paciente.estrato()})")
                    atendimento = input("Descrição do atendimento: ")
                    paciente.registrar_atendimento(atendimento)

                    nodo_impacto = registrar_aspecto()
                    paciente.adicionar_impacto(nodo_impacto)

                    criar_plano(nodo_impacto)

        # ----------------- PACIENTE -----------------
        elif usuario["tipo"] == "paciente":
            # Para fins de exemplo, paciente consulta apenas seu próprio cadastro
            for p in BancoDeDados.pacientes:
                if p.nome == usuario["nome"]:
                    p.consultar_paciente()
                    break
            else:
                print("Cadastro não encontrado!")

if __name__ == "__main__":
    menu()



                        


