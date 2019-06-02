import datetime
import svg_build
import shape

title = "star"
x_in = 1024
y_in = 1024
origin = [512,512]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

shape.divide_line([-2,-2], [2,2], 8)

hexagon = shape.centre_polygon(origin, 6, 256)

perimeter_list = []

for x in range (0, len(hexagon)):
	line = shape.divide_line(hexagon[x], hexagon[x-1], 6)
	perimeter_list.extend(line)

print(perimeter_list)
print(len(perimeter_list))
svg_build.generate_path(perimeter_list)

hexagon2 = shape.centre_polygon(origin, 7, 312)

perimeter_list2 = perimeter_list


mid_list = int(len(perimeter_list2) / 2)
print(len(perimeter_list2))
	  
for y in range (0, mid_list, 1):	
	svg_build.generate_path([perimeter_list2[y],perimeter_list2[mid_list + y]])
	


svg_build.end()