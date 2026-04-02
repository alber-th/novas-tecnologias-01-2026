class Usuario:
    def __init__(self, id, nome, email):
        self.__id = id
        self.__nome = nome
        self.__email = email

    def get_id(self):
        return self.__id

    def set_id(self, novo_id):
        self.__id = novo_id

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_email(self):
        return self.__email

    def set_email(self, novo_email):
        if "@" in novo_email:
            self.__email = novo_email
        else:
            print("E-mail inválido")
            
#=============================================================================#

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def remover_usuario_por_id(self, id):
        for u in self.usuarios:
            if u.get_id() == id:
                self.usuarios.remove(u)
                break

    def listar_usuarios(self):
        for u in self.usuarios:
            print(u.get_id(), u.get_nome(), u.get_email())