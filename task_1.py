'''
Завдання 1

Створіть функцію get_days_from_today(date), 
яка розраховує кількість днів між заданою датою та поточною датою.

'''
import datetime as dt

date = input("Введите дату в формате YYYY-MM-DD ")

if not date: print('Вы ничего не ввели')

def get_days_from_today(date:str=''):
    # date - string РРРР-ММ-ДД
    try: 
        ask_date = dt.datetime.strptime(date, '%Y-%m-%d')
    except ValueError as e:
        return f'Что то пошло не так -> {e}'
    
    curr_date = dt.datetime.today()
    if curr_date < ask_date: return 'Дата должна быть меньше сегодняшней'
    res = curr_date - ask_date
    return int(res.total_seconds()/60/60/24)


print(get_days_from_today(date))