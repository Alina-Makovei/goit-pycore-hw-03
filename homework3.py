# 1

import datetime

def get_days_from_today(date: str) -> int:

    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    except ValueError:
        print("Invalid date. Please enter date in YYYY-MM-DD format.")
        return None

    date_today = datetime.datetime.today().date()
    delta = date_today - date

    return delta.days

# self-check:
# user_date = input("Enter date (YYYY-MM-DD): ")
# print(get_days_from_today(user_date))


# 2

import random

def get_numbers_ticket(min, max, quantity):

    if not (
    isinstance(min, int)
    and isinstance(max, int)
    and isinstance(quantity, int)
    and min >= 1
    and min < max <= 1000
    and 0 < quantity <= max - min + 1):
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    numbers = sorted(numbers)

    return numbers

# self-check:
# min_value = int(input("Enter minimum number: "))
# max_value = int(input("Enter maximum number: "))
# quantity = int(input("Enter quantity: "))
# lottery_numbers = get_numbers_ticket(min_value, max_value, quantity)
# print("Your lottery numbers:", lottery_numbers)

    
# 3

import re

def normalize_phone(phone_number):
    # Видалення зайвого
    phone = re.sub(r"[^\d+]", "", phone_number)

    # Перевірка коду країни
    if phone.startswith("+380"):
        return phone
    elif phone.startswith("380"):
        return "+" + phone
    else:
        return "+38" + phone

# Обробка прикладів з завдання
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

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# 4

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= 7:

            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# self-check
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.11.13"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
