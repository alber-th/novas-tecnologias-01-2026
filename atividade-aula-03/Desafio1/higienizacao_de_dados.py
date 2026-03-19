# desafio 1

def limpar_dados(lista):
    # vai filtra apenas usuários com o status_ativo == True
    ativos = list(filter(lambda u: u["status_ativo"] == True, lista))

    # trata o nome e o email do usuário
    for usuario in ativos:
        usuario["nome"] = usuario["nome"].upper()
        usuario["email"] = usuario["email"].lower()

    return ativos


# test
usuarios = [
    {"nome": "Ana Silva",   "email": "ANA@EMAIL.COM",    "status_ativo": True},
    {"nome": "Bruno Lima",  "email": "BRUNO@EMAIL.COM",  "status_ativo": False},
    {"nome": "carla souza", "email": "CARLA@Email.com",  "status_ativo": True},
    {"nome": "Diego Melo",  "email": "Diego@EMAIL.com",  "status_ativo": False},
]

resultado = limpar_dados(usuarios)
for u in resultado:
    print(u)