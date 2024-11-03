import pygame
pygame.init()
#global variables
screen=pygame.display.set_mode([500,500])
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,0)
screen.fill(white)
class Circle():
    def __init__(self,color,pos,rad,wid=0):
        self.color=color
        self.pos=pos
        self.rad=rad
        self.wid=wid
        self.scrn=screen
    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)
    
    def grow(self,x):
        self.rad+=x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

position=(300,300)
radius=40
wid=2
pygame.draw.circle(screen, red, position, radius, wid)
pygame.display.update()
blueCircle=Circle(blue,position,radius+60)
redCircle=Circle(red,position,radius+40)
yellowCircle=Circle(yellow,position,radius,5)
greenCircle=Circle(green,position,radius,20)

while True:
    for event in pygame.event.get():
        if (event.type==pygame.MOUSEBUTTONDOWN):
           blueCircle.draw()
           redCircle.draw()
           yellowCircle.draw()
           greenCircle.draw()
           pygame.display.update()

        elif (event.type==pygame.MOUSEBUTTONUP):
            blueCircle.grow(3)
            redCircle.grow(3)
            yellowCircle.grow(3)
            greenCircle.grow(3)









