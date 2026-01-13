# Задание 1.5: Классы
# Напиши класс Student:
# Конструктор принимает имя и оценку
# Метод study() выводит "{имя} учится"
# Метод get_grade() возвращает оценку
# Создай двух студентов и используй их методы.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def study(self):
        print(f"I'm here! My name is {self.name}")

    def get_grade(self):
        return self.grade  

student1 = Student("Biba", 35)
student2 = Student("Boba", 53)

print(student1.name)
print(student2.grade)

student1.get_grade()
student2.study()