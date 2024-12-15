    #Задание №1

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}\nАвтор: {self.author}\nГод издания: {self.year}"

book1 = Book("Gorod", "Lenin", 1869)
print(book1.get_info())

    #Задание №2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self,new_radius):
        self.radius = new_radius

circ = Circle(32)
print(circ.get_radius())
circ.set_radius(64)
print(circ.get_radius())
