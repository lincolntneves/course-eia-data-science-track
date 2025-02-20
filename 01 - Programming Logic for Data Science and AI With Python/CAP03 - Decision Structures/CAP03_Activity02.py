ano = int(input("Qual o ano de nascimento? "))
from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano
if idade > 18:
    print("Idade de alistamento.")
else:
    print("Não está na idade de alistamento.")
