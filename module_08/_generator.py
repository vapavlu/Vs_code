import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'  # Регулярний вираз для пошуку чисел
    
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Певертаємо число у вигляді float

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total_sum = sum(numbers_generator)  # Обчислюємо загальну суму чисел, отриману від генератора
    return total_sum

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1200.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.05 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")