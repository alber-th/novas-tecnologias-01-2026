"""
Aula 2 — Exercício Parcial (Titanic) + Desafios 1, 2 e 3
========================================================
Resolve todos os itens usando apenas pandas (e numpy onde útil).
"""
import os
import numpy as np
import pandas as pd

pd.set_option('display.width', 140)
pd.set_option('display.max_columns', 20)


def secao(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


# =====================================================================
# EXERCÍCIO PARCIAL — TITANIC
# =====================================================================
secao("EXERCÍCIO PARCIAL — Titanic")

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
LOCAL_FALLBACK = "/home/claude/titanic_local.csv"

# Tarefa 1.1 — carga
try:
    titanic = pd.read_csv(URL)
    print(f"[OK] Lido da URL: {URL}")
except Exception as e:
    titanic = pd.read_csv(LOCAL_FALLBACK)
    print(f"[Aviso] URL indisponível neste ambiente — usando fallback local equivalente.")

# Tarefa 1.2 — head()
print("\n-- head(5) --")
print(titanic.head())

# Tarefa 1.3 — info()
print("\n-- info() --")
titanic.info()

# Tarefa 1.4 — shape
print(f"\n-- shape -- {titanic.shape}  (linhas, colunas)")

# Tarefa 2.1 — describe()
print("\n-- describe() (numéricas) --")
print(titanic.describe())

# Tarefa 2.2 — nunique() em Pclass
print(f"\n-- Pclass.nunique() = {titanic['Pclass'].nunique()}")

# Tarefa 2.3 — value_counts() em Sex
print("\n-- Sex.value_counts() --")
print(titanic['Sex'].value_counts())

# Tarefa 3.1 — loc: Name e Age, índices 0 a 10 (loc inclui o limite superior)
print("\n-- loc[0:10, ['Name','Age']] (limite superior INCLUSO) --")
print(titanic.loc[0:10, ['Name', 'Age']])

# Tarefa 3.2 — iloc: 15ª linha (índice 14, posição 15ª)
print("\n-- iloc[14] (15ª linha) --")
print(titanic.iloc[14])

# Tarefa 4.1 — Age > 60
idosos = titanic[titanic['Age'] > 60]
print(f"\n-- Age > 60 -> {len(idosos)} passageiros (mostrando 5):")
print(idosos.head())

# Tarefa 4.2 — mulheres na 1ª classe
mulheres_1a = titanic[(titanic['Sex'] == 'female') & (titanic['Pclass'] == 1)]
print(f"\n-- Sex=='female' & Pclass==1 -> {len(mulheres_1a)} passageiras (mostrando 5):")
print(mulheres_1a.head())

# Tarefa 4.3 — Fare entre 50 e 100 com between()
faixa = titanic[titanic['Fare'].between(50, 100)]
print(f"\n-- Fare.between(50, 100) -> {len(faixa)} passageiros (mostrando 5):")
print(faixa[['Name', 'Fare']].head())

# Tarefa 4.4 — query(): Embarked=='C' e Survived==1
sobreviv_C = titanic.query("Embarked == 'C' and Survived == 1")
print(f"\n-- query Embarked=='C' & Survived==1 -> {len(sobreviv_C)} passageiros (mostrando 5):")
print(sobreviv_C[['Name', 'Sex', 'Pclass', 'Embarked', 'Survived']].head())


# =====================================================================
# DESAFIO 1 — Análise de Vendas
# =====================================================================
secao("DESAFIO 1 — Análise de Vendas")

vendas = pd.read_csv('/mnt/user-data/uploads/vendas.csv')

# Tarefa 1 — head(10) e info()
print("-- head(10) --")
print(vendas.head(10))
print("\n-- info() --")
vendas.info()

# Tarefa 2 — coluna total_venda
vendas['total_venda'] = vendas['quantidade'] * vendas['preco_unitario']
print("\n-- com total_venda --")
print(vendas.head())

# Tarefa 3 — Eletrônicos com total_venda > 1000
filtro = (vendas['categoria'] == 'Eletrônicos') & (vendas['total_venda'] > 1000)
elet_top = vendas[filtro]
print(f"\n-- Eletrônicos & total_venda > 1000 -> {len(elet_top)} linhas:")
print(elet_top)

# Tarefa 4 — média de total_venda por cidade, desc
media_cidade = (vendas.groupby('cidade')['total_venda']
                      .mean()
                      .sort_values(ascending=False)
                      .round(2))
print("\n-- média de total_venda por cidade (desc) --")
print(media_cidade)


# =====================================================================
# DESAFIO 2 — Limpeza de Dados de RH
# =====================================================================
secao("DESAFIO 2 — Limpeza de Dados de RH")

func = pd.read_csv('/mnt/user-data/uploads/funcionarios.csv')
print("-- DataFrame original --")
print(func)

# Tarefa 1 — nulos por coluna
print("\n-- isnull().sum() --")
print(func.isnull().sum())

# Tarefa 2 — remover linhas com salário nulo; preencher idade com média do depto
antes = len(func)
func = func.dropna(subset=['salario']).copy()
print(f"\nLinhas removidas por salário nulo: {antes - len(func)}  (restaram {len(func)})")

# transform('mean') devolve uma Series do mesmo tamanho do DF, com a média do
# departamento de cada linha. Aí só preencher os NaN de idade com isso.
media_idade_dep = func.groupby('departamento')['idade'].transform('mean')
func['idade'] = func['idade'].fillna(media_idade_dep)
print("\n-- idade preenchida com média do departamento --")
print(func[['nome', 'departamento', 'idade']])

# Tarefa 3 — datetime + anos_empresa
func['data_admissao'] = pd.to_datetime(func['data_admissao'], errors='coerce')
hoje = pd.Timestamp.today().normalize()
func['anos_empresa'] = ((hoje - func['data_admissao']).dt.days / 365.25).round(2)
print("\n-- com anos_empresa --")
print(func[['nome', 'departamento', 'data_admissao', 'anos_empresa']])

# Tarefa 4 — > 5 anos de empresa E salário < média do departamento
media_sal_dep = func.groupby('departamento')['salario'].transform('mean')
mask = (func['anos_empresa'] > 5) & (func['salario'] < media_sal_dep)
candidatos = func[mask]
print(f"\n-- > 5 anos E salário < média do depto -> {len(candidatos)} funcionários --")
print(candidatos[['nome', 'departamento', 'salario', 'anos_empresa']])


# =====================================================================
# DESAFIO 3 — Consolidação de Estoque
# =====================================================================
secao("DESAFIO 3 — Consolidação de Estoque")

estoque = pd.read_csv('/mnt/user-data/uploads/estoque_atual.csv')
produtos = pd.read_csv('/mnt/user-data/uploads/produtos.csv')
vmensal = pd.read_csv('/mnt/user-data/uploads/vendas_mensal.csv')

print("-- estoque_atual --");      print(estoque)
print("\n-- produtos --");         print(produtos)
print("\n-- vendas_mensal --");    print(vmensal)

# Atenção: estoque tem o mesmo produto em vários armazéns (produto 2 está em SP
# e RJ; produto 5 em RJ e MG). E vendas_mensal tem várias linhas por produto
# (uma por mês). Para o "merge único" sem explodir o cruzamento, primeiro
# agregamos estoque por produto e vendas por produto.
estoque_prod = (estoque.groupby('produto_id', as_index=False)['quantidade']
                       .sum()
                       .rename(columns={'quantidade': 'quantidade'}))
vendas_prod = (vmensal.groupby('produto_id', as_index=False)['quantidade_vendida']
                      .sum())

# Tarefa 1 — merge dos 3 (left join no produtos para manter todos os produtos)
df = (produtos
      .merge(estoque_prod, on='produto_id', how='left')
      .merge(vendas_prod, on='produto_id', how='left'))
# Produtos sem estoque ou sem vendas viram NaN -> tratamos como 0
df[['quantidade', 'quantidade_vendida']] = df[['quantidade', 'quantidade_vendida']].fillna(0)

print("\n-- DataFrame consolidado --")
print(df)

# Tarefa 2 — colunas calculadas
df['custo_total_estoque'] = df['quantidade'] * df['preco_custo']
df['valor_venda_mes']     = df['quantidade_vendida'] * df['preco_custo'] * 1.5

print("\n-- com custo_total_estoque e valor_venda_mes --")
print(df[['nome', 'categoria', 'quantidade', 'quantidade_vendida',
          'preco_custo', 'custo_total_estoque', 'valor_venda_mes']])

# Tarefa 3 — alertas
estoque_zerado = df[df['quantidade'] <= 0]
estoque_insuf  = df[df['quantidade_vendida'] > df['quantidade']]

print(f"\n-- estoque <= 0 -> {len(estoque_zerado)} produto(s) --")
print(estoque_zerado[['nome', 'quantidade']] if len(estoque_zerado) else "  (nenhum)")

print(f"\n-- vendido > estoque (estoque insuficiente) -> {len(estoque_insuf)} produto(s) --")
print(estoque_insuf[['nome', 'quantidade', 'quantidade_vendida']])

# Tarefa 4 — resumo por categoria
# margem bruta estimada = valor_venda_mes - (quantidade_vendida * preco_custo)
#                       = quantidade_vendida * preco_custo * 0.5
df['margem_bruta'] = df['quantidade_vendida'] * df['preco_custo'] * 0.5
df['estoque_critico'] = df['quantidade'] < 10  # bool

resumo = df.groupby('categoria').agg(
    total_estoque=('quantidade', 'sum'),
    total_vendido=('quantidade_vendida', 'sum'),
    produtos_criticos=('estoque_critico', 'sum'),  # soma de bools = contagem de True
    margem_bruta_estimada=('margem_bruta', 'sum'),
).round(2)

print("\n-- resumo por categoria --")
print(resumo)