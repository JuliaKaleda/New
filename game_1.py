import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("Times", 25)
score_font = pygame.font.SysFont("Times", 25)

def score_1(score):
    value = score_font.render("Score: " + str(score), True, green)
    dis.blit(value, [0, 0])

def our_snake(a, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], 10, 10])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [160, 190])


def gameLoop():
    game_over = False
    game_close = False

    x1 = 300
    y1 = 400

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    food_x = round(random.randrange(0, 790) / 10.0) * 10.0
    food_y = round(random.randrange(0, 490) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("Game over! Press C-Play Again or Q-Quit", red)
            score_1(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        if x1 >= 800 or x1 < 0 or y1 >= 500 or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, red, [food_x, food_y, 10, 10])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(10, snake_List)
        score_1(Length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, 790) / 10) * 10
            food_y = round(random.randrange(0, 490) / 10) * 10
            Length_of_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()

gameLoop()