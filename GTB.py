#galaga tractor beam code

import pygame #bring in pygame library
pygame.init #initialize pygame
pi = 3.1415
screen = pygame.display.set_mode((800, 800)) #create game screen
pygame.display.set_caption("galaga beam") #window title

#load alien ship image
alienShip = pygame.image.load("boss.jpg")
while(True):
    screen.fill((0,0,0))#clear the screen
    #draw alien ship
    screen.blit(alienShip, (210, 180))
    pygame.display.flip()
    
    
    #top arc
    pygame.draw.arc(screen, (5, 100, 200), (200, 200, 100, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)


    #second arc
    pygame.draw.arc(screen, (50, 200, 100), (190, 230, 120, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (5, 100, 200), (180, 260, 140, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (50, 200, 100), (170, 290, 160, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (5, 100, 200), (160, 320, 180, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (50, 200, 100), (150, 350, 200, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (5, 100, 200), (140, 380, 220, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (50, 200, 100), (130, 410, 240, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (5, 100, 200), (120, 440, 260, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (50, 200, 100), (110, 470, 280, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (5, 100, 200), (100, 500, 300, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

    pygame.draw.arc(screen, (50, 200, 100), (90, 530, 320, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(200)

