from Practika2.Pr_13.Pr13_Task_1 import Sphere

s = Sphere(0.5)

print(s.get_radius())
print(s.get_center())
print(s.get_volume())
print(s.get_square())

s.set_radius(1.6)
s.set_center(0.0, 0.0, 0.0)

print(s.is_point_inside(1.0, 2.0, 3.0))
print(s.is_point_inside(0.0, -1.5, 0.0))