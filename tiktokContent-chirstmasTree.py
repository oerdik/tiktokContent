from turtle import *

speed(1)

#Mavi Arkaplan
penup()
goto(0,-250)
pendown()
color("lightskyblue")
begin_fill()
circle(250)
end_fill()

#Ağaç Gövdesi

penup()
goto(-15,-50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()

#Ağaç Konumu
y = -50
width = 240
height = 25

#Ağaç Yeşil Kısım
while width > 20:
    width = width - 30
    x = 0 - width / 2
    color("green")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
    
    y = y + height
    
#Yıldız
penup()
goto(-15,150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()

#Mutlu Yıllar
penup()
goto(-100,-150)
color("red")
write("MUTLU YILLAR", font=("Arial", 20,"bold"))

hideturtle()
