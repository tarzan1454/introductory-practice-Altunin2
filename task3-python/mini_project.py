# Итоговая мини-программа: Калькулятор рентабельности
# Студент: Алтунин Владислав
# Ознакомительная практика, 1 курс, 2 семестр
# Вариант 1

print("=" * 60)
print("КАЛЬКУЛЯТОР РЕНТАБЕЛЬНОСТИ")
print("=" * 60)

def calculate_profit(revenue, costs):
    """Расчёт прибыли"""
    return revenue - costs

def calculate_profitability(profit, revenue):
    """Расчёт рентабельности в %"""
    if revenue == 0:
        return 0
    return (profit / revenue) * 100

def get_rating(profitability):
    """Оценка рентабельности"""
    if profitability > 20:
        return "высокая 📈"
    elif profitability >= 10:
        return "средняя ➡️"
    else:
        return "низкая 📉"

# Ввод данных
company_name = input("Введите название компании: ")
revenue = float(input("Введите выручку (руб.): "))
costs = float(input("Введите затраты (руб.): "))

# Расчёты
profit = calculate_profit(revenue, costs)
profitability = calculate_profitability(profit, revenue)
rating = get_rating(profitability)

# Вывод отчёта
print("\n" + "=" * 60)
print("ОТЧЁТ О РЕНТАБЕЛЬНОСТИ")
print("=" * 60)
print(f"Компания: {company_name}")
print(f"Выручка: {revenue:,.2f} руб.")
print(f"Затраты: {costs:,.2f} руб.")
print(f"Прибыль: {profit:,.2f} руб.")
print(f"Рентабельность: {profitability:.2f}%")
print(f"Оценка: {rating}")
print("=" * 60)

if profit > 0:
    print("✅ Компания прибыльна")
elif profit < 0:
    print("❌ Компания убыточна")
else:
    print("➖ Компания безубыточна")