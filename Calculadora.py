num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
op = input("Digite a operacao desejada: ")

def Calculadora(num1,num2,op):
    if op == '+':
        op_escrita = 'soma'
        resultado = num1+num2
        textoResult = "mais"
    elif op == '-':
        op_escrita = 'subtracao'
        resultado = num1-num2
        textoResult = "menos"
    elif op == '*':
        op_escrita = 'multiplicacao'
        resultado = num1*num2
        textoResult = "vezes"
    elif op == '/':
        op_escrita = 'divisao'
        resultado = num1/num2
        textoResult = "dividido por"
    else:
        print("Resposta invalida. Tente novamente.")

    print(f'O resultado da {op_escrita} de {num1} {textoResult} {num2} eh: {resultado}')
Calculadora(num1,num2,op)
