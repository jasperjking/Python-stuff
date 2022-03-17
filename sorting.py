import math as maths
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 1024, 512
WIN = pygame.display.set_mode((WIDTH + 50, HEIGHT + 50))
FPS = 60

GREY = (40, 40, 40)
WHITE = (255, 255, 255)

def draw_window(arr):
    WIN.fill(GREY)
    for i in range(len(arr)):
        pygame.draw.rect(WIN, WHITE, pygame.Rect(i + 25, HEIGHT - maths.floor(arr[i]) + 25, 1, arr[i]))
    
    pygame.display.update()

def bubblesort(arr):
    swapped = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]
            swapped = True
    return swapped

def selectionsort(arr, n):
    min = n
    for j in range(n + 1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    [arr[n], arr[min]] = [arr[min], arr[n]]

def insertionsort(arr, n):
    PositionOfNext = n + 1
    while PositionOfNext <= len(arr):
        Next = arr[PositionOfNext]
        Current = PositionOfNext
        while Current > n and Next > arr[Current + 1]:
            Current = Current + 1
            arr[Current -1] = arr[Current]
        arr[Current] = Next
        PositionOfNext = PositionOfNext - 1

    



def main():
    arr = []
    mode = "Insertion"
    for i in range(WIDTH):
        arr.append(i/2)

    random.shuffle(arr)
    n = 0

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        draw_window(arr)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        if mode == "Bubble":
            swapped = bubblesort(arr)
            if not swapped:
                random.shuffle(arr)
        elif mode == "Selection":
            selectionsort(arr, n)
            if n >= len(arr) - 1:
                random.shuffle(arr)
                n = 0
            else:
                n += 1
        elif mode == "Insertion":
            insertionsort(arr, n)





if __name__ == "__main__":
    main()