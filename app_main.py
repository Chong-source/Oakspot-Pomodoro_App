import pygame
pygame.init()

screen_width = 310
screen_height = 735

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('OAKSPOT')

# load background images
home_image = pygame.image.load('home_screen.png')
leaderboard_image = pygame.image.load('leaderboard.png')
planner_image = pygame.image.load('planner.png')
stats_image = pygame.image.load('stats.png')
map_image = pygame.image.load('study_spots.png')
timer_image = pygame.image.load('total_study.png')

# load button images
home_button = pygame.image.load('home_button.png')
leaderboard_button = pygame.image.load('leaderboard_button.png')
planner_button = pygame.image.load('planner_button.png')
stats_button = pygame.image.load('stats_button.png')
map_button = pygame.image.load('map_button.png')
timer_button = pygame.image.load('timer_button.png')

# set one of the images as the background
background = home_image
background_colour = (248, 214, 173)
window.fill(background_colour)

####################################################
# Buttons
####################################################


class Button:
    """ template for the buttons"""
    def __init__(self, image, x, y, type):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.type = type
        # Resize the image to fit within the button dimensions
        self.image = pygame.transform.scale(image, (self.width, self.height))

    def draw(self):
        # Call this method to draw the button on the screen
        # pygame.draw.rect(window, (9, 50, 45), (self.x, self.y, self.width, self.height), 0)
        window.blit(self.image, (self.x, self.y))

    def is_over(self, position):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < position[0] < self.x + self.width:
            if self.y < position[1] < self.y + self.height:
                return True

        return False


####################################################
# Game loop
####################################################


home = Button(home_button, 0, 685, 'home')
leaderboard = Button(leaderboard_button, 50, 685, 'leaderboard')
planner = Button(planner_button, 100, 685, 'planner')
stats = Button(stats_button, 150, 685, 'stats')
map = Button(map_button, 200, 685, 'map')
timer = Button(timer_button, 250, 685, 'timer')
buttons = [home, leaderboard, planner, stats, map, timer]


def draw_window():
    for button in buttons:
        button.draw()


run = True
while run:
    window.blit(background, (0, 0))
    draw_window()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        for button in buttons:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and button.is_over(pos):
                print(button.type, ' clicked')
                if button.type == 'home':
                    background = home_image
                elif button.type == 'leaderboard':
                    background = leaderboard_image
                elif button.type == 'planner':
                    background = planner_image
                elif button.type == 'stats':
                    background = stats_image
                elif button.type == 'map':
                    background = map_image
                else:
                    background = timer_image
            if event.type == pygame.MOUSEMOTION:
                if button.is_over(pos):
                    button.colour = (255, 0, 0)
                else:
                    button.colour = (0, 255, 0)

    # updates the visuals
    pygame.display.update()
