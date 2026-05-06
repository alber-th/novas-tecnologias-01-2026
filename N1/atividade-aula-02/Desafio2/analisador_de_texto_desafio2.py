# Recebe a frase do usuário
frase = input("Digite uma frase: ")

# Separar em palavras (converte para minúsculas para evitar "Python" ≠ "python")
palavras = frase.lower().split()

# Contar frequência com dicionário
frequencia = {}
for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1
    # .get(palavra, 0) retorna o valor atual ou 0 se a palavra ainda não existe

# Palavras únicas
palavras_unicas = set(palavras)  # set remove duplicatas automaticamente

# Palavras que se repetem mais de uma vez
se_repetem = [p for p, qtd in frequencia.items() if qtd > 1]

# Palavra mais frequente
mais_frequente = max(frequencia, key=frequencia.get)

# Relatório final
print("\n===== RELATÓRIO =====")
print(f"Total de palavras:        {len(palavras)}")
print(f"Total de palavras únicas: {len(palavras_unicas)}")
print(f"Palavras que se repetem:  {se_repetem}")
print(f"Palavra mais frequente:   '{mais_frequente}' ({frequencia[mais_frequente]}x)")
