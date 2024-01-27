def BuscaBinaria(lista, valor):
    lista.sort()
    inicio = 0
    fim = len(lista) -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return f'O valor {valor} foi encontrado na posicao {meio}'
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return f'O valor {valor} nao foi encontrado na lista.'


entrada_usuario_lista = input("Digite uma lista separada por espaco: ")
entrada_usuario_valor = int(input("Digite o valor que voce dejesa procurar: "))
lista_numeros = [int(numero) for numero in entrada_usuario_lista.split()]

resultado = BuscaBinaria(lista_numeros, entrada_usuario_valor)
print(resultado)