from datetime import datetime


def get_days_from_today(date_str):
    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return ("Invalid date format. Use YYYY-MM-DD")
    today = datetime.today()
    diff = (parsed_date - today).days
    return int(diff)

print(get_days_from_today("2023-10-01") ) # Example usage

import random

def get_numbers_ticket(min, max, quantity):
    number_set = set()

    if min >= 1 and max <= 1000 and (max - min) >= quantity:
        while len(number_set) < quantity:
            number_set.add(random.randint(min, max))
        print("Your lottery numbers are:", sorted(number_set))
    else:
        print("The conditions are not right, please, check it!", number_set)
    
get_numbers_ticket(1, 1000, 5)  # Example usage

import re
clean_phone_number = []
def normalize_phone(phone_number):
    for phone in phone_number:
        phone = re.sub(r'\D+', '', phone)
        
        if len(phone) == 10:
            phone = '+38' + phone
        elif len(phone) == 12 and phone.startswith('380'):
            phone = '+' + phone
        else:
            return "Invalid phone number format"

        clean_phone_number.append(phone)
    print("Нормалізовані номери телефонів для SMS-розсилки:", clean_phone_number)

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
normalize_phone(raw_numbers) # Example usage
