#**Задание 4. Нарисуйте картинку**
#1. Создайте файл `lesson_3_task_4.py`.
#2. Скопируйте и запустите код:
#
#    ```python
#    from turtle import *
    
#    my_turtle = Turtle()
#   my_turtle.speed(0)
#    my_turtle.screen.setup(1200, 800)
#    
#    # Нарисовать квадрат
#    def draw_rect(t):
#        for x in range(0, 4):
#            t.right(90)
#            t.forward(100)
#    
#    # Рисует квадраты в цикле
#    for x in range(0, 360):
#        draw_rect(my_turtle)
#        my_turtle.right(1)
#    
#    # Необходимо, чтобы окно не закрывалось само, а только по клику
#    my_turtle.screen.exitonclick()
#    my_turtle.screen.mainloop()
#    
#    ```
    
#3. Изучите структуру кода  на предмет основных блоков.
#4. Изучите статьи:
#- «**Графика turtle черепашка в питон»:**  http://itrobo.ru/programmirovanie/python/grafika-turtle-cherepashka-v-piton.html
#- «****Черепаха (turtle) в python»:**** https://koddom.com/kodim/turtle-python/****.****
#1. Напишите код, который рисует изображение любого животного.
#2. Поделитесь скриншотом рисунка в чате с коллегами.

import turtle

# Create a turtle object
snake = turtle.Turtle()

# Set the turtle's speed
snake.speed(2)

# Draw the snake's body with zigzag teeth
for _ in range(6):
    snake.forward(30)
    snake.left(90)
    snake.forward(30)
    snake.right(90)

snake.right(90)
snake.forward(30)
snake.left(45)
snake.forward(30)    

# Hide the turtle
snake.hideturtle()

# Keep the window open
turtle.done()
snake.screen.exitonclick()
snake.screen.mainloop()