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
FPS = 5

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

# classes
class TrainDART:
    rect = pygame.Rect
    velocity = 64
    img = 0

    def __init__(self, x, y, temp_img):
        self.rect = pygame.Rect(x, y, 64, 64)
        self.img = temp_img


class StationDART:
    rect = pygame.Rect
    img = 0
    is_occupied = False

    def __init__(self, x, y, temp_img):
        self.rect = pygame.Rect(x, y, 64, 64)
        self.img = temp_img


class MapDART:
    img = 0

    def __init__(self, temp_img):
        self.img = temp_img
        # we can add road finding here


# update function
def update(train_list, station_list, dart_map):
    # loop through trains and do stuff to them
    for train in train_list:
        train.rect.x += train.velocity
        if train.rect.x >= (WIDTH - 64) or (train.rect.x == 0):
            train.velocity = train.velocity * (-1)
        # loop through stations for collision stuff
        for station in station_list:
            if train.rect.x == station.rect.x and train.rect.y == station.rect.y:
                station.is_occupied = True
                station.img = STATION_YES_HOR_IMG
            else:
                station.is_occupied = False
                station.img = STATION_NO_HOR_IMG


# display function
def display(train_list, station_list, dart_map):
    # we want to draw map in background so... yeah
    WIN.blit(dart_map.img, (0, 0))

    # draw the trains
    for train in train_list:
        WIN.blit(train.img, (train.rect.x, train.rect.y))
    # draw the stations
    for station in station_list:
        WIN.blit(station.img, (station.rect.x, station.rect.y))

    pygame.display.update()


def main():
    # clock stuff for fps
    clock = pygame.time.Clock()

    # before going into the game loop I'm gonna load all the surfaces into a list
    train_list = []
    station_list = []
    dart_map = MapDART(MAP_IMG)

    train_list.append(TrainDART(0, 95, TRAIN_HOR_IMG))
    station_list.append(StationDART(0, 95, STATION_NO_HOR_IMG))
    station_list.append(StationDART(192, 95, STATION_NO_HOR_IMG))

    # main game loop
    run = True
    while run:
        # using the clock obj to set ticks
        clock.tick(FPS)

        # input
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
        # gonna remove this for now was sent to the update function
        # keypressed = pygame.key.get_pressed()

        # update
        update(train_list, station_list, dart_map)
        # display stuff
        display(train_list, station_list, dart_map)
    # quit the game
    pygame.quit()


if __name__ == "__main__":
    main()
