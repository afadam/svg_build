"""svg_build contains functions to create .svg files and generate shapes/text
in them when given points and point lists.

point - [x,y]
point list - [[x,y],[x1,y1],...,[xn,yn]]
"""

import datetime
import os

layers = [] 

def start(title, layer, x, y, fill="none", anim=False):
	"""Create a new .svg file, open and assign it as a layer. 
	Open the <svg> tag with height and width and draw a background fill.

    title -- name of the drawing
    layer -- layer of the drawing
	x,y -- height and width of svg file
	fill -- background colour
    """
	# build a string for the layer's filename
	
	time = datetime.datetime.now()	
	string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
	
	try:
		os.stat('output/' + title)
	except:
		os.mkdir('output/' + title)
	
	if (anim==True):
		layer_file = (	
			'output/' + title + '/' + 'image' + str(layer).zfill(4) + '.svg'
			)	
	else:
		layer_file = (	
			'output/' + title + string_time + '.svg'
			)

	new_layer = open(layer_file, 'w')
	
	layers.append(new_layer)

	layers[layer].write(
		'<svg width="' + str(x) + '" height="' + str(y) + '">\n'
	)
	layers[layer].write(
		'<rect width="100%" height="100%" fill="' + fill + '" />\n'                  
	)

def end(layer):
	layers[layer].write('</svg>')
	layers[layer].close
	
def end_all():
	"""Close all layer's svg tags and close all layer files.
	"""
	for layer in range(len(layers)):
		layers[layer].write('</svg>')
		layers[layer].close
			
def generate_circle(centre, r, fill = "none", st_w=1, st="black", layer=0):
	"""Draw a circle of given radius using <circle> tag, centred on 

	centre -- a point 
	r -- radius
	fill -- colour (default none)
	st_w -- stroke width in px (default 1)
	st -- stroke colour (default black)
	layer (default 0)
	"""
	layers[layer].write('<circle cx="' + 
		str(centre[0]) + '" cy="' + str(centre[1]) + '" r="' + str(r)
	)
	layers[layer].write(
		'" stroke-width="' + str(st_w) + '" stroke="' + st + 
		'" fill="' + fill + '" />\n'
	)
	
def generate_line(pt1, pt2, st_w=1, st="black", layer=0):
	"""Draw a line between two given points using <line> tag & apply formatting
	
	pt1 -- start point
	pt2 -- end point
	st_w -- stroke width (default 1)
	st = stroke colour (default "black")
	layer (default 0)
	"""
	layers[layer].write(
		'<line x1="' + str(round(pt1[0], 3)) + '" y1="' + str(round(pt1[1], 3)) + 
		'" x2="' + str(round(pt2[1], 3)) + '" y2="' + str(round(pt2[1], 3))
	)
	layers[layer].write(
		'" stroke-width="' + str(st_w) + '" stroke="' + st + '" />\n'
	)
	
def generate_path(p_list, closed=True, fill="none", st_w=1, st="black", layer=0):
	"""
	p_list, 
	fill = "none", 
	st_w = 1, 
	st = "black",
	closed = 1, 
	layer = 0
	"""
	layers[layer].write(
		'<path d="M' + str(round(p_list[0][0], 3)) + ' ' + str(round(p_list[0][1], 3))
	)
	
	for pt in range(1, len(p_list)):
		layers[layer].write(
			' L' + str(round(p_list[pt][0], 3)) + ' ' + str(round(p_list[pt][1], 3))
		)
	
	if closed:
		layers[layer].write(' Z')
	
	layers[layer].write(
		'" stroke-width="' + str(st_w) + '" stroke="' + st +
		'" fill="' + fill + '" stroke-linejoin="round" />\n'
	)

def generate_text(location, message, size, layer=0):
	"""
	location, 
	message,
	size,
	layer=0
	"""
	layers[layer].write(
		'<text x="' + str(round(location[0], 3)) + 
		'" y="' + str(round(location[1], 3))
	)
	layers[layer].write(
		'" font-size="' + str(size) + '" > '
	)
	layers[layer].write(
		str(message) + '</text>\n'
	)