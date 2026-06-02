# Модуль 3: Функции (def, параметры, return)
# Студент: Алтунин Владислав
# Ознакомительная практика, 1 курс, 2 семестр

print("=" * 60)
print("МОДУЛЬ 3: ФУНКЦИИ")
print("=" * 60)

# =====================================================
# Упражнение 1: calculate_profit() - расчёт прибыли
# =====================================================
print("\n1. Функция calculate_profit()")

def calculate_profit(revenue, costs):
    """Принимает выручку и затраты, возвращает прибыль"""
    return revenue - costs

# Тестируем с тремя разными парами
print(f"Прибыль (1000, 700): {calculate_profit(1000, 700)} руб.")
print(f"Прибыль (500, 600): {calculate_profit(500, 600)} руб.")
print(f"Прибыль (2000, 1500): {calculate_profit(2000, 1500)} руб.")

# =====================================================
# Упражнение 2: calculate_vat() - расчёт НДС
# =====================================================
print("\n2. Функция calculate_vat()")

def calculate_vat(price, vat_rate=20):
    """Принимает цену и ставку НДС (по умолчанию 20%), возвращает сумму налога"""
    return price * (vat_rate / 100)

print(f"НДС 20% от 1000 руб.: {calculate_vat(1000)} руб.")
print(f"НДС 10% от 1000 руб.: {calculate_vat(1000, 10)} руб.")
print(f"НДС 20% от 2500 руб.: {calculate_vat(2500)} руб.")

# =====================================================
# Упражнение 3: get_category() - категория бизнеса
# =====================================================
print("\n3. Функция get_category()")

def get_category(revenue):
    """Возвращает категорию бизнеса по выручке (в млн руб.)"""
    if revenue < 1:
        return "Микробизнес"
    elif revenue < 10:
        return "Малый бизнес"
    elif revenue < 100:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"

# Тестируем на 4 значениях
print(f"Выручка 0.5 млн → {get_category(0.5)}")
print(f"Выручка 5 млн → {get_category(5)}")
print(f"Выручка 50 млн → {get_category(50)}")
print(f"Выручка 200 млн → {get_category(200)}")

# =====================================================
# Упражнение 4: compound_interest() - сложный процент
# =====================================================
print("\n4. Функция compound_interest()")

def compound_interest(capital, rate, years):
    """Принимает капитал, ставку и срок, возвращает итоговую сумму"""
    return capital * ((1 + rate / 100) ** years)

print(f"1000 руб., ставка 10%, 3 года: {compound_interest(1000, 10, 3):.2f} руб.")
print(f"1000 руб., ставка 10%, 5 лет: {compound_interest(1000, 10, 5):.2f} руб.")
print(f"1000 руб., ставка 10%, 10 лет: {compound_interest(1000, 10, 10):.2f} руб.")

# =====================================================
# Упражнение 5: apply_discount() - применение скидки
# =====================================================
print("\n5. Функция apply_discount()")

def apply_discount(price, discount_percent):
    """Принимает цену и процент скидки, возвращает новую цену"""
    return price * (1 - discount_percent / 100)

# Список товаров
products = [
    {"name": "Ноутбук", "price": 50000},
    {"name": "Мышь", "price": 1500},
    {"name": "Клавиатура", "price": 3000},
    {"name": "Монитор", "price": 25000},
    {"name": "Наушники", "price": 4000}
]

discount = 15
print(f"Скидка {discount}%:")
for product in products:
    new_price = apply_discount(product["price"], discount)
    print(f"  {product['name']}: {product['price']} руб. → {new_price:.2f} руб.")

print("\n" + "=" * 60)
print("Модуль 3 завершён!")
print("=" * 60)