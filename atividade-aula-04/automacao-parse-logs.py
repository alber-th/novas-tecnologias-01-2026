
# logs = [
#    "2023-10-01 10:00:00 INFO User 105 logged in",
#    "2023-10-01 10:05:23 ERROR Database connection failed",
#    "2023-10-01 10:07:00 INFO User 105 requested /home",
#    "2023-10-01 10:15:00 WARNING Memory usage above 80%",
#    "2023-10-01 10:20:00 ERROR Timeout on API gateway",
#    "2023-10-01 10:22:00 INFO User 202 logged in"
# ]

def analisar_logs(lista_logs):
    contagem = {}
    for linha in lista_logs:
        partes = linha.split(" ")
        nivel = partes[2]  # INFO, ERROR, WARNING

        # se ainda não existe no dicionário, inicializa em 0
        if nivel not in contagem:
            contagem[nivel] = 0

        # incrementa
        contagem[nivel] += 1

    return contagem
