#**Задание 7. Вызов функций**
#1. Создайте файл lesson_1_task_7.py
#2. Создайте по одной функции на каждое действие (всего 10 функций):
#    1. Вывести в консоль 1
#    2. Вывести в консоль 2
#    3. Вывести в консоль 3
#    4. Вывести в консоль 4
#    5. Вывести в консоль 5
#    6. Вывести в консоль 6
#    7. Вывести в консоль 7
#    8. Вывести в консоль 8
#    9. Вывести в консоль 9
#    10. Вывести в консоль 0
#3. Вызовите объявленные функции в таком порядке, чтобы на экране отобразился номер 88005553535.

def func1():
    return 1
def func2():
    return 2 
def func3():
    return 3
def func4():
    return 4
def func5():
    return 5
def func6():
    return 6
def func7():
    return 7
def func8():
    return 8
def func9():
    return 9
def func0():
    return 0
result = str(func8()) + str(func8()) + str(func0()) + str(func0()) + str(func5()) + str(func5()) + str(func5()) + str(func3()) + str(func5()) + str(func3()) + str(func5())
print(result)
