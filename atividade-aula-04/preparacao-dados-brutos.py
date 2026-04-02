categorias = set()
for t in transacoes:
    categoria = t[1]
    categorias.add(categoria)

print(categorias)

totais = {}
for t in transacoes:
    _, categoria, valor = t
    if categoria not in totais:
        totais[categoria] = 0
    totais[categoria] += valor
    
# Não sei o que está dando de errado aqui.