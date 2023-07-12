import pygame
import random
from button import Button

pygame.init()

scr_width = 800
scr_height = 600

screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Brick Breaker")

# The colors of the objects in the game
bkgrd_color = (200, 200, 200)
ball_color = (50, 40, 255)
paddle_color = (80, 50, 30)
brick_color = [(200, 50, 80), (45, 80, 240), (46, 235, 70),
               (150, 50, 180), (230, 170, 80), (60, 230, 220), (180, 210, 80)]

class Bricks():
    # Declare global variables
    global screen
    global scr_width
    global scr_height
    global brick_color
    
    def __init__(self):
        self.rows = 7
        self.rows_bricks = 9
        self.length = int(scr_width*0.8)//self.rows_bricks
        self.width = 40
        self.spacing = 4
        self.cordinates = []
        self.random_color = []
        
        for i in range(10, self.rows*(self.width), self.width):
            for j in range(int(scr_width*0.1), int(scr_width*0.9 - self.length)+1, self.length):
                self.cordinates.append([j, i])
                self.random_color.append(random.choice(brick_color))
                
    def show(self):
        num = 1
        color_index = 1
        for item in self.cordinates:
            # Draw each brick on the screen
            pygame.draw.rect(screen, brick_color[color_index-1], ((item[0], item[1]), (self.length-self.spacing, self.width-self.spacing)))
            num += 1
            if num > color_index * self.rows_bricks:
                color_index += 1
    
    def clone(self):
        # Create a copy of the brick coordinates
        brick_list = []
        for item in self.cordinates:
            brick_list.append(item)
        return brick_list
    
    def update(self, cordinate):
        # Update the screen by drawing a background color over a brick that has been broken
        pygame.draw.rect(screen, bkgrd_color, (cordinate, (self.length-self.spacing, self.width-self.spacing)))
        
class Paddle():
    # Declare global variables
    global screen
    global scr_height
    global scr_width
    global paddle_color
    
    def __init__(self, paddleX):
        self.paddleX = paddleX
        self.paddleY = int(scr_height*0.95)
        self.length = 120

    def show(self):
        thickness = 10
        # Draws the paddle(user) on the screen
        pygame.draw.rect(screen, paddle_color, ((self.paddleX, self.paddleY), (self.length, thickness)))

    def move_left(self):
        self.velocity = 15
        self.paddleX += -self.velocity

    def move_right(self):
        self.velocity = 15
        self.paddleX += self.velocity

    def stop(self):
        self.velocity = 0

    def boundaries(self):
        # Makes sure the paddles dont go outside the screen
        if self.paddleX >= (scr_width - self.length):
            self.paddleX = scr_width - self.length
        elif self.paddleX <= 0:
            self.paddleX = 0


#Importing libraries
#Custom import
#OOP
#Nested iterations
#Randomization
#Drawing 
#Clone 
#Update 
#Global variables
#Movement of objects
#Stopping objects
#Boundaries