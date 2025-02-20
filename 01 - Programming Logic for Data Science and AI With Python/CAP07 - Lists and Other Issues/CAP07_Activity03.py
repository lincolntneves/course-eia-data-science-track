
list1 = list(range(1,6))

for n in range(0, 5):
        print("Indique o número ",n+1,":")
        list1[n] = float(input())

from math import sqrt

for n in range(0, 5):
    print("A raíz quadrada do número ",n+1,"é: ",sqrt(list1[n]))
    if sqrt(list1[n])-round(sqrt(list1[n])) > 0:
        print("O número ",n+1,"é Real.")
    else:
        print("O número ",n+1,"é Inteiro.")

