# Задание 1.5: Классы
# Напиши класс Student:
# Конструктор принимает имя и оценку
# Метод study() выводит "{имя} учится"
# Метод get_grade() возвращает оценку
# Создай двух студентов и используй их методы.

class Student:
    def __intit__(self, name, grade):
        self.name = name
        self.grade = grade