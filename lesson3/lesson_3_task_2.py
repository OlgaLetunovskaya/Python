#**Задание 2. Список объектов**
#1. Создайте файл `smartphone.py`.
#2. В файле объявите класс `Smartphone`.
#3. Объявите в классе конструктор.
#Конструктор должен принимать на вход следующие параметры:
#- марка телефона,
#- модель телефона,
#- абонентский номер (”+79…”).
#4. Создайте файл `lesson_3_task_2.py`.
#5. В файле объявите переменную `catalog`.
#6. Переменная хранит в себе список (`[]`).
#7. Наполните список пятью разными экземплярами класса `Smartphone`.
#8. Напишите цикл, который печатает весь каталог (список) в формате `<марка> - <модель>. <номер телефона>`.

from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 12", "+79111111111")
phone2 = Smartphone("Samsung", "Galaxy S21", "+79222222222")
phone3 = Smartphone("Google", "Pixel 5", "+79333333333")
phone4 = Smartphone("OnePlus", "8 Pro", "+79444444444")
phone5 = Smartphone("Xiaomi", "Mi 11", "+79555555555")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(phone.brand, phone.model, phone.phone_number)


    