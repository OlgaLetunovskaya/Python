#**Задание 3. Вложенные классы**
#1. В отдельном файле создайте класс `Address`.
#2. Класс должен содержать в себе поля:
#    - «индекс»,
#    - «город»,
#    - «улица»,
#    - «дом»,
#    - «квартира».
#3. В отдельном файле создайте класс `Mailing` (почтовое отправление).
#4. В классе должно быть 4 поля:
#    - `to_address` (тип данных `Address`),
#    - `from_address` (тип данных `Address`),
#    - `cost` (тип данных `число`),
#    - `track` (тип данных строка).
#5. Создайте файл `lesson_3_task_3.py`.
#6. Импортируйте классы `Address` и `Mailing`.
#7. В файле создайте экземпляр класса `Mailing`.
#8. Заполните поля класса адресами (`to_address` и `from_address`), трек-номером (`track`) и стоимостью (`cost`).
#9. Распечатайте в консоль отправление в формате: `Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.`.
#Все данные должны получаться из экземпляра `Mailing`.

from address import Address
from mailing import Mailing

to_address = Address("123456", "Moscow", "Main Street", "1", "fl 101")
from_address = Address("654321", "Saint Petersburg", "Second Street", "2", "fl 202")
cost = 100.50
track = "ABC123"

mailing = Mailing(to_address, from_address, cost, track)

print(f"Mailing {mailing.track} from {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} to {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.flat}. Cost {mailing.cost} rubles.")