valor = ''
def adicao (valor1, valor2):
    return valor1 + valor2
def subtracao (valor1, valor2):
    return valor1 - valor2
def multiplicacao (valor1, valor2):
    return valor1 * valor2
def divisao (valor1, valor2):
    if valor2 == 0:
        return "Erro: Divisão por zero"
    return valor1 / valor2
def calculadora(valor1, valor2, operacao):
    if operacao in ('+', 'adicao', 'adição'):
        resultado = adicao(valor1, valor2)
    elif operacao in ('-', 'subtracao', 'subtração'):
        resultado = subtracao(valor1, valor2)
    elif operacao in ('*', 'multiplicacao', 'multiplicação'):
        resultado = multiplicacao(valor1, valor2)
    elif operacao in ('/', 'divisao', 'divisão'):
        resultado = divisao(valor1, valor2)
    else:
        resultado = "Operação inválida"
    return resultado

saida = 's'
while saida.lower() == 's':
    valor1 = float(input("Digite o primeiro número: "))
    valor2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou nome): ")
    resultado = calculadora(valor1, valor2, operacao)
    print("Resultado da operação: ", resultado)
    saida = input("Deseja continuar? (S/N): ")