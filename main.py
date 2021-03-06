import pygame
pygame.init()

x_screen = 500
y_screen = 500

win = pygame.display.set_mode((x_screen, y_screen), pygame.RESIZABLE)
pygame.display.set_caption("doodle")

cameraX = 0
cameraY = 0
vel = 5


def vertices(x, y, z):
    pygame.draw.polygon(win, (255, 0, 0),
                        ((120 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                         (280 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                         (100 + (cameraX / 1.5), 100 + (cameraY / 1.5))))
    pygame.draw.polygon(win, (0, 0, 255),
                        ((100 + cameraX, 100 + cameraY),
                         (280 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                         (300 + cameraX, 100 + cameraY)))


run = True
while run:
    win.fill((0, 0, 0))
    pygame.time.delay(16)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cameraX = cameraX - vel
        print(cameraX)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cameraX = cameraX + vel
        print(cameraX)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cameraY = cameraY - vel
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cameraY = cameraY + vel

    #top
    if cameraY >= 60:
        pygame.draw.polygon(win, (255, 0, 0),
                            ((120 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                            (280 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                            (100 + cameraX, 100 + cameraY)))
        pygame.draw.polygon(win, (0, 0, 255),
                            ((100 + cameraX, 100 + cameraY),
                            (280 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                            (300 + cameraX, 100 + cameraY)))
    #top end
    #bottom
    if cameraY <= -60:
        pygame.draw.polygon(win, (255, 0, 0),
                            ((120 + (cameraX / 1.5), 280 + (cameraY / 1.5)),
                            (280 + (cameraX / 1.5), 280 + (cameraY / 1.5)),
                            (100 + cameraX, 300 + cameraY)))
        pygame.draw.polygon(win, (0, 0, 255),
                            ((100 + cameraX, 300 + cameraY),
                            (280 + (cameraX / 1.5), 280 + (cameraY / 1.5)),
                            (300 + cameraX, 300 + cameraY)))
    #bottom end
    #left
    if cameraX >= 60:
        pygame.draw.polygon(win, (255, 0, 0),
                            ((120 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                            (100 + cameraX, 100 + cameraY),
                            (120 + (cameraX / 1.5), 280 + (cameraY / 1.5))))
        pygame.draw.polygon(win, (0, 0, 255),
                            ((120 + (cameraX / 1.5), 280 + (cameraY / 1.5)),
                            (100 + cameraX, 100 + cameraY),
                            (100 + cameraX, 300 + cameraY)))
    #left end
    #right
    if cameraX <= -60:
        pygame.draw.polygon(win, (255, 0, 0),
                            ((300 + cameraX, 100 + cameraY),
                            (280 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                            (300 + cameraX, 300 + cameraY)))
        pygame.draw.polygon(win, (0, 0, 255),
                            ((300 + cameraX, 300 + cameraY),
                            (280 + (cameraX / 1.5), 120 + (cameraY / 1.5)),
                            (280 + (cameraX / 1.5), 280 + (cameraY / 1.5))))
    #right end
    #front
    pygame.draw.polygon(win, (255, 0, 0),
                        ((100 + cameraX, 100 + cameraY),
                         (300 + cameraX, 100 + cameraY),
                         (100 + cameraX, 300 + cameraY)))
    pygame.draw.polygon(win, (0, 0, 255),
                        ((100 + cameraX, 300 + cameraY),
                         (300 + cameraX, 100 + cameraY),
                         (300 + cameraX, 300 + cameraY)))
    #front end

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
print("done")
