


lista1 = list(range(1,6))

for n in range(0,5):
    print("Digite um número inteiro para posição: ",n+1)
    lista1[n] = int(input())
    while lista1[n] < lista1[n-1]:
        print("Entrada inválida! Digite um número maior que o anterior!")
        lista1[n] = int(input())

print("Esses são os números escolhidos: ", lista1)

