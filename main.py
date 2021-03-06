import pygame
pygame.init()

x_screen = 500
y_screen = 500

win = pygame.display.set_mode((x_screen, y_screen), pygame.RESIZABLE)
pygame.display.set_caption("polyBlox")

skyBox = pygame.image.load('images/skyBox.jpeg').convert_alpha(win)
pygame.transform.scale(skyBox, (1000, 1000))

cameraX = 0
cameraY = 0
cameraZ = 0
vel = 3

object1 = []
row = []
i = 1
f = open("cube").read()
for Value in f.split():
    row.append(int(Value))
    if i == 10:
        object1.append(row)
        row = []
        i = 0
    i = i + 1

object2 = []
row = []
i = 1
f = open("pyramid").read()
for Value in f.split():
    row.append(int(Value))
    if i == 10:
        object2.append(row)
        row = []
        i = 0
    i = i + 1


def vertices(x1, y1, z1, x2, y2, z2, x3, y3, z3, r, g, b, x, y):
    surface = pygame.display.get_surface()
    x_width, y_width = surface.get_width(), surface.get_height()
    z_speed = 300

    pygame.draw.polygon(win, (r, g, b),
                        (
                        ((x1 + x_width / 2 + x) + (cameraX / ((z1 / z_speed) + 1)),
                         (y1 + y_width / 2 + y) + (cameraY / ((z1 / z_speed) + 1))),
                        ((x2 + x_width / 2 + x) + (cameraX / ((z2 / z_speed) + 1)),
                         (y2 + y_width / 2 + y) + (cameraY / ((z2 / z_speed) + 1))),
                        ((x3 + x_width / 2 + x) + (cameraX / ((z3 / z_speed) + 1)),
                         (y3 + y_width / 2 + y) + (cameraY / ((z3 / z_speed) + 1)))
                        ))


def render_object1(color_r, color_g, color_b, location_x, location_y):
    for z in range(len(object1)):
        if object1[z][9] == 5:
            if cameraY >= 40:
                vertices(object1[z][0], object1[z][1], object1[z][2],
                         object1[z][3], object1[z][4], object1[z][5],
                         object1[z][6], object1[z][7], object1[z][8],
                         color_r, color_g, color_b,
                         location_x, location_y)
        if object1[z][9] == 3:
            if cameraY <= -40:
                vertices(object1[z][0], object1[z][1], object1[z][2],
                         object1[z][3], object1[z][4], object1[z][5],
                         object1[z][6], object1[z][7], object1[z][8],
                         color_r - 100, color_g - 100, color_b - 100,
                         location_x, location_y)
        if object1[z][9] == 2:
            if cameraX >= 40:
                vertices(object1[z][0], object1[z][1], object1[z][2],
                         object1[z][3], object1[z][4], object1[z][5],
                         object1[z][6], object1[z][7], object1[z][8],
                         color_r - 100, color_g - 100, color_b - 100,
                         location_x, location_y)
        if object1[z][9] == 4:
            if cameraX <= -40:
                vertices(object1[z][0], object1[z][1], object1[z][2],
                         object1[z][3], object1[z][4], object1[z][5],
                         object1[z][6], object1[z][7], object1[z][8],
                         color_r - 10, color_g - 10, color_b - 10,
                         location_x, location_y)
        if object1[z][9] == 1:
            vertices(object1[z][0], object1[z][1], object1[z][2],
                     object1[z][3], object1[z][4], object1[z][5],
                     object1[z][6], object1[z][7], object1[z][8],
                     color_r - 50, color_g - 50, color_b - 50,
                     location_x, location_y)


def render_object2(color_r, color_g, color_b, location_x, location_y):
    for z in range(len(object2)):
        if object2[z][9] == 5:
            if cameraY >= 40:
                vertices(object2[z][0], object2[z][1], object2[z][2],
                         object2[z][3], object2[z][4], object2[z][5],
                         object2[z][6], object2[z][7], object2[z][8],
                         color_r, color_g, color_b,
                         location_x, location_y)
        if object2[z][9] == 3:
            if cameraY <= -40:
                vertices(object2[z][0], object2[z][1], object2[z][2],
                         object2[z][3], object2[z][4], object2[z][5],
                         object2[z][6], object2[z][7], object2[z][8],
                         color_r - 100, color_g - 100, color_b - 100,
                         location_x, location_y)
        if object2[z][9] == 2:
            if cameraX >= 40:
                vertices(object2[z][0], object2[z][1], object2[z][2],
                         object2[z][3], object2[z][4], object2[z][5],
                         object2[z][6], object2[z][7], object2[z][8],
                         color_r - 100, color_g - 100, color_b - 100,
                         location_x, location_y)
        if object2[z][9] == 4:
            if cameraX <= -40:
                vertices(object2[z][0], object2[z][1], object2[z][2],
                         object2[z][3], object2[z][4], object2[z][5],
                         object2[z][6], object2[z][7], object2[z][8],
                         color_r - 10, color_g - 10, color_b - 10,
                         location_x, location_y)
        if object2[z][9] == 1:
            vertices(object2[z][0], object2[z][1], object2[z][2],
                     object2[z][3], object2[z][4], object2[z][5],
                     object2[z][6], object2[z][7], object2[z][8],
                     color_r - 50, color_g - 50, color_b - 50,
                     location_x, location_y)


run = True
while run:
    win.fill((100, 100, 100))
    pygame.time.delay(10)
    win.blit(skyBox, (0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cameraX = cameraX + vel
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cameraX = cameraX - vel
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cameraY = cameraY + vel
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cameraY = cameraY - vel

    render_object1(255, 100, 100, 0, 0)
    render_object2(255, 100, 100, -200, -400)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
print("stopped")
