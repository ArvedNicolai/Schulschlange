import turtle as t
from turtle import *

# edit this line to control where window appears
t.setup(width=500, height=500, startx=400, starty=400)

setposition(100, 100)
window = t.Screen()

laenge = 50

def south():
    t.setheading(180)
    t.forward(laenge)

def north():
    t.setheading(0)
    t.forward(laenge)
    
def west():
    t.setheading(270)
    t.forward(laenge)
    
def east():
    t.setheading(90)
    t.forward(laenge)

def A(k):
    if k>0:
        D(k-1)
        west()
        A(k-1)
        south()
        A(k-1)
        east()
        B(k-1)
    return

def B(k):
    if k>0:
        C(k-1)
        north()
        B(k-1)
        east()
        B(k-1)
        south()
        A(k-1)
    return

def C(k):
    if k>0:
        B(k-1)
        east()
        C(k-1)
        north()
        C(k-1)
        west()
        D(k-1)
    return

def D(k):
    if k>0:
        A(k-1)
        south()
        D(k-1)
        west()
        D(k-1)
        north()
        C(k-1)
    return

#ordnung = input("Gib' die Ordnung der Hilbert -Kurve an: ")
A(3)

window.exitonclick()