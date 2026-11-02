def busca_sequencial(registros, codigo):
    comparacoes = 0

    for posicao in range(len(registros)):
        comparacoes += 1

        if registros[posicao]["codigo"] == codigo:
            return posicao, comparacoes

    return -1, comparacoes
