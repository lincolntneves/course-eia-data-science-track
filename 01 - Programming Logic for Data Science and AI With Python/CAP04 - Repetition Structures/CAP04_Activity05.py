qtd = 0
soma = 0
produto = 1
val1 = int(input("Informe o valor 01: "))
val2 = int(input("Informe o valor 02: "))
val3 = int(input("Informe o valor 03: "))
val4 = int(input("Informe o valor 04: "))
val5 = int(input("Informe o valor 05: "))
for x in (val1, val2, val3, val4, val5):
    if x%2 == 0:
        qtd += 1
        soma = soma + x
        produto = produto * x
print("Temos ",qtd, " números pares.")
print("A soma deles é: ",soma)
print("O produto deles é: ",produto)
