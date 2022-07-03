import pygame
import os

# new map stuff feature:
# change background to map image
# place the stations at either corner
# place train on the tracks and move it around :^)

# first create a window
WIDTH, HEIGHT = 1000, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DART Test")

# add the icon for the game
ICON = pygame.image.load(os.path.join("Assets", "MC", "MCdiR64.png"))
pygame.display.set_icon(ICON)

# Clock to reduce frames
FPS = 10

# add our assets into pygame
TRAIN_HOR_IMG = pygame.image.load(os.path.join("Assets", "MC", "MClr64.png"))
ROAD_HOR_IMG = pygame.image.load(os.path.join("Assets", "Roads", "Roadlr64.png"))
VEL = 64


# update function
def update(train_rect, keypressed):
    if keypressed[pygame.K_LEFT] and train_rect.x > 0:
        train_rect.x -= VEL
    if keypressed[pygame.K_RIGHT] and train_rect.x < (WIDTH - 64):
        train_rect.x += VEL


# display function
def display(train_rect):
    WIN.fill((229, 255, 230))
    # drawing a road from left to right of the screen
    for i in range(0, WIDTH, 64):
        WIN.blit(ROAD_HOR_IMG, (i, 100))

    # draw the train
    WIN.blit(TRAIN_HOR_IMG, (train_rect.x, train_rect.y))
    pygame.display.update()


def main():
    # clock stuff for fps
    clock = pygame.time.Clock()

    # before the game loop load in assets, like the train's rect
    train_rect = pygame.Rect(64, 100, 64, 64)
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
