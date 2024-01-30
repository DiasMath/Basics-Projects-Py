import random
import os

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


def TituloInicio():
    print("****************************")
    print("Bem Vindo ao Jogo Da Forca!")
    print("****************************")

    print("\nEscolha o tema para jogar: ")
    print(list(temas.keys()))


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

def VerificaConteudo(palavra_correta,letras_corretas):   
    conjunto_palavra_correta = set(palavra_correta)
    conjunto_letras_corretas = set(letras_corretas)

    if conjunto_palavra_correta.issubset(conjunto_letras_corretas):
        print(f"Parabens! Voce adivinhou a palavra '{palavra_correta}'!")
        return
    else:
        print(f"Voce atingiu o numero maximo de tentativas. A palavra era: {palavra_correta}")

        


def IniciarJogo():
    
    letras_corretas = []
    tentativas = 0 
    max_tentativas = 6
    letras_erradas = []

    input_tema =  input("\nTema Escolhido: \n")

    while input_tema not in (temas.keys()):
        print("Tema nao encontrado. Tente Novamente.")
        input_tema =  input("\nTema Escolhido: \n")
        
    palavra_a_adivinhar = SortearPalavra(input_tema)

    while tentativas < max_tentativas:

        palavra_oculta = ExibirPalavraOculta(palavra_a_adivinhar, letras_corretas)
        print(f"\nPalavra: {palavra_oculta}")

        input_tentativa = input("Digite uma letra: ").lower()

        if input_tentativa in palavra_a_adivinhar:
            letras_corretas.append(input_tentativa)
            print(f"Boa! A letra '{input_tentativa}' esta na palavra.\n") 
        else:
            print(f"\nOps! A letra '{input_tentativa}' nao esta na palavra.\n")
            

        if input_tentativa not in palavra_a_adivinhar and input_tentativa not in letras_erradas:
            tentativas += 1
            letras_erradas.append(input_tentativa)
            print(f"Tentativas: {letras_erradas}")
            print(f"Suas Tentativas: {tentativas} (Max 6)\n")
        else:
            print(f"Tentativas: {letras_erradas}")
            print(f"Voce ja tentou a letra '{input_tentativa}'. Tente novamente")
            


    while True:
        resposta = input("Deseja jogar novamente? (s/n)").lower()        
        if resposta == 's':
            Main()
        elif resposta == 'n':
            break
        else:
            print("Resposta invalida. Tente novamente.")
            continue



def Main():
    os.system('clear')
    print(TituloInicio())
    IniciarJogo()


Main()