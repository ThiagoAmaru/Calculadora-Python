def soma(num1,num2):
    return num1+num2
def subtracao(num1,num2):
    return num1 - num2
def multiplicacao(num1,num2):
    return num1 * num2
def divisao(num1,num2):
    return num1 / num2

opcao=1

while opcao:
    print("CALCULADORA EM PYTHON \n")

    print("Para Somar digite          1")
    print("Para Subtrair digite       2")
    print("Para Multiplicar digite    3")
    print("Para Dividir digite        4")
    print("Se desejar sair, digite    0")

    opcao= int(input("Opção: "))
    if (opcao == 0):
        break
    valor1= int(input("Digite o primeiro valor: \n"))
    valor2= int(input("Digite o segundo valor: \n"))
    
    if (opcao == 1):
        print(f'O valor da soma dos valores {valor1} e {valor2} é igual a {soma(valor1,valor2)}')
    if (opcao == 2):
        print(f'O valor da subtracao dos valores {valor1} e {valor2} é igual a {subtracao(valor1,valor2)}')
    if (opcao == 3):
        print(f'O valor da multiplicacao dos valores {valor1} e {valor2} é igual a {multiplicacao(valor1,valor2)}')
    if (opcao == 4):
        print(f'O valor da divisao dos valores {valor1} e {valor2} é igual a {divisao(valor1,valor2)}')