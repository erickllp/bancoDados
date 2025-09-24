#Lista usuarios armazena os usuários do sistema.

usuarios =  [

    {"nome": "admin", "senha": "1234", "tipo": "admin"},
    {"nome": "medico1", "senha": "abcd", "tipo": "medico"},
    {"nome": "paciente1", "senha": "0000", "tipo": "paciente"}

]

"""

A função login() solicita nome e senha.
Percorre a lista para verificar se existe correspondência.
Retorna o usuário logado se correto ou None se incorreto

"""

def login():
    print("LOGIN\n")   
    nome = input("Usuario: ")
    senha = input("Senha: ")

    for user in usuarios:
        if user ["nome"] == nome and user ["senha"] == senha:
            print(f"Login bem sucedido!: {user['tipo']}\n")
            return user

    print("Usuario ou senha Incorretos!")
    return None