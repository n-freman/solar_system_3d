import math
from ursina import Entity
from ursina import color as urs_color


class Planet(Entity):
    AU = 149.6e6 * 1000
    G = 6.47428e-11
    SCALE = 3 / AU
    # TIMESTEP here is equal to one day
    TIMESTEP = 3600 * 2
    

    def __init__(self, x, y, radius, color, mass):
        super().__init__(model = 'sphere')
        self.x_pos = x
        self.y_pos = y
        self.radius = radius
        self.color = urs_color.rgb(*color)
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_pos_vel = 0
        self.y_pos_vel = 0
        self.update_coord()
        
        self.scale = self.radius/50
    
    def gravity(self, other):
        other_x, other_y = other.x_pos, other.y_pos
        distance_x = other_x - self.x_pos
        distance_y = other_y - self.y_pos
        distance = math.sqrt(distance_x**2+distance_y**2)

        if other.sun:
            self.distance_to_sun = distance
        
        force = self.G * self.mass* other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_coord(self):
        self.x = self.x_pos * self.SCALE
        self.z = self.y_pos * self.SCALE
    
    def update_pos(self, planets):
        # Use itertools permutations later
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.gravity(planet)
            total_fx += fx
            total_fy += fy

        # F = ma = mv/t =>
        # V = Ft/m
        self.x_pos_vel += total_fx / self.mass * self.TIMESTEP
        self.y_pos_vel += total_fy / self.mass * self.TIMESTEP

        # S = Vt
        self.x_pos += self.x_pos_vel * self.TIMESTEP
        self.y_pos += self.y_pos_vel * self.TIMESTEP
        self.orbit.append((self.x_pos, self.y_pos))
        