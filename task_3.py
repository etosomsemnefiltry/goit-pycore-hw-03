'''
Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
Функція видаляє всі символи, крім цифр та символу '+'.
Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') та коли номер починається без коду (додається '+38').
Функція повертає нормалізований телефонний номер у вигляді рядка.
'''
import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number:str):
    # Убрать из номера все кроме + и цифр, привести к общему формату

    pattern = r'[^\+0-9]'
    phone_number = re.sub(pattern, '', phone_number)

    match phone_number[0]:
        case '0':
            phone_number = '+38' + phone_number
        case '3':
            phone_number = '+' + phone_number
        case '8':
            phone_number = '+3' + phone_number
            
    return phone_number

correct_numbers = []
for number in raw_numbers:
    correct_numbers.append(normalize_phone(number))

print (correct_numbers)