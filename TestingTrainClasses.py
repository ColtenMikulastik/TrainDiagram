import pygame
import os

# pygame window info
WIDTH, HEIGHT = 256, 256
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DART Test")

# clock fps
FPS = 5

# train assets
TRAIN_HOR_IMG = pygame.image.load(os.path.join("Assets", "MC", "MClr64.png"))
TRAIN_VER_IMG = pygame.transform.rotate(TRAIN_HOR_IMG, 90)

# station Block
STATION_NO_VER_IMG = pygame.image.load(os.path.join("Assets", "Station", "Stationupdono.png"))
STATION_NO_HOR_IMG = pygame.transform.rotate(STATION_NO_VER_IMG, 90)
STATION_YES_VER_IMG = pygame.image.load(os.path.join("Assets", "Station", "Stationupdoyes.png"))
STATION_YES_HOR_IMG = pygame.transform.rotate(STATION_YES_VER_IMG, 90)

# Map asset
MAP_IMG = pygame.image.load(os.path.join("Assets", "Maps", "MAP.png"))

# so I'm going to create a class to store the pygame info so that I'm not confusing myself


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


def draw_window(list_o_trains, list_o_stations, dart_map):
    # draw map
    WIN.blit(dart_map.img, (0, 0))
    # draw trains
    for train in list_o_trains:
        WIN.blit(train.img, (train.rect.x, train.rect.y))
    # draw stations
    for station in list_o_stations:
        WIN.blit(station.img, (station.rect.x, station.rect.y))
    # update my display
    pygame.display.update()


def update(list_o_trains, list_o_stations, dart_map):
    # loop through trains and do stuff to them
    for train in list_o_trains:
        train.rect.x += train.velocity
        if train.rect.x >= (WIDTH - 64) or (train.rect.x == 0):
            train.velocity = train.velocity * (-1)
        # loop through stations for collision stuff
        for station in list_o_stations:
            if train.rect.x == station.rect.x and train.rect.y == station.rect.y:
                station.is_occupied = True
                station.img = STATION_YES_HOR_IMG
            else:
                station.is_occupied = False
                station.img = STATION_NO_HOR_IMG


def main():
    # clock fps stuff
    clock = pygame.time.Clock()

    # before going into the game loop I'm gonna load all the surfaces into a list
    train_list = []
    station_list = []
    dart_map = MapDART(MAP_IMG)

    # add elements to the list
    train_list.append(TrainDART(0, 95, TRAIN_HOR_IMG))
    station_list.append(StationDART(0, 95, STATION_NO_HOR_IMG))
    station_list.append(StationDART(192, 95, STATION_NO_HOR_IMG))

    # game loop
    run = True
    while run:
        # more clock stuff
        clock.tick(FPS)
        # check for window being closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update(train_list, station_list, dart_map)
        draw_window(train_list, station_list, dart_map)
    pygame.quit()

main()