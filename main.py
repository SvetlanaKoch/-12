money = input('Введите сумму, которую хотите положить под процент: ')
m = int(money)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} #Словарь
procent = list(per_cent.values()) #Лист из значений
TKB = round(procent[0]*m/100) #Округленные суммы по ставка
SKB = round(procent[1]*m/100)
VTB = round(procent[2]*m/100)
SBER = round(procent[3]*m/100)
deposit = [TKB, SKB, VTB, SBER] #лист уравнений
print(deposit)

max_deposit = max(deposit) #максиамальная сумма
print('Максимальная сумма, которую вы можете заработать - ', max_deposit)
