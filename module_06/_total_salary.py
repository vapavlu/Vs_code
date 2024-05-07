def total_salary(path):
        with open(path, 'r',encoding='utf-8') as file:
            lines = file.readlines()
            total_salary = 0
            for line in lines:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
            average_salary = total_salary / len(lines)
            return total_salary, average_salary
    

# чомусь цей код викликає помилку, ми з GPT вдвох не розуміємо чому
total, average = total_salary("C:\Users\Иван\Vs_code\salary_file.py")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")