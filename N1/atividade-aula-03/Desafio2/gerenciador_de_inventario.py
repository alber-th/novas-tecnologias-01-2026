# desafio 2

class Equipamento:
    def __init__(self, id_equipamento, nome, preco_diaria):
        self.id_equipamento = id_equipamento
        self.nome           = nome
        self.preco_diaria   = preco_diaria
        self.status         = "Disponível"

    def alugar(self):
        self.status = "Alugado"

    def devolver(self):
        self.status = "Disponível"


class Locadora:
    def __init__(self):
        self.inventario              = []
        self.faturamento_por_cliente = {}

    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)

    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        for equip in self.inventario:
            if equip.id_equipamento == id_equipamento:
                if equip.status == "Disponível":
                    equip.alugar()
                    custo = equip.preco_diaria * dias

                    # acumula no dicionário de faturamento
                    if nome_cliente in self.faturamento_por_cliente:
                        self.faturamento_por_cliente[nome_cliente] += custo
                    else:
                        self.faturamento_por_cliente[nome_cliente] = custo

                    print(f"Locação realizada! {nome_cliente} alugou '{equip.nome}' "
                          f"por {dias} dia(s). Custo: R$ {custo:.2f}")
                else:
                    print(f"Equipamento '{equip.nome}' não está disponível.")
                return  # encerra após encontrar o equipamento

        print(f"Equipamento com ID {id_equipamento} não encontrado.")

    def equipamentos_disponiveis(self):
        disponiveis = [equip.nome for equip in self.inventario
                       if equip.status == "Disponível"]
        return disponiveis


# test 
locadora = Locadora()

# cadastro equipamentos
locadora.cadastrar_equipamento(Equipamento(1, "Betoneira",    150.0))
locadora.cadastrar_equipamento(Equipamento(2, "Andaime",       80.0))
locadora.cadastrar_equipamento(Equipamento(3, "Compressor",   200.0))

print("\n--- Equipamentos disponíveis ---")
print(locadora.equipamentos_disponiveis())

print("\n--- Realizando locações ---")
locadora.realizar_locacao("Carlos", 1, 3)   # aluga Betoneira por 3 dias
locadora.realizar_locacao("Maria",  2, 5)   # aluga Andaime por 5 dias
locadora.realizar_locacao("Carlos", 1, 2)   # tenta alugar Betoneira (já alugada)

print("\n--- Equipamentos disponíveis após locações ---")
print(locadora.equipamentos_disponiveis())

print("\n--- Faturamento por cliente ---")
for cliente, total in locadora.faturamento_por_cliente.items():
    print(f"  {cliente}: R$ {total:.2f}")

print("\n--- Devolvendo Betoneira ---")
locadora.inventario[0].devolver()
print(locadora.equipamentos_disponiveis())