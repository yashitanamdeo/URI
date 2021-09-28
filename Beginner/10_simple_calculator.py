code1, unit1, price1 = map(float,input().split())
code2, unit2, price2 = map(float,input().split())

amount = (unit1*price1) + (unit2*price2)

print("VALOR A PAGAR: R$", format(amount,".2f"))