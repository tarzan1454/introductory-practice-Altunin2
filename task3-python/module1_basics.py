# Модули Python
# Модуль 1: Переменные, типы данных, ввод/вывод
# Студент: Алтунин Владислав
# Ознакомительная практика, 1 курс, 2 семестр

print("=" * 50)
print("МОДУЛЬ 1: ПЕРЕМЕННЫЕ И ТИПЫ ДАННЫХ")
print("=" * 50)

# Упражнение 1: Карточка сотрудника
print("\n1. Карточка сотрудника")
name = "Владислав Алтунин"
age = 18
salary = 50000.0
is_working = True
print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Зарплата: {salary} руб.")
print(f"Работает: {is_working}")

# Упражнение 2: Приветствие
print("\n2. Приветствие")
user_name = input("Введите имя сотрудника: ")
user_city = input("Введите город: ")
print(f"Сотрудник {user_name} работает в городе {user_city}")

# Упражнение 3: Стоимость заказа
print("\n3. Стоимость заказа")
price = float(input("Цена товара: "))
quantity = int(input("Количество: "))
total = price * quantity
print(f"Итого: {total} руб.")

# Упражнение 4: Доход по вкладу
print("\n4. Доход по вкладу")
deposit = float(input("Сумма вклада: "))
rate = float(input("Годовая ставка (%): "))
income = deposit * (rate / 100)
print(f"Доход за год: {income:.2f} руб.")

# Упражнение 5: Конвертер валюты
print("\n5. Конвертер валюты")
usd_rate = float(input("Курс доллара: "))
rub_amount = float(input("Сумма в рублях: "))
usd_amount = rub_amount / usd_rate
print(f"Сумма в долларах: {usd_amount:.2f} USD")

print("\n" + "=" * 50)
print("Модуль 1 завершён!")
print("=" * 50)