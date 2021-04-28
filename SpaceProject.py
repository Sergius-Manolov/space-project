#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import and initialize the pygame library
import pygame
pygame.init()

screen = pygame.display.set_mode([650, 650])
x= 325
y=0
image=pygame.image.load(r'.\space backround.jpg')

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity=8


class cordinate():
    def __init__(self, xCord, yCord):
        self.xCord = xCord
        self.yCord = yCord

    def draw(self,screen):
        screen.blit(character1,(spaceship1Cordinate.xCord,spaceship1Cordinate.yCord))
        screen.blit(character2,(spaceship2Cordinate.xCord, spaceship2Cordinate.yCord))

#class called projectiles to hold the bullets that
#will come out of the ship
class projectiles(object):
    def __init__(self, x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.velocity=8

    def drawBullet(self,screen):
        pygame.draw.circle(screen,self.color(self.x,self.y), self.radius)

def redrawGameWindow():
    bullets=[]
        #screen.blit(image(0,0))
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

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
    bullets = []
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        if len(bullets)<5:
            bullets.append(projectiles(30,20,8,(255,255,255)))
    if pressed[pygame.K_w]:
        spaceship2Cordinate.yCord -=4
    if pressed[pygame.K_s]:
        spaceship2Cordinate.yCord +=4
    if pressed[pygame.K_a]:
        spaceship2Cordinate.xCord -=4
    if pressed[pygame.K_d]:
        spaceship2Cordinate.xCord +=4

def main():
    bullets= []
# Set up the drawing window
    screen = pygame.display.set_mode([650, 650])
    x= 325
    y=0
    spaceship1Cordinate = cordinate(465, 570)
    spaceship2Cordinate = cordinate(200, 570)
    # Run until the user asks to quit
    running = True
    while running:

        clock= pygame.time.Clock()
        
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                clock.tick(60)
        for bullet in bullets:
            if bullet.bulletX < 650 and bullet.bulletX> 0:
                bullet.bulletX += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet))
        
        # set backround as image from the web
        screen.fill((255, 2, 255))
        image=pygame.image.load(r'.\space backround.jpg')
        #screen.blit(image,(0,0))
                                    
        # Draw a solid white line in the middle of screen
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x,y,5,650))
        

        character1 = pygame.image.load(r'.\spaceship1.png')
        screen.blit(character1,(spaceship1Cordinate.xCord,spaceship1Cordinate.yCord)) 


        character2 = pygame.image.load(r'.\spaceship2.png')
        screen.blit(character2,(spaceship2Cordinate.xCord,spaceship2Cordinate.yCord))


        player1keyMove(spaceship1Cordinate)
        player2keyMove(spaceship2Cordinate)
        redrawGameWindow()
        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()
# %%
