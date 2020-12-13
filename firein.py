import datetime
import svg_build
import shape
import palettes
import random
import funcs

title = "firein"
x_in = 1000
y_in = 1000
time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
name = (title + "_" + string_time)
svg_build.start(name, 0, x_in, y_in, "white")

hexagon = shape.centre_polygon([500,500], 12, 400, orient=0)
svg_build.generate_path(hexagon)

polygon_list = funcs.firein(hexagon, 72)

for polygon in range(0, len(polygon_list)):
	colour = str(hex(random.randrange(11111, 14555222, 30)))
	svg_build.generate_path(polygon_list[polygon], st_w=2, st=palettes.plt11[1], fill=palettes.plt11[random.randint(0,3)])
	#svg_build.generate_path(polygon_list[polygon], st_w=2, st=palettes.plt11[1], fill='#' + colour[2:])

septagon = shape.centre_polygon([500,500], 7, 400, orient=0)
svg_build.generate_path(septagon)
svg_build.generate_path(funcs.kernel(septagon, 7))

svg_build.end()		