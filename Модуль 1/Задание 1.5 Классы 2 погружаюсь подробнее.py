# 9.1. Ресторан.
# Создайте класс Restaurant. 
# Его метод __init__() должен содержать два атрибута: restaurant_name и cuisine_type. 
# Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(), 
# который выводит сообщение о том, что ресторан открыт.
class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

# метод describe_restaurant(), который выводит два атрибута
    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name}')
        print(f'We have {self.cuisine_type} cuisine')
        
    def open_restaurant(self):
        print(f'Restaurant is OPEN')

Rest1 = Restaurant("Ololosh", "russian")
Rest2 = Restaurant("Trololosh", "oriental")


Rest1.describe_restaurant()
Rest1.open_restaurant()

Rest2.describe_restaurant()
Rest2.open_restaurant()


# Создайте класс Car.
# Его метод __init__() должен содержать два атрибута: car_brand и car_color.
# Создайте метод describe_car(), который выводит два атрибута, и метод start_engine(), 
# который выводит сообщение о том, что двигатель запущен.
# Создайте два экземпляра класса и вызовите все методы.

class Car:
    def __init__(self,car_brand, car_color):
        self.car_brand = car_brand
        self.car_color = car_color
    
# Создайте метод describe_car(), который выводит два атрибута
    def describe_car(self):
        print(f'Car brand is {self.car_brand}')
        print(f'car color is {self.car_color}')

# метод start_engine()
    def start_engine(self):
        if self.car_brand == 'Lada':
            print('You are dead')
        else:
            print('Engine wrum-wrum')

Car1 = Car('Lada', 'red')
Car2 = Car('Vulva','Pink')

Car2.describe_car()
Car2.start_engine()


Car1.describe_car()
Car1.start_engine()



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Депозит {amount}. Новый баланс: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Вывод {amount}. Новый баланс: {self.balance}")
        else:
            print("Недостаточно средств")
    
    def get_balance(self):
        return self.balance


account = BankAccount("Иван", 1000)
account.deposit(500)      
account.withdraw(200)     
print(account.get_balance()) 
