#**Задание 1. Создание класса**
#1. Создайте файл `user.py`.
#2. В файле объявите класс `User`.
#3. Объявите в классе конструктор.
#Конструктор должен принимать на вход 2 параметра:
#4. `first_name` — имя.
#5. `last_name` — фамилия.
#Помните, что все методы класса, включая конструктор, принимают первым параметром `self`.
#6. Создайте в классе 3 метода, которые печатают:
#    - имя,
#    - фамилию,
#    - имя и фамилию.
#7. Создайте файл `lesson_3_task_1.py`.
#8. Импортируйте в него класс `user`.
#9. Создайте новый экземпляр `User` и сохраните его в переменную `my_user`.
#10. Вызовите все методы у объекта в переменной `my_user

from user import User

my_user = User("Olga", "Letunovskaya")
my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()
