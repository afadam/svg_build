import datetime
import svg_build
import shape
import palettes
import random
import funcs

title = "plotter"
x_in = 1024
y_in = 1024
origin = [512, 512]

p = palettes.plt12

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
name = (title + "_" + string_time)
svg_build.start(name, 0, x_in, y_in, p[0])

polygon = shape.centre_polygon(origin, 17, 480)
print(polygon)
svg_build.point_plotter(polygon)

svg_build.end()				