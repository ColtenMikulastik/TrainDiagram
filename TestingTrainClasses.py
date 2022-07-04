import pygame
import os

# pygame window info
WIDTH, HEIGHT = 256, 256
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DART Test")

# clock fps
FPS = 10

# train assets
TRAIN_HOR_IMG = pygame.image.load(os.path.join("Assets", "MC", "MClr64.png"))
TRAIN_VER_IMG = pygame.transform.rotate(TRAIN_HOR_IMG, 90)

# Map asset
MAP_IMG = pygame.image.load(os.path.join("Assets", "Maps", "MAP.png"))

# so I'm going to create a class to store the pygame info so that I'm not confusing myself


class TrainDART:
    rect = pygame.Rect
    img = 0

    def __init__(self, x, y, tempimg):
        self.rect = pygame.Rect(x, y, 64, 64)
        self.img = tempimg


def draw_window(list_o_trains):
    WIN.blit(MAP_IMG, (0, 0))
    for train in list_o_trains:
        WIN.blit(train.img, (train.rect.x, train.rect.y))
    pygame.display.update()


def update(list_o_trains):
    for train in list_o_trains:
        train.rect.x += 1


def main():
    # clock fps stuff
    clock = pygame.time.Clock()

    # new class
    train_a = TrainDART(64, 256, TRAIN_HOR_IMG)

    # before going into the game loop I'm gonna load all the surfaces into a list
    function_lists = []
    for i in range(0, 256, 64):
        function_lists.append(TrainDART(0, i, TRAIN_HOR_IMG))

    run = True
    while run:
        # more clock stuff
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update(function_lists)
        draw_window(function_lists)
    pygame.quit()

main()