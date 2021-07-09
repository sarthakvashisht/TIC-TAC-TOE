import pygame

pygame.init()
# screen size and display name nd icon
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TIC TAC TOE")

# variables
green = (115, 230, 6)
markers = []
winner = 0
font = pygame.font.SysFont("freeSans.ttf", 40)
gameover = False
row = []
clicked = False
player = 1
pos = []
for i in range(3):
    row = [0] * 3
    markers.append(row)


def grid():
    for x in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (0, x * 100), (300, x * 100), 5)
        pygame.draw.line(screen, (0, 0, 0), (x * 100, 300), (x * 100, 0), 5)


def symbol():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15),
                                 (x_pos * 100 + 85, y_pos * 100 + 85), 5)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85),
                                 (x_pos * 100 + 85, y_pos * 100 + 15), 5)
            if y == -1:
                pygame.draw.circle(screen, (255, 0, 0), (x_pos * 100 + 50, y_pos * 100 + 50), 38, 3)
            y_pos += 1
        x_pos += 1


def gamewin(winner):
    wintxt = 'player ' + str(winner) + 'wins!'
    winimg = font.render(wintxt, True, (0, 0, 255))
    pygame.draw.rect(screen, (0, 255, 0), (60, 120,200,50))
    screen.blit(winimg, (70, 130))


def win():
    global winner
    global gameover
    ypos = 0
    for x in markers:
        if sum(x) == 3:
            winner = 1
            gameover = True
        if sum(x) == -3:
            winner = 2
            gameover = True
        if markers[0][ypos] + markers[1][ypos] + markers[2][ypos] == 3:
            winner = 1
            gameover = True
        if markers[0][ypos] + markers[1][ypos] + markers[2][ypos] == -3:
            winner = 2
            gameover = True
        ypos += 1
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == 3:
        winner = 1
        gameover = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[0][2] + markers[1][1] + markers[2][1] == -3:
        winner = 2
        gameover = True


run = True
while run:
    screen.fill((255, 221, 51))
    symbol()
    grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if gameover == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                px = pos[0]
                py = pos[1]
                if markers[px // 100][py // 100] == 0:
                    markers[px // 100][py // 100] = player
                    player *= -1
                    win()
    if gameover == True:
        gamewin(winner)

    pygame.display.update()
