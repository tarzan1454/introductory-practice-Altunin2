# Итоговая мини-программа: Анализ прайс-листа
# Студент: Алтунин Владислав
# Ознакомительная практика, 1 курс, 2 семестр
# Вариант 10

print("=" * 70)
print("АНАЛИЗ ПРАЙС-ЛИСТА")
print("=" * 70)

def calculate_average_price(prices):
    """Расчёт средней цены"""
    if len(prices) == 0:
        return 0
    return sum(prices) / len(prices)

def find_cheapest_product(products):
    """Поиск самого дешёвого товара"""
    cheapest = min(products, key=lambda x: x["price"])
    return cheapest["name"], cheapest["price"]

def find_most_expensive_product(products):
    """Поиск самого дорогого товара"""
    most_expensive = max(products, key=lambda x: x["price"])
    return most_expensive["name"], most_expensive["price"]

def count_above_average(prices, average):
    """Подсчёт товаров дороже среднего"""
    return sum(1 for price in prices if price > average)

def apply_markup(price, markup_percent):
    """Применение наценки"""
    return price * (1 + markup_percent / 100)

# Ввод данных
products = []
print("\nВведите товары (5-7 штук):")
print("Для каждого товара введите название и цену")
print("-" * 50)

for i in range(1, 8):
    print(f"\nТовар {i}:")
    name = input(f"  Название товара {i}: ")
    if name == "" or name.lower() == "стоп":
        break
    
    try:
        price = float(input(f"  Цена товара {i} (руб.): "))
        products.append({"name": name, "price": price})
    except ValueError:
        print("  Ошибка! Введите число. Пропускаем этот товар.")
        continue

if len(products) < 3:
    print("\n❌ Недостаточно товаров для анализа (нужно минимум 3)")
    exit()

# Получение списка цен
prices = [p["price"] for p in products]

# Анализ
average_price = calculate_average_price(prices)
cheapest_name, cheapest_price = find_cheapest_product(products)
most_expensive_name, most_expensive_price = find_most_expensive_product(products)
above_average_count = count_above_average(prices, average_price)

# Вывод результатов
print("\n" + "=" * 70)
print("РЕЗУЛЬТАТЫ АНАЛИЗА ПРАЙС-ЛИСТА")
print("=" * 70)

print("\n1. ИСХОДНЫЙ ПРАЙС-ЛИСТ:")
print("-" * 50)
for product in products:
    print(f"  {product['name']:<20} {product['price']:>10,.2f} руб.")

print(f"\n2. СТАТИСТИКА:")
print(f"   📊 Средняя цена: {average_price:,.2f} руб.")
print(f"   📉 Самый дешёвый товар: {cheapest_name} ({cheapest_price:,.2f} руб.)")
print(f"   📈 Самый дорогой товар: {most_expensive_name} ({most_expensive_price:,.2f} руб.)")
print(f"   🔼 Товаров дороже среднего: {above_average_count} из {len(products)}")

# Обновлённый прайс с наценкой 15%
markup = 15
print(f"\n3. ОБНОВЛЁННЫЙ ПРАЙС-ЛИСТ (наценка {markup}%):")
print("-" * 50)

updated_products = []
for product in products:
    new_price = apply_markup(product["price"], markup)
    updated_products.append({"name": product["name"], "price": new_price})
    print(f"  {product['name']:<20} {product['price']:>10,.2f} руб. → {new_price:>10,.2f} руб.")

# Дополнительный анализ
print("\n4. ВЫВОДЫ:")
if average_price > 10000:
    print("   💰 Премиальный сегмент — средняя цена выше 10 000 руб.")
elif average_price > 5000:
    print("   💵 Средний ценовой сегмент — средняя цена от 5 000 до 10 000 руб.")
else:
    print("   🛍️ Бюджетный сегмент — средняя цена ниже 5 000 руб.")

if cheapest_price < average_price * 0.5:
    print("   🎯 Есть товары значительно дешевле среднего — возможно, товары-локомотивы")
    
if most_expensive_price > average_price * 2:
    print("   👑 Есть товары-флагманы с ценой выше среднего более чем в 2 раза")

print("\n" + "=" * 70)
print("Анализ завершён! Прайс-лист обновлён с учётом наценки 15%")
print("=" * 70)