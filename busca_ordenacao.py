def busca_sequencial(registros, codigo):
    comparacoes = 0

    for posicao in range(len(registros)):
        comparacoes += 1

        if registros[posicao]["codigo"] == codigo:
            return posicao, comparacoes

    return -1, comparacoes

def ordenar_insercao(registros, chave):
    lista = registros[:]

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j][chave] > atual[chave]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista
