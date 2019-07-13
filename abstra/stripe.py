import svg_build
import shape
import palettes

title = "red stripe2"

x_in = 1920
y_in = 1080

corners = [[0,0],[x_in,0],[x_in,y_in],[0,y_in]]
perimeter_list = []

for x in range (0, 4):
	line = shape.divide_line(corners[x-1], corners[x], 90)
	perimeter_list.extend(line)
	
print(len(perimeter_list))

layer = 0


for z in range (0, len(perimeter_list), 1):
	svg_build.start(title, layer, x_in, y_in, "white")
			
	if layer == 0:
	for z in range (0, len(perimeter_list), 1):
	
	svg_build.generate_line(perimeter_list[z], perimeter_list[z-180], 120, "red", z)
	
	svg_build.end(layer)
	
	layer += 1
	
	
	