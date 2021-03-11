import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_HEIGHT = 480

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, yTest=None):
        super().__init__() #inherit from parent (aka sprite)
        
        self.image = pygame.Surface([10, 90])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        #draw paddle
        pygame.draw.rect(self.image, WHITE, [0, 0, 10, 90])
        
        #get rectangle object that has dimensions of img
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = SCREEN_HEIGHT//3 if yTest == None else yTest
        
    def up(self):
        if self.rect.y > 0:
            self.rect.y -= 10
        else:
            self.rect.y = 0
            
    def down(self):
        if self.rect.y < (SCREEN_HEIGHT - self.rect.height):
            self.rect.y += 10
        else:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            
    def moveBot(self, ball):
        paddleCenter = (self.rect.y + self.rect.height)/2

        if ball.rect.y < paddleCenter: # Move up
            self.up()
        
        if ball.rect.y > paddleCenter: # Move down
            self.down()
        