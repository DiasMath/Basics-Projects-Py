moedas = {
    "dolar" : 0.20,
    "euro" : 0.19,
    "iene" : 30.13,
    "thai baht" : 7.25
}

def Conversor(valor, moeda_escolhida):
    if moeda_escolhida in moedas:
        moeda = moedas[moeda_escolhida]
        operacao = valor * moeda

        print(f"A conversao do valor: {valor} em real para {moeda_escolhida} eh de: {operacao} {moeda_escolhida}(s)")

    else:
        print(f"A moeda {moeda_escolhida} nao existe no dicionario.")

resposta = 's'
while resposta.lower() == 's':

    print("Moedas disponíveis:", list(moedas.keys()))

    valor = int(input("Digite o valor que deseja converter: "))
    input_moeda = input("Digite a moeda para conversao: ")

    Conversor(valor, input_moeda)

    resposta = input("\nDeseja fazer uma nova conversao? (s/n): ").lower()
    while resposta not in ('s','n'):
        print("Resposta invalida. Tente novamente.")
        resposta = input("\nDeseja fazer uma nova conversao? (s/n): ").lower()

