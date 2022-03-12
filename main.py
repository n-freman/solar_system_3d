from xml.dom.minidom import Entity
import ursina
from Model import Planet

WIDTH, HEIGHT = 800, 800
FPS = 60
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 29, 50)
DARK_GREY = (80, 78, 81)






def update():

    for planet in planets:
        planet.update_pos(planets)
        planet.update_coord()


app = ursina.Ursina()

sun = Planet(0, 0, 30, YELLOW, 1.98892*10**30)
sun.sun = True

earth = Planet(-1*Planet.AU, 0, 16, BLUE, 5.9472*10**24)
earth.y_vel = 29.783 * 10**3

mars = Planet(-1.524*Planet.AU, 0, 12, RED, 6.39*10**23)
mars.y_vel = 24.077 * 10**3

mercury = Planet(0.387*Planet.AU, 0, 8, DARK_GREY, 3.30*10**23)
mercury.y_vel = -47.4 * 10**3

venus = Planet(0.723*Planet.AU, 0, 14, WHITE, 4.8685*10**24)
venus.y_vel = -35.02 * 10**3

planets = [sun, earth, mars, mercury, venus]
# ursina.camera.position = (0, 3, 0)
# ursina.camera.rotation_y = 90
ursina.PointLight(y=5)

app.run()

    

print(int(input()) + int(input()))