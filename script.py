per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вашего депозита: '))
print('Ваш депозит', str(money), 'рублей')
print('Текущие ставки банка ТКБ:', per_cent['ТКБ'], '%')
print('Текущие ставки банка СКБ:', per_cent['СКБ'], '%')
print('Текущие ставки банка ВТБ:', per_cent['ВТБ'], '%')
print('Текущие ставки банка СБЕР:', per_cent['СБЕР'], '%')
deposit = []
deposit_TKB = int((per_cent['ТКБ'] * money / 100))
deposit_SKB = int((per_cent['СКБ'] * money / 100))
deposit_VTB = int((per_cent['ВТБ'] * money / 100))
deposit_SBER = int((per_cent['СБЕР'] * money / 100))
deposit = [deposit_TKB, deposit_SKB, deposit_VTB, deposit_SBER]
inverse = [(value, key) for key, value in per_cent.items()]
print('Максимальный доход за год по депозиту составит', max(deposit), 'рублей в банке', max(inverse)[1])


