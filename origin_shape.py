import datetime
import svg_build
import shape
import math
import random

#title = input('Title ')
#x_in = input('X: ')
#y_in = input('Y: ')

title = "centre"
x_in = 1024
y_in = 1024
r = [[462,512],[562,512]]
colours = ["green", "blue", "yellow", "lightblue", "orange", "red", "purple", "pink"]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

tri = shape.triangle(r[0],r[1],-200)
svg_build.generate_path(tri)

tri = shape.triangle(r[0],r[1],200)
svg_build.generate_path(tri)

print("hello")

svg_build.end()
