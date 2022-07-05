import pygame
import os

# new map stuff feature:
# change background to map image
#   -load map asset and other station assets (done)
#   -change the placement of stuff in the window (done)
# Change the behaviour of the train

# first create a window
WIDTH, HEIGHT = 256, 256
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DART Test")

# add the icon for the game
ICON = pygame.image.load(os.path.join("Assets", "MC", "MCdiR64.png"))
pygame.display.set_icon(ICON)

# Clock to reduce frames
FPS = 10

# add our assets into pygame
# train block
TRAIN_HOR_IMG = pygame.image.load(os.path.join("Assets", "MC", "MClr64.png"))
TRAIN_VER_IMG = pygame.transform.rotate(TRAIN_HOR_IMG, 90)
# Road block
ROAD_HOR_IMG = pygame.image.load(os.path.join("Assets", "Roads", "Roadlr64.png"))
ROAD_VER_IMG = pygame.transform.rotate(ROAD_HOR_IMG, 90)
# station Block
STATION_NO_VER_IMG = pygame.image.load(os.path.join("Assets", "Station", "Stationupdono.png"))
STATION_NO_HOR_IMG = pygame.transform.rotate(STATION_NO_VER_IMG, 90)
STATION_YES_VER_IMG = pygame.image.load(os.path.join("Assets", "Station", "Stationupdoyes.png"))
STATION_YES_HOR_IMG = pygame.transform.rotate(STATION_YES_VER_IMG, 90)
# Map block
MAP_IMG = pygame.image.load(os.path.join("Assets", "Maps", "MAP.png"))

VEL = 64


# update function
def update(train_rect, keypressed):
    if keypressed[pygame.K_LEFT] and train_rect.x > 0:
        train_rect.x -= VEL
    if keypressed[pygame.K_RIGHT] and train_rect.x < (WIDTH - 64):
        train_rect.x += VEL


# display function
def display(train_rect):
    # we want to draw map in background so... yeah
    WIN.blit(MAP_IMG, (0, 0))

    # two not one but two stations
    WIN.blit(STATION_NO_HOR_IMG, (0, 95))
    WIN.blit(STATION_NO_HOR_IMG, (194, 95))
    # draw the train
    WIN.blit(TRAIN_HOR_IMG, (train_rect.x, train_rect.y))
    pygame.display.update()


def main():
    # clock stuff for fps
    clock = pygame.time.Clock()

    # before the game loop load in assets, like the train's rect
    train_rect = pygame.Rect(0, 95, 64, 64)
    # main game loop
    run = True
    while run:
        # using the clock obj to set ticks
        clock.tick(FPS)

        # input
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
        keypressed = pygame.key.get_pressed()

        # update
        update(train_rect, keypressed)
        # display stuff
        display(train_rect)
    # quit the game
    pygame.quit()


if __name__ == "__main__":
    main()
