#Import Pygame
import pygame, sys

# Game Clock
mainClock = pygame.time.Clock()
from pygame.locals import *

#Initiates Pygame
pygame.init()

#Display game name in top bar of window
pygame.display.set_caption('Space PvP')

#Size of game screen
screen = pygame.display.set_mode((720, 720))
 
font = pygame.font.SysFont(None, 40)

class cordinate():
    def __init__(self, xCord, yCord):
        self.xCord = xCord
        self.yCord = yCord

#class called projectiles to hold the bullets that
#will come out of the ship
class projectiles(object):
    def __init__(self, bulletX,bulletY,bulletRadius,bulletColor, bulletVelocity):
        self.bulletX=bulletX
        self.bulletY=bulletY
        self.bulletRadius=bulletRadius
        self.bulletColor=bulletColor
        self.bulletVelocity=8

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
        if spaceship1Cordinate.yCord <= 5:
            spaceship1Cordinate.yCord = 5
        spaceship1Cordinate.yCord -=4
    if pressed[pygame.K_DOWN]:
        if spaceship1Cordinate.yCord >= 650:
            spaceship1Cordinate.yCord = 650
        spaceship1Cordinate.yCord +=4
    if pressed[pygame.K_LEFT]:
        if spaceship1Cordinate.xCord <= 375:
            spaceship1Cordinate.xCord = 375
        spaceship1Cordinate.xCord -=4
    if pressed[pygame.K_RIGHT]:
        if spaceship1Cordinate.xCord >= 670:
            spaceship1Cordinate.xCord = 670
        spaceship1Cordinate.xCord +=4

#def player1_fire_bullet():


#def player2_fire_bullet():
    


def player2keyMove(spaceship2Cordinate):

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        if spaceship2Cordinate.yCord <= 5:
            spaceship2Cordinate.yCord = 5
        spaceship2Cordinate.yCord -=4
    if pressed[pygame.K_s]:
        if spaceship2Cordinate.yCord >= 650:
            spaceship2Cordinate.yCord = 650
        spaceship2Cordinate.yCord +=4
    if pressed[pygame.K_a]:
        if spaceship2Cordinate.xCord <= 0:
            spaceship2Cordinate.xCord = 0
        spaceship2Cordinate.xCord -=4
    if pressed[pygame.K_d]:
        if spaceship2Cordinate.xCord >= 295:
            spaceship2Cordinate.xCord = 295
        spaceship2Cordinate.xCord +=4


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():

    while True:
        #menu background and text
        screen.fill((255, 2, 255))
        image=pygame.image.load(r'.\intro background.jpg')
        screen.blit(image,(0,0))
        draw_text('Space PvP - Main Menu', font, (255, 255, 255), screen, 200, 20)
        mx, my = pygame.mouse.get_pos()


        #button rectangle position
        button_1 = pygame.Rect(260, 100, 200, 50)
        button_2 = pygame.Rect(260, 200, 200, 50)

        #button click to main or credits screen
        if button_1.collidepoint((mx, my)):
            if click:
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                credits()

        #button rectangle color        
        pygame.draw.rect(screen, (0, 0, 255), button_1)
        pygame.draw.rect(screen, (0, 0, 255), button_2)
        
        #draw text ontop of button
        draw_text('Play', font, (255, 255, 255), screen, 330, 110)
        draw_text('Credits', font, (255, 255, 255), screen, 310, 212)
        
 
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
    screen = pygame.display.set_mode([720, 720])
    x= 365
    y=0
    spaceship1Cordinate = cordinate(530, 390)
    spaceship2Cordinate = cordinate(170, 390)
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
        image=pygame.image.load(r'.\space backround resize.jpg')
        screen.blit(image,(0,0))
                                    
        # Draw a solid white line in the middle of screen
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x,y,5,720))

        character1 = pygame.image.load(r'.\spaceship1.png')
        screen.blit(character1,(spaceship1Cordinate.xCord,spaceship1Cordinate.yCord)) 

        character2 = pygame.image.load(r'.\spaceship2.png')
        screen.blit(character2,(spaceship2Cordinate.xCord,spaceship2Cordinate.yCord))

        player1keyMove(spaceship1Cordinate)
        player2keyMove(spaceship2Cordinate)

        #Flip the display
        pygame.display.flip()


#Pressing esc will Return to main menu        
        fontesc = pygame.font.SysFont(None, 20)
        draw_text('Press "esc" for main menu.', fontesc, (255, 255, 255), screen, 20, 20)
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