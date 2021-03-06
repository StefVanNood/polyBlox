import pygame
pygame.init()

x_screen = 500
y_screen = 500

win = pygame.display.set_mode((x_screen, y_screen), pygame.RESIZABLE)
pygame.display.set_caption("doodle")

cameraX = 0
cameraY = 0
vel = 5


def vertices(x1, y1, z1, x2, y2, z2, x3, y3, z3, r, g, b, x, y):
    surface = pygame.display.get_surface()
    x_width, y_width = surface.get_width(), surface.get_height()
    z_speed = 200
    if (cameraX / ((z1.__abs__() / 100) + 1)).__abs__() >= z1 and \
            not z1 == 1:
        z_speed = z1
    if (cameraY / ((z1.__abs__() / 100) + 1)).__abs__() >= z1 and \
            not z1 == 1:
        z_speed = z1
    if (cameraX / ((z2.__abs__() / 100) + 1)).__abs__() >= z2 and \
            not z2 == 1:
        z_speed = z2
    if (cameraY / ((z2.__abs__() / 100) + 1)).__abs__() >= z2 and \
            not z2 == 1:
        z_speed = z2
    if (cameraX / ((z3.__abs__() / 100) + 1)).__abs__() >= z3 and \
            not z3 == 1:
        z_speed = z3
    if (cameraY / ((z3.__abs__() / 100) + 1)).__abs__() >= z3 and \
            not z3 == 1:
        z_speed = z3

    pygame.draw.polygon(win, (r, g, b),
                        (
                        ((x1 + x_width / 2 - 200 + x) + (cameraX / ((z1.__abs__() / z_speed) + 1)),
                         (y1 + y_width / 2 - 200 + y) + (cameraY / ((z1.__abs__() / z_speed) + 1))),
                        ((x2 + x_width / 2 - 200 + x) + (cameraX / ((z2.__abs__() / z_speed) + 1)),
                         (y2 + y_width / 2 - 200 + y) + (cameraY / ((z2.__abs__() / z_speed) + 1))),
                        ((x3 + x_width / 2 - 200 + x) + (cameraX / ((z3.__abs__() / z_speed) + 1)),
                         (y3 + y_width / 2 - 200 + y) + (cameraY / ((z3.__abs__() / z_speed) + 1)))
                        ))


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

    if cameraY >= 40:
        vertices(120, 120, 200, 280, 120, 200, 100, 100, 1, 255, 0, 0, 0, 0)
        vertices(100, 100, 1, 280, 120, 200, 300, 100, 1, 0, 0, 255, 0, 0)
    if cameraY <= -40:
        vertices(100, 300, 1, 300, 300, 1, 120, 280, 200, 255, 0, 0, 0, 0)
        vertices(120, 280, 200, 300, 300, 1, 280, 280, 200, 0, 0, 255, 0, 0)
    if cameraX >= 35:
        vertices(120, 120, 200, 100, 100, 1, 120, 280, 200, 255, 0, 0, 0, 0)
        vertices(120, 280, 200, 100, 100, 1, 100, 300, 1, 0, 0, 255, 0, 0)
    if cameraX <= -35:
        vertices(300, 100, 1, 280, 120, 200, 300, 300, 1, 255, 0, 0, 0, 0)
        vertices(300, 300, 1, 280, 120, 200, 280, 280, 200, 0, 0, 255, 0, 0)
    vertices(100, 100, 1, 300, 100, 1, 100, 300, 1, 255, 0, 0, 0, 0)
    vertices(100, 300, 1, 300, 100, 1, 300, 300, 1, 0, 0, 255, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
print("done")
