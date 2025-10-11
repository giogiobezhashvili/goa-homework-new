from turtle import *


width(7)
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

  
    #door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60,120)
pendown()
 
color("blue")
begin_fill()
right(60)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
end_fill()

penup()
goto(140,120) 
pendown()

color("blue")
begin_fill()
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
end_fill()

exitonclick(2)