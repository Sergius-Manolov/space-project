#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import and initialize the pygame library
import pygame
pygame.init()

class cordinate():
    def __init__(self, xCord, yCord):
        self.xCord = xCord
        self.yCord = yCord


def keyMove(spaceshipCordinate):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        spaceshipCordinate.yCord -=1
    if pressed[pygame.K_DOWN]:
        spaceshipCordinate.yCord +=1
    if pressed[pygame.K_LEFT]:
        spaceshipCordinate.xCord -=1
    if pressed[pygame.K_RIGHT]:
        spaceshipCordinate.xCord +=1


def main():
# Set up the drawing window
    screen = pygame.display.set_mode([650, 650])
    x= 325
    y=0
    spaceshipCordinate = cordinate(465, 570)
    # Run until the user asks to quit
    running = True
    while running:

        clock= pygame.time.Clock()
        
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
        screen.blit(character1,(spaceshipCordinate.xCord,spaceshipCordinate.yCord)) 
        
        keyMove(spaceshipCordinate)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()