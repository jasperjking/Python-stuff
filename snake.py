import pygame
pygame.init()

WIDTH, HEIGHT = 700, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

GREY = (40, 40, 40)

def draw_window():
    WIN.fill(GREY)
    
    pygame.display.update()

def main():
    
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window()


if __name__ == "__main__":
    main()