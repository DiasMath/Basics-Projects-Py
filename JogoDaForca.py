import random

lista_animais = [
    'leão', 'elefante', 'tigre', 'zebra', 'girafa',
    'rinoceronte', 'hipopótamo', 'macaco', 'jacaré', 'cobra',
    'coruja', 'pinguim', 'golfinho', 'tubarão', 'peixe',
    'leopardo', 'gorila', 'panda', 'lobo', 'tartaruga'
]

lista_objetos = [
    'cadeira', 'mesa', 'sofá', 'computador', 'televisão',
    'celular', 'livro', 'caneta', 'relógio', 'carro',
    'bicicleta', 'óculos', 'chave', 'laptop', 'fotografia',
    'óculos', 'mochila', 'telefone', 'câmera', 'violão'
]

lista_comidas = [
    'pizza', 'hamburguer', 'sushi', 'salada', 'lasanha',
    'macarrão', 'chocolate', 'sanduíche', 'sorvete', 'frutas',
    'hummus', 'kebab', 'panqueca', 'taco', 'batata',
    'sopa', 'queijo', 'bolo', 'pão', 'churrasco'
]


temas = {
    'animais': lista_animais,
    'objetos': lista_objetos,
    'comidas':lista_comidas
}

print("****************************")
print("Bem Vindo ao Jogo Da Forca!")
print("****************************")

print("\nEscolha o tema para jogar: ")
print(list(temas.keys()))
input_tema = input("\nTema Escolhido: ")

def SortearPalavra(tema_escolhido):
    if tema_escolhido in temas:
        tema = temas[tema_escolhido] 
        palavra_escolhida = random.choice(tema)
        return palavra_escolhida


def ExibirPalavraOculta(palavra_escolhida, letras_corretas):
    palavra_oculta = ""
    for letra in palavra_escolhida:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta


def IniciarJogo():
    palavra_a_adivinhar = SortearPalavra(input_tema)

    letras_corretas = []
    tentativas = 0 
    max_tentativas = 6

    while tentativas < max_tentativas:
        palavra_oculta = ExibirPalavraOculta(palavra_a_adivinhar, letras_corretas)
        print(f"Palavra: {palavra_oculta}")

        input_tentativa = input("Digite uma letra: ").lower()

        if input_tentativa in letras_corretas:
            print(f"Voce ja tentou a letra '{input_tentativa}'. Tente novamente")
            continue

        if input_tentativa in palavra_a_adivinhar:
            letras_corretas.append(input_tentativa)
            print(f"Boa! A letra '{input_tentativa}' esta na palavra.\n")
            continue    
        else:
            print(f"Ops! A letra '{input_tentativa}' nao esta na palavra.")
            tentativas += 1
            print(f"Suas Tentativas: {tentativas} (Maximo 6)\n")
            

        if set(letras_corretas) == set(palavra_a_adivinhar):
            print(f"Parabens! Voce adivinhou a palavra '{palavra_a_adivinhar}'!")
            return
    else:
        print(f"Voce atingiu o numero maximo de tentativas. A palavra era: {palavra_a_adivinhar}")
        return


IniciarJogo()