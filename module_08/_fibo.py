def caching_fibonacci():
    cache = {}  

    def fibonacci(n):
        # Перевірка, чи вже обчислене число знаходиться у кеші
        if n in cache:
            return cache[n]
        
        # Обчислення числа Фібоначчі
        if n <= 1:
            result = n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  
print(fib(15)) 