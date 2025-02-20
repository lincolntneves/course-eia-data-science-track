

lista1 = list(range(1,6))

for n in range(0,5):
    print("Informe o número na posição ",n+1,":")
    lista1[n] = int(input())
    while lista1[n] <= 0:
        print("Informe um valor maior que zero!")
        lista1[n] = int(input())


for n in range(0,5):
    a = (lista1[n]/2)
    if (a - round(a)) == 0:
        print("O número da posição ",n+1,"da lista é par e igual a: ",lista1[n])
        
