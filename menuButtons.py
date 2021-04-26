#Import Pygame
import pygame, sys

# Game Clock
mainClock = pygame.time.Clock()
from pygame.locals import *

#Initiates Pygame
pygame.init()

#Display game name in top bar of window
pygame.display.set_caption('Space Fighters')

#Size of game screen
screen = pygame.display.set_mode((650, 650))
 
font = pygame.font.SysFont(None, 20)

class cordinate():
    def __init__(self, xCord, yCord):
        self.xCord = xCord
        self.yCord = yCord

#class called projectiles to hold the bullets that
#will come out of the ship
class projectiles(object):
    def __init__(self, x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.velocity=8

    def draw(win):
        pygame.draw.circle(win,self.color(self.x,self.y), self.radius)

#These are the credits 
def credits():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Credits:', font, (255, 255, 255), screen, 20, 20)
        draw_text('Adam', font, (255, 255, 255), screen, 250, 160)
        draw_text('Sergius', font, (255, 255, 255), screen, 250, 180)
        draw_text('Zach', font, (255, 255, 255), screen, 250, 200)
        draw_text('Press "esc" for main menu.', font, (255, 255, 255), screen, 20, 560)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        

        pygame.display.update()
        mainClock.tick(60)
 

def player1keyMove(spaceship1Cordinate):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        spaceship1Cordinate.yCord -=4
    if pressed[pygame.K_DOWN]:
        spaceship1Cordinate.yCord +=4
    if pressed[pygame.K_LEFT]:
        spaceship1Cordinate.xCord -=4
    if pressed[pygame.K_RIGHT]:
        spaceship1Cordinate.xCord +=4

def player2keyMove(spaceship2Cordinate):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        spaceship2Cordinate.yCord -=4
    if pressed[pygame.K_s]:
        spaceship2Cordinate.yCord +=4
    if pressed[pygame.K_a]:
        spaceship2Cordinate.xCord -=4
    if pressed[pygame.K_d]:
        spaceship2Cordinate.xCord +=4

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():

    while True:

        screen.fill((0,0,0))
        draw_text('Space Fighters - Main Menu', font, (255, 255, 255), screen, 240, 20)
        mx, my = pygame.mouse.get_pos()


# !!!!! Need to figure out how to move "Play" and "Credits" text over the botton and not under the button
        button_1 = pygame.Rect(230, 100, 200, 50)
        draw_text('Play', font, (255, 255, 255), screen, 170, 100)
        button_2 = pygame.Rect(230, 200, 200, 50)
        draw_text('Credits', font, (255, 255, 255), screen, 190, 200)


        if button_1.collidepoint((mx, my)):
            if click:
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                credits()
        pygame.draw.rect(screen, (0, 0, 255), button_1)
        pygame.draw.rect(screen, (0, 0, 255), button_2)
        
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

#This is the game 
def main():
    
    # Set up the drawing window
    screen = pygame.display.set_mode([650, 650])
    x= 325
    y=0
    spaceship1Cordinate = cordinate(465, 570)
    spaceship2Cordinate = cordinate(200, 570)
    # Run until the user asks to quit
    running = True
    while running:
        
        clock = pygame.time.Clock()
        
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                clock.tick(60)

        

        # set backround as image from the web
        screen.fill((255, 2, 255))
        image=pygame.image.load(r'.\space backround.jpg')
        screen.blit(image,(0,0))
                                    
        # Draw a solid white line in the middle of screen
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x,y,5,650))
        

        character1 = pygame.image.load(r'.\spaceship1.png')
        screen.blit(character1,(spaceship1Cordinate.xCord,spaceship1Cordinate.yCord)) 

        character2 = pygame.image.load(r'.\spaceship2.png')
        screen.blit(character2,(spaceship2Cordinate.xCord,spaceship2Cordinate.yCord))


        player1keyMove(spaceship1Cordinate)
        player2keyMove(spaceship2Cordinate)

        # Flip the display
        pygame.display.flip()


#Pressing esc will Return to main menu        
        draw_text('Press "esc" for main menu.', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False    
        pygame.display.update()
        mainClock.tick(60)

    
if __name__ == "__main__":
    main_menu()
    main()