#Calculadora em Python para praticar


#Funcoes utilizadas:

#retorna insere dois valores e retorna operacao correspondente
def soma(num1,num2):
    return num1+num2
def subtracao(num1,num2):
    return num1 - num2
def multiplicacao(num1,num2):
    return num1 * num2
def divisao(num1,num2):
    return num1 / num2

opcao=1

#laco de repeticao que sera encerrado quando o quando o comando break for chamado
while opcao:
    print("CALCULADORA EM PYTHON \n")

    print("Para Somar digite          1")
    print("Para Subtrair digite       2")
    print("Para Multiplicar digite    3")
    print("Para Dividir digite        4")
    print("Se desejar sair, digite    0\n")

#input para selecionar a operacao e introduzir os dois valores utilizados na operacao
    opcao= int(input("Opção: \n"))
    if (opcao >= 5 or opcao < 0):
        print("Opção inválida, por favor digite uma das opções acima!")

    elif (opcao == 0):
        print("Encerrando")
        break

    else:

        valor1= float(input("Digite o primeiro valor: \n"))


        valor2= float(input("Digite o segundo valor: \n"))

#Formato como os resultados serão apresentados

        if (opcao == 1):
            print(f'O valor da soma dos valores {valor1} e {valor2} é igual a {soma(valor1,valor2)}')
        if (opcao == 2):
            print(f'O valor da subtracao dos valores {valor1} e {valor2} é igual a {subtracao(valor1,valor2)}')
        if (opcao == 3):
            print(f'O valor da multiplicacao dos valores {valor1} e {valor2} é igual a {multiplicacao(valor1,valor2)}')
        if (opcao == 4):
            print(f'O valor da divisao dos valores {valor1} e {valor2} é igual a {divisao(valor1,valor2)}')

#Ainda falta adicionar:
#tratamento de excecao
#documentacao
#outras funcionalidades