def tempe(a, b):
    if a == "F":
        return b * 1.8 + 32
    elif a == "C":
        return (b - 32) / 1.8

temperatura = input("Esse é um conversor de temperatura:\nQuer converter de Celcius para Fahrenheit? Digite F\nQuer converter de Fahrenheit para Celsius? Digite C\nResposta:  ")
temperatura = temperatura.upper()

if temperatura == "F":
    nome = "Fahrenheit"
elif temperatura == "C":
    nome = "Celsius"

valor = float(input("Digite o valor da temperatura em " + nome + " que deseja converter: "))
resposta = tempe(temperatura, valor)

if temperatura == "F":
    nome_conv = "Celsius"
elif temperatura == "C":
    nome_conv = "Fahrenheit"

print("A temperatura de",valor, nome_conv, "será",resposta, nome,".")
