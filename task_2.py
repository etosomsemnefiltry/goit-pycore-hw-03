'''
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з 
числами, що випали випадковим чином та в певному діапазоні під час чергового тиражу. 
Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати 
набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий 
набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні 
бути унікальні.
'''

import random as r

# Будущие аргументы для запуска функции
min = 1
max = 999
quantity = 5

def get_numbers_ticket(min:int=1, max:int=49, quantity:int=5):
    # Генериурем список случайных уникальных чисел согласно заданным аргументам

    if min < 1: return 'Число min должно быть больше нуля'
    if max > 1000: return 'Число max должно быть менее 1000'

    res = set()

    # Крутим цикл, пока не наберем заданное количество уникальных чисел
    # Уникальность задаем набором set()
    while len(res) < quantity:
        res.add(r.randrange(min, max))

    return sorted(res)

print(get_numbers_ticket(min,max,quantity))