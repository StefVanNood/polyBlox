import pygame
pygame.init()

x_screen = 500
y_screen = 500

win = pygame.display.set_mode((x_screen, y_screen))
pygame.display.set_caption("doodle")

cameraX = 0
cameraY = 0
vel = 5

run = True
while run:
    win.fill((0, 0, 0))
    pygame.time.delay(16)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cameraX = cameraX - vel
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cameraX = cameraX + vel
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cameraY = cameraY - vel
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cameraY = cameraY + vel

    pygame.draw.line(win, (255, 255, 255), (100, 100), (300, 100))
    pygame.draw.line(win, (255, 255, 255), (100, 100), (100, 300))
    pygame.draw.line(win, (255, 255, 255), (100, 300), (300, 300))
    pygame.draw.line(win, (255, 255, 255), (300, 300), (300, 100))

    pygame.draw.line(win, (255, 255, 255), (100, 100), (120, 120))
    pygame.draw.line(win, (255, 255, 255), (100, 300), (120, 280))
    pygame.draw.line(win, (255, 255, 255), (300, 300), (280, 280))
    pygame.draw.line(win, (255, 255, 255), (300, 100), (280, 120))

    pygame.draw.line(win, (255, 255, 255), (120, 120), (280, 120))
    pygame.draw.line(win, (255, 255, 255), (120, 120), (120, 280))
    pygame.draw.line(win, (255, 255, 255), (120, 280), (280, 280))
    pygame.draw.line(win, (255, 255, 255), (280, 280), (280, 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
print("done")
