idade = int(input("Informe a idade em anos:"))
escolaridade = int(input("Informe a escolaridade: \n1 - para ensino fundamental, \n2 - para ensino médio \n3 - para ensino superior \n"))
if (escolaridade == 3) or (escolaridade == 2 and idade > 60):
    print("Habilitado")
else:
    print("Não habilitado")

