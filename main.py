import pygame
import os

# for the map I am commiting to using a background fill, and then using an object to hold all of the road and
# member information

# first create a window
WIDTH, HEIGHT = 1792, 1024
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


# Train class
class TrainDART:
    rect = pygame.Rect
    velocity = 64
    img = 0
    is_ver = False

    def __init__(self, x, y, temp_img):
        self.rect = pygame.Rect(x, y, 64, 64)
        self.img = temp_img


# station class
class StationDART:
    rect = pygame.Rect
    img = 0
    is_occupied = False

    def __init__(self, x, y, temp_img):
        self.rect = pygame.Rect(x, y, 64, 64)
        self.img = temp_img


# map class
class MapDART:
    roads_list = []

    def __init__(self):
        # we can add road finding here
        for i in range(0, HEIGHT, 64):
            self.roads_list.append(pygame.Rect(WIDTH/2, i, 64, 64))


# update function
def update(train_list, station_list, dart_map):
    # loop through trains and do stuff to them
    for train in train_list:
        # check for vertical movement
        if train.is_ver:
            train.rect.y += train.velocity
            if train.rect.y >= (HEIGHT - 64) or (train.rect.y == 0):
                train.velocity = train.velocity * (-1)
        else:
            train.rect.x += train.velocity
            if train.rect.x >= (WIDTH - 64) or (train.rect.x == 0):
                train.velocity = train.velocity * (-1)
        # loop through stations for collision stuff
        for station in station_list:
            if train.rect.x == station.rect.x and train.rect.y == station.rect.y:
                station.is_occupied = True

    for station in station_list:
        if station.is_occupied:
            # this is going to need to be fixed
            station.img = STATION_YES_VER_IMG
        else:
            # this too
            station.img = STATION_NO_VER_IMG
        station.is_occupied = False


# display function
def display(train_list, station_list, dart_map):
    # we want to draw map in background so... yeah
    WIN.fill((229, 255, 230))
    for road in dart_map.roads_list:
        # ! need to figure out the road image stuff
        WIN.blit(ROAD_VER_IMG, (road.x, road.y))
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
    dart_map = MapDART()

    new_train = TrainDART(WIDTH/2, 0, TRAIN_VER_IMG)
    new_train.is_ver = True
    train_list.append(new_train)

    station_list.append(StationDART(WIDTH/2, HEIGHT/4, STATION_NO_VER_IMG))
    station_list.append(StationDART(WIDTH / 2, HEIGHT/2, STATION_NO_VER_IMG))
    station_list.append(StationDART(WIDTH / 2, (HEIGHT * 3) / 4, STATION_NO_VER_IMG))

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
