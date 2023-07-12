#importing of library
import pygame

pygame.init()
# Initialization of pygame 

#Set the size and color of the background screen
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))  


class Button():
    def __init__(self, screen, colorButton, colorText, cordinates=(0, 0), dimensions=(100, 100), text='Click Here', textSize=10):
        # Initialization of the Button class with the required parameters
        self.screen = screen
        self.colorButton = colorButton
        self.colorText = colorText
        self.X, self.Y = cordinates
        self.width, self.length = dimensions
        self.text = text
        self.textSize = textSize
    #Used to display the button on the screen
    def show(self):
       
        pygame.draw.rect(self.screen, self.colorButton, ((self.X, self.Y), (self.width, self.length)))
        font = pygame.font.Font('freesansbold.ttf', self.textSize)
        caption = font.render(self.text, True, self.colorText)
        self.screen.blit(caption, (int(self.X + self.width*0.05), int(self.Y + self.length*0.2)))
    #Function used to check if the mouse is over the button
    def isOverMouse(self):
        
        x, y = pygame.mouse.get_pos()
        if self.X < x < self.X + self.width and self.Y < y < self.Y + self.length:
            return True
        return False
    # Draws a colored rectangle on the screen
    def changeColor(self, changeColorButton, changeColorText):
        
        pygame.draw.rect(self.screen, changeColorButton, ((self.X, self.Y), (self.width, self.length)))
        font = pygame.font.Font('freesansbold.ttf', self.textSize)
        caption = font.render(self.text, True, changeColorText)
        self.screen.blit(caption, (int(self.X + self.width*0.05), int(self.Y + self.length*0.2)))


if __name__ == '__main__':
    # Create a button instance with specific parameters
    b = Button(screen, (80, 45, 200), (200, 250, 255), (200, 250), (100, 60), "PLAY", 30)
    state = 'original'

    while True:
        screen.fill((255, 255, 255))  #white background color
        b.show()  # Display the button on the screen

        for event in pygame.event.get():
            if b.isOverMouse() == True:
                state = 'changed'  # State changes when mouse is over the button
            elif b.isOverMouse() == False:
                state = 'original'  # When the mouse is not over the button the state should back to the original
            if event.type == pygame.QUIT:
                pygame.quit()  # If window is closed, the game stops

        if state == 'changed':
            b.changeColor((80, 240, 80), (14, 37, 100))  # Change button color when mouse is over button

        pygame.display.update()  # Update the display
