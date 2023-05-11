class Sphere:
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return 4 / 3 * 3.1415926535 * self.radius ** 3

    def get_square(self):
        return 4 * 3.1415926535 * self.radius ** 2

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_center(self):
        return self.center

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance_squared = (x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2
        return distance_squared <= self.radius ** 2

    def __str__(self):
        return f"Sphere with radius {self.radius} and center ({self.center})"