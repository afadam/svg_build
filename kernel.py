import datetime
import svg_build
import shape
import palettes
import random
import funcs

title = "kernel"
x_in = 1000
y_in = 1000
time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
name = (title + "_" + string_time)
svg_build.start(name, 0, x_in, y_in, "white")

polygon = shape.centre_polygon([500,500], 4, 100, orient=0)
svg_build.generate_path(polygon)
segments = funcs.kernel(polygon)

print(len(segments))
for segment in range(0, len(segments)):
	svg_build.generate_path(segments[segment])
	jam = funcs.firein(segments[segment], 9)
	for roll in range(0, len(jam)):
		svg_build.generate_path(jam[roll])

svg_build.end()		