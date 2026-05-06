def gerar_boletins(dados):
    # 1) AGRUPAR NOTAS POR ALUNO E MATÉRIA
    # estrutura: { "Ana": { "Matematica": [8.5, 7.5, 4.0], "Fisica": [9.0, 8.0] }, ... }
    agrupado = {}

    for registro in dados:
        aluno = registro["aluno"]
        materia = registro["materia"]
        nota = registro["nota"]

        # se o aluno ainda não existe no dicionário, cria
        if aluno not in agrupado:
            agrupado[aluno] = {}

        # se a matéria ainda não existe para esse aluno, cria a lista de notas
        if materia not in agrupado[aluno]:
            agrupado[aluno][materia] = []

        # adiciona a nota à lista daquele aluno e daquela matéria
        agrupado[aluno][materia].append(nota)

    # 2) CALCULAR MÉDIAS POR MATÉRIA (DESCARTANDO AS PIORES NOTAS SE PRECISAR)
    boletins = {}
    medias_gerais = {}

    for aluno, materias in agrupado.items():
        medias_disciplinas = {}

        for materia, lista_notas in materias.items():
            # copiamos a lista para não alterar o agrupado original
            notas_para_media = lista_notas[:]

            # se tiver 3 ou mais provas, vamos removendo a pior até sobrar só 2
            while len(notas_para_media) > 2:
                pior_nota = min(notas_para_media)
                notas_para_media.remove(pior_nota)

            # agora calcula a média das notas restantes
            media = sum(notas_para_media) / len(notas_para_media)
            media = round(media, 2)  # 2 casas decimais
            medias_disciplinas[materia] = media

        # 3) MÉDIA GERAL DO ALUNO (média das médias das matérias)
        soma_medias = 0
        qtd_materias = 0

        for media_materia in medias_disciplinas.values():
            soma_medias += media_materia
            qtd_materias += 1

        if qtd_materias > 0:
            media_geral = round(soma_medias / qtd_materias, 2)
        else:
            media_geral = 0.0  # só por segurança

        medias_gerais[aluno] = media_geral

        # 4) STATUS DO ALUNO
        if media_geral >= 7.0:
            status = "Aprovado"
        elif media_geral >= 5.0:
            status = "Recuperacao"
        else:
            status = "Reprovado"

        # monta o boletim desse aluno
        boletins[aluno] = {
            "medias_disciplinas": medias_disciplinas,
            "media_geral": media_geral,
            "status": status
        }

    # 5) RANKING DA TURMA
    # cria uma lista de tuplas: [(nome, media_geral), ...]
    lista_medias = []
    for aluno, media_geral in medias_gerais.items():
        lista_medias.append((aluno, media_geral))

    # ordena pela média (decrescente) e, em empate, pelo nome (alfabético)
    lista_ordenada = sorted(lista_medias, key=lambda x: (-x[1], x[0]))

    ranking = [nome for nome, media in lista_ordenada]

    # 6) RETORNO NO FORMATO PEDIDO
    return {
        "boletins": boletins,
        "ranking": ranking
    }