    # Задание №1

def greet(name):
    print(f"Приветствую, {name}")
greet("Пётр")

def square(number):
    print(number ** 2)
square(5)


def max_of_two(x, y):
    if x > y:
        print(x)
    else:
        print(y)
max_of_two(350, 480)

    # Задание №2

def describe_person(name, age=30):
    print(f"Имя {name}. Ему {age} лет.")
describe_person("Алексей")

    # Задание №3

def is_prime(b):
    a = 2
    while b % a != 0:
        a += 1
    if a == b:
        print("Число простое")
    else:
        print("Число составное")

is_prime(int(input("Введите число:")))