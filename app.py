import turtle
from time import sleep

def fel():
    y = tihi.ycor()
    tihi.sety(y+5)

def le():
    y = tihi.ycor()
    tihi.sety(y-5)

def bal():
    x = tihi.xcor()
    tihi.setx(x-5)

def jobb():
    x = tihi.xcor()
    tihi.setx(x+5)

def tihifel():
    y = viktor.ycor()
    viktor.sety(y+5)

def tihile():
    y = viktor.ycor()
    viktor.sety(y-5)

def tihibal():
    x = viktor.xcor()
    viktor.setx(x-5)

def tihijobb():
    x = viktor.xcor()
    viktor.setx(x+5)

def penup():
    tihi.penup()

def tavolsag():
    dx = tihi.xcor() - viktor.xcor()
    dy = tihi.ycor() - viktor.ycor()
    tav = (dx**2 + dy**2) ** 0.5    

    turtle.write(int(tav))

def torles():
    turtle.clear()
    


ablak = turtle.Screen()
ablak.setup(600,600)
ablak.bgcolor("lightgreen")

viktor = turtle.Turtle()
viktor.shape("turtle")
viktor.color("blue")
viktor.shapesize(3)
viktor.speed(5)

tihi = turtle.Turtle()
tihi.shape("turtle")
tihi.color("red")
tihi.shapesize(3)
tihi.speed(2)

ablak.listen()
ablak.onkeypress(fel, "Up")
ablak.onkeypress(le, "Down")
ablak.onkeypress(bal, "Left")
ablak.onkeypress(jobb, "Right")
ablak.onkeypress(penup, "m")
ablak.onkeypress(tavolsag, "e")
ablak.onkeypress(torles, "r")

ablak.onkeypress(tihifel, "w")
ablak.onkeypress(tihile, "s")
ablak.onkeypress(tihibal, "a")
ablak.onkeypress(tihijobb, "d")

ablak.mainloop()