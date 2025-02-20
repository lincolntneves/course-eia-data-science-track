
qtd = 1

while qtd < 2:
    print("Digite um valor > ou = a 2:")
    qtd = int(input("Quantos números ira trabalhar? "))

list1 = list(range(1, qtd+1))

for n in range(0, qtd):
             print("Informe o número",n+1,"dos números escolhidos:")
             list1[n] = int(input())
    
print("A soma do primeiro e do último número é: ",list1[0]+list1[qtd-1])
print("O produto do primeiro e segundo número informado é: ",list1[0]*list1[1])
