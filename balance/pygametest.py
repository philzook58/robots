import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640,480))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
points = [(100,100), (150,200), (200,100)]

 
while (True):

   # check for quit events
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();

   # erase the screen
   screen.fill(white)

   # draw the updated picture

   #updatePoints(points)  # changes the location of the points
   pygame.draw.lines(screen,black,False,points,1)  # redraw the points

   # update the screen
   pygame.display.update()