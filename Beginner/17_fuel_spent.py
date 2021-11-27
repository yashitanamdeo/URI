'''Problem Statement: https://www.beecrowd.com.br/judge/en/problems/view/1017'''

time_spent = int(input())
avg_speed = int(input())

total_fuel_spent = (time_spent * avg_speed) / 12

print(format(total_fuel_spent,".3f"))