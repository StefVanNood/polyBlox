import pygame
pygame.init()

x_screen = 500
y_screen = 500

win = pygame.display.set_mode((x_screen, y_screen))
pygame.display.set_caption("doodle")

run = True
while run:
    win.fill((0, 0, 0))
    pygame.time.delay(16)
    pygame.draw.line(win, (255, 255, 255), (60, 80), (200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
print("done")
