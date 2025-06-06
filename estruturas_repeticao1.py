entrada_idade = 1

while entrada_idade != 0:
    try:
        entrada_idade = int(input("Digite um número qualquer ou 0 para sair: "))
        print("Número digitado:", entrada_idade)
    except ValueError:
        print("Por favor, digite um número válido.")