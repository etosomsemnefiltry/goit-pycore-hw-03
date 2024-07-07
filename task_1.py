'''
Завдання 1

Створіть функцію get_days_from_today(date), 
яка розраховує кількість днів між заданою датою та поточною датою.

'''
import datetime as dt

# Get date from user
date = input("Введите дату в формате YYYY-MM-DD ")

# If empty entire
if not date: print('Вы ничего не ввели')

def get_days_from_today(date:str=''):
    # get difference between two dates
    # date - string РРРР-ММ-ДД
    try: 
        # Is we can get date from user in needed format
        ask_date = dt.datetime.strptime(date, '%Y-%m-%d')
    except ValueError as e:
        # Describe most expected error to user
        return f'Что то пошло не так -> {e}'
    
    # Get current date in similar format as user enter
    curr_date = dt.datetime.today()

    if curr_date < ask_date: return 'Дата должна быть меньше сегодняшней'
    res = curr_date - ask_date
    
    # Превращаем расчетные данные сразу в секунды и арифметикой перегоняем в дни.
    return int(res.total_seconds()/60/60/24) 

# run function
print(get_days_from_today(date))