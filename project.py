#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([650, 650])
x= 325
y=0

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
    #screen.fill((255, 255, 255))
    image=pygame.image.load(r'C:\Users\19086\Downloads\pygame downloads\space backround.jpg')
    screen.blit(image,(0,0))
                                
                            
    # Draw a solid white line in the middle of screen
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x,y,5,650))
    
    character1 = pygame.image.load(r'C:\Users\19086\Downloads\pygame downloads\spaceship1.png')
    screen.blit(character1,(465,570)) 
    
    pressed= pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -=1
    if pressed[pygame.K_DOWN]: y+=1
    if pressed[pygame.K_LEFT]: x -=1
    if pressed[pygame.K_RIGHT]: x+=1
    screen.blit(image,(0,0))
        

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

