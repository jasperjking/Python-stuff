import math as maths
import pygame
import random
import os
pygame.init()
pygame.display.set_caption("Sorting Algorithms")

WIDTH, HEIGHT = 1024, 512
WIN = pygame.display.set_mode((WIDTH + 50 + 150, HEIGHT + 50))
FPS = 60

NUMBER = 1024

GREY = (40, 40, 40)
WHITE = (255, 255, 255)
GREEN = (100, 200, 100)
BLUE = (100, 100, 200)

BUTTON_FONT = pygame.font.SysFont('Impact', 24)
MODE_FONT = pygame.font.SysFont('comicsans', 18)
MODE_FONT_2 = pygame.font.SysFont('comicsans', 14)

SHUFFLE_BUTTON = pygame.Rect(WIDTH + 75, HEIGHT - 25, 100, 50)
PAUSE_BUTTON = pygame.Rect(WIDTH + 75, HEIGHT - 100, 100, 50)
TOGGLE_BUTTON = pygame.Rect(WIDTH + 75, HEIGHT - 175, 100, 50)



def draw_window(arr, mode, sorted, sortedindex):
    WIN.fill(GREY)


    for i in range(len(arr)):
        pygame.draw.rect(WIN, WHITE, pygame.Rect(i * WIDTH//NUMBER + 25, HEIGHT - maths.floor(arr[i]) + 25, WIDTH//NUMBER, arr[i]))

    if sorted:
        for j in range(maths.floor(sortedindex)):
            pygame.draw.rect(WIN, GREEN, pygame.Rect(j * WIDTH//NUMBER + 25, HEIGHT - maths.floor(arr[j]) + 25, WIDTH//NUMBER, arr[j]))

    
    #shuffle button

    pygame.draw.rect(WIN, WHITE, SHUFFLE_BUTTON)
    pygame.draw.rect(WIN, BLUE, pygame.Rect(WIDTH + 77, HEIGHT - 23, 96, 46))

    shuffle_text = BUTTON_FONT.render("Shuffle", 1, WHITE)
    WIN.blit(shuffle_text, (WIDTH + 125 - shuffle_text.get_width()//2, HEIGHT - shuffle_text.get_height()//2))

    #pause button

    pygame.draw.rect(WIN, WHITE, PAUSE_BUTTON)
    pygame.draw.rect(WIN, BLUE, pygame.Rect(WIDTH + 77, HEIGHT - 98, 96, 46))

    pause_text = BUTTON_FONT.render("Pause", 1, WHITE)
    WIN.blit(pause_text, (WIDTH + 125 - pause_text.get_width()//2, HEIGHT - pause_text.get_height()//2 - 75))

    #toggle mode button

    pygame.draw.rect(WIN, WHITE, TOGGLE_BUTTON)
    pygame.draw.rect(WIN, BLUE, pygame.Rect(WIDTH + 77, HEIGHT - 173, 96, 46))

    toggle_text = BUTTON_FONT.render("Toggle", 1, WHITE)
    WIN.blit(toggle_text, (WIDTH + 125 - toggle_text.get_width()//2, HEIGHT - toggle_text.get_height()//2 - 150))

    #display of mode

    pygame.draw.rect(WIN, WHITE, pygame.Rect(WIDTH + 75, HEIGHT - 250, 100, 50))
    pygame.draw.rect(WIN, BLUE, pygame.Rect(WIDTH + 77, HEIGHT - 248, 96, 46))

    if mode == "Intelligent Design":
        mode_text_1 = MODE_FONT_2.render("Intelligent", 1, WHITE)
        mode_text_2 = MODE_FONT_2.render("Design", 1, WHITE)
        WIN.blit(mode_text_1, (WIDTH + 125 - mode_text_1.get_width()//2, HEIGHT - mode_text_1.get_height()//2 - 225 - 10))
        WIN.blit(mode_text_2, (WIDTH + 125 - mode_text_2.get_width()//2, HEIGHT - mode_text_2.get_height()//2 - 225 + 9))
    else:
        mode_text = MODE_FONT.render(mode, 1, WHITE)
        WIN.blit(mode_text, (WIDTH + 125 - mode_text.get_width()//2, HEIGHT - mode_text.get_height()//2 - 225))


    pygame.display.update()

def bubblesort(arr):

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]

def selectionsort(arr, n):
    min = n
    for j in range(n + 1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    [arr[n], arr[min]] = [arr[min], arr[n]]

def insertionsort(arr, n):
    PositionOfNext = len(arr) - 2 - n
    Next = arr[PositionOfNext] 
    Current = PositionOfNext
    while Current < len(arr) - 1 and Next > arr[Current + 1]:
        Current = Current + 1
        arr[Current -1] = arr[Current]
    arr[Current] = Next

def bogosort(arr):
    sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            sorted = False
    if not sorted:
        random.shuffle(arr)

def bozosort(arr):
    sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            sorted = False
    if not sorted:
        randindex1 = random.randint(0, len(arr) - 1)
        randindex2 = random.randint(0, len(arr) - 1)
        [arr[randindex1], arr[randindex2]] = [arr[randindex2], arr[randindex1]]

def grogosort(arr):
    indexes = []
    values = []
    for i in range(0, len(arr)):
        if arr[i] != (i+1)/2 * WIDTH//NUMBER:
            indexes.append(i)
            values.append(arr[i])
    random.shuffle(values)
    for i in range(len(values)):
        arr[indexes[i]] = values[i]


 





def main():
    arr = []
    mode = ["Insertion", "Bubble", "Selection", "Bogosort", "Bozosort", "Intelligent Design", "Gorosort"]
    modeindex = 0
    for i in range(1, NUMBER + 1):
        arr.append(i/2 * WIDTH//NUMBER)

    random.shuffle(arr)
    n = 0
    sorted = False
    sortedindex = 1
    paused = False
    run = True
    clock = pygame.time.Clock()
    while run:
        #clock.tick(FPS)
        draw_window(arr, mode[modeindex], sorted, sortedindex)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()
                if mousepress[0]:
                    mousepos = pygame.mouse.get_pos()
                    #shuffle button
                    if mousepos[0] < SHUFFLE_BUTTON.x + SHUFFLE_BUTTON.width and mousepos[0] > SHUFFLE_BUTTON.x and mousepos[1] < SHUFFLE_BUTTON.y + SHUFFLE_BUTTON.height and mousepos[1] > SHUFFLE_BUTTON.y:
                        random.shuffle(arr)
                        n = 0
                        paused = False
                        sorted = False
                    #pause button
                    elif mousepos[0] < PAUSE_BUTTON.x + PAUSE_BUTTON.width and mousepos[0] > PAUSE_BUTTON.x and mousepos[1] < PAUSE_BUTTON.y + PAUSE_BUTTON.height and mousepos[1] > PAUSE_BUTTON.y:
                        paused = not paused
                    #toggle button
                    elif mousepos[0] < TOGGLE_BUTTON.x + TOGGLE_BUTTON.width and mousepos[0] > TOGGLE_BUTTON.x and mousepos[1] < TOGGLE_BUTTON.y + TOGGLE_BUTTON.height and mousepos[1] > TOGGLE_BUTTON.y:
                        modeindex += 1
                        modeindex = modeindex % len(mode)
                        random.shuffle(arr)
                        n = 0
                        sorted = False
                        sortedindex = 1
                    
            
        if not paused:
            
            sorted = True
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    sorted = False
            if sorted:
                sortedindex = sortedindex + NUMBER/100

                if sortedindex >= len(arr):
                    sortedindex = len(arr)
            else:
                sortedindex = 0


            if mode[modeindex] == "Bubble":
                bubblesort(arr)
            elif mode[modeindex] == "Selection":
                selectionsort(arr, n)
            elif mode[modeindex] == "Insertion":
                insertionsort(arr, n)
            elif mode[modeindex] == "Bogosort":
                bogosort(arr)
            elif mode[modeindex] == "Bozosort":
                bozosort(arr)
            elif mode[modeindex] == "Intelligent Design":
                pass
            elif mode[modeindex] == "Gorosort":
                grogosort(arr)
            else:
                print("ERROR")
            
            n += 1
            n = n % (len(arr) - 1)


                






if __name__ == "__main__":
    main()