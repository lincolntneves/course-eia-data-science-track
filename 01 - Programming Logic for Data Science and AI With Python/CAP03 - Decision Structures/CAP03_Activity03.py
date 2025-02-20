num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))
if num1>num2:
    print("Ordem crescente: ", num2,", ", num1, ".")
elif num1<num2:
    print("Ordem crescente: ", num1,", ", num2, ".")
elif num1==num2:
    print("Os números são iguais!")
