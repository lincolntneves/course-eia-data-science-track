salario_atual = float(input("Indique o salário atual: "))
reajuste = float(input("Indique o valor percentual do reajuste: "))
print("O salário reajustado é: R$", salario_atual * (1 + (reajuste / 100)))
