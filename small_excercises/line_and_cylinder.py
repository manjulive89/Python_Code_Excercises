#!/usr/bin/env python3

class Line():
    def __init__(self, coor1,coor2):
        self.x1 = coor1[0]
        self.x2 = coor1[1]
        self.y1 = coor2[0]
        self.y2 = coor2[1]

    def distance(self):
        self.distance = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        return self.distance

    def slope(self):
        self.slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        return self.slope


coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1,coordinate2)
print(line.distance())
print(line.slope())

class Cylinder():
    pi = 3.142

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        self.volume = ((self.pi * (self.radius **2)) * self.height)
        return self.volume

    def surface_area(self):
        self.surface_area = (2 * self.pi * (self.radius **2)) + (2 * self.pi * self.radius * self.height)
        return self.surface_area

cyl = Cylinder(2,3)
print(cyl.volume())
print(cyl.surface_area())
