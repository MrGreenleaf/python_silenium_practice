# Напиши функцию multiply(a, b), которая:
# Принимает два числа
# Возвращает их произведение
# Протестируй: multiply(5, 3) должна вернуть 15

# функция умножения а на б
def multiply(a, b):

    result =  a * b
    print(f"Result is {result}")

# не забывай сделать вызов функции
c = int(input ('Input a '))
d = int(input ('Input b '))
multiply(c, d)

# Напиши функцию greet(name):
# - Принимает имя (строка)
# - Возвращает "Привет, [имя]!"
# - Вызови функцию с разными именами

# Пример:
# greet("Алексей") → "Привет, Алексей!"
# greet("Катя") → "Привет, Катя!"

# Шаблон:
def greet(name):
    # твой код
    return(f"Hello, {name}")

print(greet("Алексей"))
print(greet("Катя"))


# Напиши функцию max_of_two(a, b):
# - Принимает 2 числа
# - Возвращает большее из них

# Пример:
# max_of_two(10, 5) → 10
# max_of_two(-1, 3) → 3

# НЕ используй встроенный max()!

def max_of_two(a, b):
    # твой код
    if a > b:
        return (f"Max is {a}")
    elif b > a:
        return (f"Max is {b}")
    else:
        return (f"They are equal, {a} and {b}")

print(max_of_two(10, 5))
print(max_of_two(-1, 3))
print(max_of_two(7, 7))


# Напиши функцию is_even(number):
# - Принимает число
# - Возвращает True если четное, False если нечетное

# Пример:
# is_even(4) → True
# is_even(7) → False

def is_even(number):
    # твой код
    return (number % 2) == 0

print(is_even(4))  # True
print(is_even(7))  # False
print(is_even(0))  # True

# Напиши функцию sum_digits(number): - нахуй, не за головоломками я пришел)
# - Принимает число (например 123)
# - Возвращает сумму цифр (1+2+3=6)

# Пример:
# sum_digits(123) → 6
# sum_digits(999) → 27
# sum_digits(5) → 5


# def sum_digits(number):
    # твой код (используй % и //)

# print(sum_digits(123))  # 6
# print(sum_digits(999))  # 27