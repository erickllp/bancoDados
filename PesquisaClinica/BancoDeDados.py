class BancoDeDados:
    pacientes = []  # lista compartilhada entre todas as instâncias

    def __init__(self, nome, idade):    # Cadastro de paciente não cadastrados
        self.nome = nome
        self.idade = idade

    def cadastrar(self):
        BancoDeDados.pacientes.append(self.nome)
        print(f"Pronto {self.nome}, você foi cadastrado!\nIdade: {self.idade}")

    @classmethod
    def verificacao(cls, nome):   # verificação de participantes já cadastrados
        return nome in cls.pacientes

    def resultados(self, aprovados, reprovados):
        total = aprovados + reprovados
        if total == 0:
            print("Nenhum resultado disponível.")
            return
        eficacia_geral = (aprovados / total) * 100
        print(f"Eficácia geral: {eficacia_geral:.2f}%")