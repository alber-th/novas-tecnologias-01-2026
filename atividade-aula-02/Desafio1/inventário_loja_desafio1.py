# Estoque da loja
estoque = [
    {"nome": "Notebook",    "preco": 3500.00, "quantidade": 5},
    {"nome": "Mouse",       "preco": 80.00,   "quantidade": 20},
    {"nome": "Teclado",     "preco": 250.00,  "quantidade": 0},
    {"nome": "Monitor",     "preco": 1200.00, "quantidade": 3},
    {"nome": "Headset",     "preco": 450.00,  "quantidade": 0},
    {"nome": "Webcam",      "preco": 300.00,  "quantidade": 8},
]

# Calcular valor total e imprimir itens com valor > R$500
total_estoque = 0

print("=== Itens com valor acima de R$ 500 ===")
for item in estoque:
    valor_item = item["preco"] * item["quantidade"]  # preço × quantidade
    total_estoque += valor_item

    if valor_item > 500:
        print(f"  {item['nome']}: R$ {valor_item:.2f}")

print(f"\nValor total em estoque: R$ {total_estoque:.2f}")

# Bônus: list comprehension — produtos em falta (quantidade == 0)
em_falta = [item["nome"] for item in estoque if item["quantidade"] == 0]
print(f"\nProdutos em falta: {em_falta}")
