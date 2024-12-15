    #Задание №1

class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return self.password == password

user = UserAccount("X_Sanya338_X", "sanek587@gmail.com", "SanyaPro")
user.set_password("S@ny@Pro368")
print(user.check_password("Sany@Pro369"))
print(user.check_password("S@ny@Pro368"))

    #Задание №2

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{super().get_info()}, Тип топлива: {self.fuel_type}"

my_car = Car("Da", "Net", "GDE")
print(my_car.get_info())