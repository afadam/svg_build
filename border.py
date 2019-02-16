import datetime
import svg_build
import shape
import math
import random

#title = input('Title ')
#x_in = input('X: ')
#y_in = input('Y: ')

title = "border"
x_in = 1024
y_in = 1024

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

o_border = [[1,1],[1024,1],[1024,1024],[1,1024]]
i_border = [[32,32],[992,32],[992,992],[32,992]]
	
svg_build.end()

