import svg_build
import shape
import palettes

title = "test"
x_in = 1920
y_in = 1080

origin = [(x_in/2),(y_in/2)]

offset = 120

corners = [[120,120],[x_in-120,120],[x_in-120,y_in-120],[120,y_in-120]]
perimeter_list = []

for x in range (0, 3):
	line = shape.divide_line(corners[x-1], corners[x], 8)
	perimeter_list.extend(line)
	
print(len(perimeter_list))

layer = 0

for z in range (0, len(perimeter_list), 1):
	svg_build.start(title, layer, x_in, y_in, "white")
	
	if layer == 0:
		for x in range(0, len(corners), 1):
			svg_build.generate_text(corners[x], x, 100)
	
	svg_build.end(layer)
	
	layer += 1
	