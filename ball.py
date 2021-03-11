import pygame
from random import randint, random 

BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

class Ball(pygame.sprite.Sprite):
    def __init__(self, xTest=None, yTest=None, vel=[]):
        super().__init__() #inherit from parent (aka sprite)
        
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        #draw ball
        pygame.draw.rect(self.image, WHITE, [0, 0, 10, 10])
        
        #declare rect object that has dimensions of img
        self.rect = self.image.get_rect()
        
        self.rect.x = SCREEN_WIDTH//2 if xTest == None else xTest
        self.rect.y = SCREEN_HEIGHT//2 if yTest == None else yTest
        
        self.vel = [randint(3,4), randint(-4, 4)] if len(vel) == 0 else vel
        
        self.xTest = xTest
        self.yTest = yTest
        self.velTest = vel
        
        goLeft = random()
        if goLeft > 0.5:
            self.vel[0] *= -1
            if len(self.velTest) > 0:
                self.velTest[0] *= -1
        
    def reset(self):
        #set x-loc
        self.rect.x = SCREEN_WIDTH//2 if self.xTest == None else self.xTest
            
        #Set y-loc
        self.rect.y = SCREEN_HEIGHT//2 if self.yTest == None else self.yTest
            
        #Set velocity 
        self.vel = [randint(3,4), randint(-4, 4)] if len(self.velTest) == 0 else self.velTest
            
        #make ball go a direction
        goLeft = random()
        if goLeft > 0.5:
            self.vel[0] *= -1
            if len(self.velTest) > 0:
                self.velTest[0] *= -1
    
    def wallCollision(self):
        #check if hitting top or bottom
        if self.rect.y < self.rect.height or self.rect.y > (SCREEN_HEIGHT - self.rect.height):
            self.vel[1] *= -1
        
        #check for goal
        if self.rect.x < self.rect.width or self.rect.x > (SCREEN_WIDTH + self.rect.width):
            self.reset();
           
    def move(self):
        self.wallCollision()
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
        
    def hitPlayer(self, player):
        if self.rect.x <= (player.rect.x + player.rect.width) and self.rect.x >= player.rect.x :
            if self.withinPaddleHeight(player):
                self.rect.x = player.rect.x + player.rect.width 
                self.vel[0] *= -1
    
    def hitBot(self, bot):
        if (self.rect.x + self.rect.width) >= bot.rect.x and self.rect.x <= (bot.rect.x + bot.rect.width):
            if self.withinPaddleHeight(bot):
                self.rect.x = bot.rect.x - self.rect.width
                self.vel[0] *= -1
            
    def withinPaddleHeight(self, paddle):
        b = self.rect.y + self.rect.height
        return b >= paddle.rect.y and b <= (paddle.rect.y + paddle.rect.height)
    
    
        