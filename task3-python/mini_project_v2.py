# Итоговая мини-программа: Симулятор вклада
# Студент: Алтунин Владислав
# Ознакомительная практика, 1 курс, 2 семестр
# Вариант 2 (дополнительный)

print("=" * 70)
print("СИМУЛЯТОР ВКЛАДА СЛОЖНЫЙ ПРОЦЕНТ")
print("=" * 70)

def calculate_final_amount(capital, rate, years):
    """Расчёт итоговой суммы по сложному проценту"""
    return capital * ((1 + rate / 100) ** years)

def calculate_total_income(capital, final_amount):
    """Расчёт общего дохода"""
    return final_amount - capital

def format_currency(amount):
    """Форматирование денежной суммы"""
    return f"{amount:,.2f} руб."

# Ввод данных
print("\nВведите параметры вклада:")
initial_capital = float(input("Начальная сумма вклада (руб.): "))
interest_rate = float(input("Годовая процентная ставка (%): "))
years = int(input("Срок вклада (лет): "))

print("\n" + "=" * 70)
print("ТАБЛИЦА РОСТА ВКЛАДА ПО ГОДАМ")
print("=" * 70)

# Вывод таблицы по годам
print(f"{'Год':<6} {'Сумма на счёте':<20} {'Доход за год':<18} {'Всего доход':<18}")
print("-" * 70)

current_amount = initial_capital
for year in range(1, years + 1):
    previous_amount = current_amount
    current_amount = calculate_final_amount(initial_capital, interest_rate, year)
    yearly_income = current_amount - previous_amount
    total_income = current_amount - initial_capital
    
    print(f"{year:<6} {format_currency(current_amount):<20} "
          f"{format_currency(yearly_income):<18} {format_currency(total_income):<18}")

# Итоговый результат
print("=" * 70)
print("\nИТОГОВЫЙ ОТЧЁТ:")
print(f"Начальная сумма: {format_currency(initial_capital)}")
print(f"Процентная ставка: {interest_rate}%")
print(f"Срок вклада: {years} лет")
print(f"Итоговая сумма: {format_currency(current_amount)}")
print(f"Общий доход: {format_currency(current_amount - initial_capital)}")

# Дополнительный анализ
print("\nАНАЛИЗ:")
if current_amount > initial_capital * 2:
    print("✅ Ваш капитал увеличился более чем в 2 раза!")
elif current_amount > initial_capital * 1.5:
    print("👍 Хороший прирост капитала (более 50%)")
elif current_amount > initial_capital:
    print("✅ Доход получен, но можно поискать ставку выше")
else:
    print("⚠️ Вклад не принёс дохода (проверьте ставку)")

print("\n" + "=" * 70)
print("СОВЕТ: Чем дольше срок и выше ставка, тем сильнее эффект сложного процента!")
print("=" * 70)