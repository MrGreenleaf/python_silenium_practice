# Напиши цикл, который выведет все числа от 1 до 10.
# Потом напиши цикл, который выведет все элементы списка fruits = ["яблоко", "банан", "апельсин"].

i=1
while i <= 10:
    print(f"Number is {i}")
    i = i + 1

fruits = ['apple', 'banana', 'orange']
for fruits in fruits:
    print(f"The fruit is {fruits}")