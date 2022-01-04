import pgzrun
import random


WIDTH = 650
HEIGHT = 400
blue = 150
blueforward = True
groundcolor = 0,0,139
floor = Rect ((0,580), (1000,20))
cubo= Actor("cubo",(90,200))

def draw():
    screen.fill((173,216,blue))
    screen.blit("spazio",(0,0))
    cubo.draw()



pgzrun.go()
