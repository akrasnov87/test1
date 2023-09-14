# подключаем специальную библиотеку для работы с "математикой" https://pythonworld.ru/moduli/modul-math.html
import math

def get_number(msg, is_float=True):
    while True: # требуем получение числа
        # в этой статье описан ввод пользовательских данных https://timeweb.com/ru/community/articles/prostoy-kalkulyator-na-python
        n = input(f"{msg}: ")
        # для некоторых математических операций требуется только целые числа
        if is_float:
            # таким образом проверяем, что число с плавающей точкой
            if n.replace('.', '', 1).isdigit():
                return float(n)
        else:
            if n.isdigit():
                return int(n)

def select_operation():
    # будем спрашивать номер операции

    # в этой статье описан ввод пользовательских данных https://timeweb.com/ru/community/articles/prostoy-kalkulyator-na-python
    while True:
        print(f'''Введите номер операции:
1 - Сложение
2 - Вычитание
3 - Деление
4 - Умножение
5 - Факториал''')
        
        n = input() # получаем, то что ввёл пользователь
  
        if n.isdigit():
            return int(n)
        else:
            print("Неверный номер операции")

while True:
    operation = select_operation() # получение номера операции

    if operation <= 3: # это условие для операций, где требутся два числа
        a = get_number("Первое число", is_float=False)
        b = get_number("Второе число", is_float=False)

        if operation == 1:
            print(f'{a} + {b} =', a + b)
        elif operation == 2:
            print(f'{a} - {b} =', a - b) 
        elif operation == 3:
            if b == 0:
                print("Деление на ноль запрещено")
            else:
                print(f'{a} / {b} =', a / b)

    elif operation == 5:
        a = get_number("Введите целове число", is_float=False) # тут специально указываем, что можно использовать только целое число
        print(f'{a}! =', math.factorial(a))
    else:
        print("Операция не найден")

    print()