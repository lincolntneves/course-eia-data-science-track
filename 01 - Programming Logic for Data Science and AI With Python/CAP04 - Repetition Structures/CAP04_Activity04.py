
val1 = 0
val2 = 0
while  val1 <= 10:
    val1 = int(input("Informe o primeiro valor maior que 10: "))
while val2 < (val1 * 10):
    val2 = int(input("Informe um valor no mínimo 10x maior que o primeiro: "))
print("O produto dos dois valores é: ", val1 * val2)
