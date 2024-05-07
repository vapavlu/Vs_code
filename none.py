def total_salary():
    try:
        with open("path/to/salary_file.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_salary = 0
            for line in lines:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
            average_salary = total_salary / len(lines)
            return total_salary, average_salary
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return None  # Повертаємо None у випадку, якщо виникає яка-небудь помилка

result = total_salary()
if result is not None:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print("Щось пішло не так. Перевірте вхідні дані.")
