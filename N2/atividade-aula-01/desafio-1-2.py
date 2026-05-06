import numpy as np

# ============================================================
# DESAFIO 1 - Análise de Notas de uma Turma
# ============================================================
print("=" * 60)
print("DESAFIO 1 - Análise de Notas")
print("=" * 60)

notas = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 4.5, 6.0, 5.5],
    [9.0, 9.5, 8.5, 10.0],
    [3.0, 4.0, 5.0, 4.5],
    [8.0, 7.5, 9.0, 8.5]
])

# 1) Médias por aluno (média das 4 provas -> média ao longo das colunas, axis=1)
medias_alunos = notas.mean(axis=1)
print("\n1) Médias por aluno:")
for i, m in enumerate(medias_alunos):
    print(f"   Aluno {i+1}: {m:.3f}")

aluno_maior = np.argmax(medias_alunos)
print(f"\n   -> Aluno com a MAIOR média: Aluno {aluno_maior+1} "
      f"(média = {medias_alunos[aluno_maior]:.3f})")

# 2) Normalização por coluna (z-score): (x - média_coluna) / desvio_coluna
# axis=0 -> opera ao longo das linhas, gerando um valor POR COLUNA
media_colunas = notas.mean(axis=0)        # shape (4,)
desvio_colunas = notas.std(axis=0)        # shape (4,)
notas_normalizadas = (notas - media_colunas) / desvio_colunas  # broadcast (5,4)-(4,)

print("\n2) Notas normalizadas por coluna (z-score):")
print(f"   Média de cada coluna   : {np.round(media_colunas, 3)}")
print(f"   Desvio de cada coluna  : {np.round(desvio_colunas, 3)}")
print("   Matriz normalizada:")
print(np.round(notas_normalizadas, 3))

# 3) Aprovados: alunos com média >= 6.0 (indexação booleana)
mask_aprovados = medias_alunos >= 6.0
notas_aprovados = notas[mask_aprovados]

print("\n3) Aprovados (média >= 6.0) — notas originais:")
indices_aprov = np.where(mask_aprovados)[0] + 1
print(f"   Alunos aprovados: {list(indices_aprov)}")
print(notas_aprovados)


# ============================================================
# DESAFIO 2 - Manipulação de Imagem em Escala de Cinza
# ============================================================
print("\n" + "=" * 60)
print("DESAFIO 2 - Imagem em Escala de Cinza")
print("=" * 60)

imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

# 1) Estatísticas de brilho
brilho_geral = imagem.mean()
brilho_linhas = imagem.mean(axis=1)   # média de cada linha
brilho_colunas = imagem.mean(axis=0)  # média de cada coluna

print(f"\n1) Brilho médio geral : {brilho_geral:.3f}")
print(f"   Brilho por linha   : {np.round(brilho_linhas, 3)}")
print(f"   Brilho por coluna  : {np.round(brilho_colunas, 3)}")

linha_mais_escura = np.argmin(brilho_linhas)
print(f"\n   -> Linha mais ESCURA: linha {linha_mais_escura} "
      f"(média = {brilho_linhas[linha_mais_escura]:.3f})")

# 2) Limiarização (threshold = 128) usando indexação booleana
# Cria-se uma cópia para não alterar a original
imagem_bin = imagem.copy()
mask_clara = imagem_bin >= 128
imagem_bin[mask_clara] = 255
imagem_bin[~mask_clara] = 0

print("\n2) Imagem binarizada (>=128 -> 255 ; <128 -> 0):")
print(imagem_bin)