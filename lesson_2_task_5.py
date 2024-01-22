#**Задание 5. Месяц — сезон**
#1. Создайте файл lesson_2_task_5.py.
#2. Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает 
#название сезона, к которому относится этот месяц.
#Например, передаем 2, на выходе получаем «Зима».

def month_to_season(month):
   if month == 1 or month == 2 or month == 12:
        return "Зима"
   elif month == 3 or month == 4 or month == 5:
        return "Весна"
   elif month == 6 or month == 7 or month == 8:
        return "Лето"
   elif month == 9 or month == 10 or month == 11:
        return "Осень"
   else:
        return "Неверный номер месяца"    
print(month_to_season(int(input())))   