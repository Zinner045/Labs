
    # Задания №1,3

def reading(filename="example.txt", reading_mode='full'):
    try:
        file = open(filename, encoding='utf-8')
        if reading_mode == 'full':
            print(file.read())
        elif reading_mode == 'line':
            for line in file:
                print(line)
        else:
            print('Неверный ввод режима чтения. Доступны "full" или "line"')
    except FileNotFoundError:
        print('Ошибка: файл не найден')

reading(filename='example.txt', reading_mode='line')

    # Задание №2

def writing():
    user_input = input("Введите текст:")
    file = open('user_input.txt', mode='a', encoding='utf-8')
    file.write(user_input)

writing()