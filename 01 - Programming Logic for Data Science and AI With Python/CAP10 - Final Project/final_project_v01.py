
#Final Project: Solution v1.0
#Data source: https://www.kaggle.com/datasets/heidarmirhajisadati/deutschebank-financial-performance

income = [4370861.07,9556428.76,7587945.48,6387926.36,2404167.76,2403950.68,
1522752.51,8795585.31,6410035.11,7372653.2,1185260.45,9729188.67,8491983.77,
2911052,2636424.7,2650640.59,3738180.19,5722807.88,4887505.17,3621062.26,
6506676.05,2255444.75,3629301.84,4297256.59,5104629.86,8066583.65,
2797064.04,5628109.95,6331731.12,1418053.71,6467903.67,2534717.11,
1585464.34,9539969.84,9690688.3,8275576.13,3741523.92,1879049.03,
7158097.24,4961372.44,2098344.11,5456592.19,1309496.69,9183883.62,
3329019.83,6962700.56,3805399.68,5680612.19,5920392.51,2663690.1]

first_digit = list(range(0, len(income)))
 
for n in range(0,len(income)):
    x = str(income[n])
    first_digit[n] = x[:1]

print(first_digit)

first_digit_count = [0,0,0,0,0,0,0,0,0]
first_digit_count_perc = [0,0,0,0,0,0,0,0,0]

for n in range(0, len(income)):
    if int(first_digit[n]) == 1:
        first_digit_count[0] += 1
    elif int(first_digit[n]) == 2:
        first_digit_count[1] += 1
    elif int(first_digit[n]) == 3:
        first_digit_count[2] += 1
    elif int(first_digit[n]) == 4:
        first_digit_count[3] += 1
    elif int(first_digit[n]) == 5:
        first_digit_count[4] += 1
    elif int(first_digit[n]) == 6:
        first_digit_count[5] += 1
    elif int(first_digit[n]) == 7:
        first_digit_count[6] += 1
    elif int(first_digit[n]) == 8:
        first_digit_count[7] += 1
    elif int(first_digit[n]) == 9:
        first_digit_count[8] += 1

digits = [1,2,3,4,5,6,7,8,9]
digits_perc = [30,17,12,9,7,6,5,5,4]

for n in range(0,9):
    first_digit_count_perc[n] = (first_digit_count[n] / sum(first_digit_count)) * 100
    if n + 1 == digits[n]:
        print("Digito ",digits[n],"Percentual esperado: ",digits_perc[n],"%")
        print("Percentual encontrado: ",round(first_digit_count_perc[n]),"%")
    if abs(digits_perc[n] - round(first_digit_count_perc[n])) > 1:
        print("Diferença Significativa!")     
   
    


