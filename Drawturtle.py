from turtle import Turtle, Screen 

timmy = Turtle()
myScreen = Screen()

timmy.speed(2)

for i in range (20) :
    timmy.circle(5*i)
    timmy.circle(-5*i)
    timmy.left(i)

myScreen.exitonclick()
