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



svg_build.end()		