valor_tot_manutencao = float(input("Informe o valor total da manutenção: "))
imposto_serv = float(input("Informe o percentual de imposto de servições: "))
imposto_prod = float(input("Informe o percentual de imposto de produto: "))
vl_imposto_serv = (imposto_serv/100) * valor_tot_manutencao
vl_imposto_prod = (imposto_prod/100) * valor_tot_manutencao
valor_manutencao = valor_tot_manutencao - vl_imposto_serv - vl_imposto_prod
print("O total a ser pago no imposto de serviços é: R$", vl_imposto_serv)
print("O total a ser pago no imposto de produto é: R$", vl_imposto_prod)
print("O valor a ser pago pela manutenção é de: R$", valor_manutencao)
