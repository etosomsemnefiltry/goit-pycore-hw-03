'''
Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
'''
from datetime import datetime as dt, timedelta as td

# Пример списка пользователей
users = [
    {"name": "John Doe", "birthday": "1985.07.13"},
    {"name": "Jane Smith", "birthday": "1990.07.09"},
    {"name": "John Doe", "birthday": "1995.03.23"},
    {"name": "John Doe", "birthday": "1975.07.24"}
]

def get_upcoming_birthdays(users):
    # Вычисляем кого поздравить в следующий 7 дней и с выходных переносим праздник на будние
    today_day = dt.today().date()
    upcoming_birthdays = []
    
    for user in users:

        birth_date = dt.strptime(user['birthday'], "%Y.%m.%d").date()

        # Переменные для понимания, прошел день рождения или нет.
        month = True if birth_date.month == today_day.month  else False
        day = True if birth_date.day >= today_day.day else False

        # Точно ли ДР в этом месяце и еще не прошел.
        if month and day:
            # Нужно дату рождения сделать в нынешнем году
            birth_date = str(today_day.year) + '.' + str(birth_date.month) + '.' + str(birth_date.day)
            birth_date = dt.strptime(birth_date, "%Y.%m.%d").date()
            # Порядковый номер дня недели
            birth_weekday = dt.weekday(birth_date)
            add_days = 0
             
            # Если день рождение в субботу или воскресенье. Дни (0-6)
            if birth_weekday >=5:
                # Сколько дней нужно добавить к дате дня рождения, чтобы получить понедельник.
                add_days = int(7 - birth_weekday)
                # Соответственно меняем дату рождения
                birth_date = birth_date + td(days=add_days)
            
            # Нужно показывать только дни рождения в грядущие 7 дней. Сравниваем с 6, т.к. учитываем сегодняшний день
            if birth_date.day - today_day.day <= 6:
                # Запишем в словарь с предстоящими днями рождения
                upcoming_birthdays.append({'name': user['name'], 'congratulation_date': dt.strftime(birth_date, "%Y.%m.%d")})
           
    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)