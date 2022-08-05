import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Edureka')

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 -= 10
            elif event.key == pygame.K_RIGHT:
                x1 += 10
            elif event.key == pygame.K_UP:
                y1 -= 10
            elif event.key == pygame.K_DOWN:
                y1 += 10

    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()