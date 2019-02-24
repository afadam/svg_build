canvas = []

def start(
	name, layer, x, y, fill
):
	canvas_file = (
		'output/' + name + "_l" + str(layer) + '_' + str(x) + 'x' + str(y) + '.svg'
		)	
	new_layer = open(canvas_file, 'w')
	canvas.append(new_layer)
	
	canvas[layer].write(
		'<svg width="' + str(x) + '" height="' + str(y) + '">\n'
	)
	canvas[layer].write(
		'<rect width="100%" height="100%" fill="' + fill + '" />\n'
	)

def end():
	for layer in range(len(canvas)):
		canvas[layer].write('</svg>')
		canvas[layer].close
			
def generate_circle(
	center, r, fill = "none", st_w = 1, st = "black", layer = 0
):
	canvas[layer].write('<circle cx="' + 
		str(center[0]) + '" cy="' + str(center[1]) + '" r="' + str(r)
	)
	canvas[layer].write(
		'" stroke-width="' + str(st_w) + '" stroke="' + st + '" fill="' + fill + '" />\n'
	)
	
def generate_line(
	pt1, pt2, st_w = 1, st = "black", layer = 0
):
	canvas[layer].write(
		'<line x1="' + str(pt1[0]) + '" y1="' + str(pt1[1]) + '" x2="' + str(pt2[1]) + '" y2="' + str(pt2[1])
	)
	canvas[layer].write(
		'" stroke-width="' + str(st_w) + '" stroke="' + st + '" />\n'
	)
	
def generate_path(
	p_list, fill = "none", st_w = 1, st = "black", closed = 1, layer = 0
):
	canvas[layer].write(
		'<path d="M' + str(p_list[0][0]) + ' ' + str(p_list[0][1])
	)
	
	for pt in range(1, len(p_list)) :
		canvas[layer].write(
			' L' + str(p_list[pt][0]) + ' ' + str(p_list[pt][1])
		)
	
	if closed == 1:
		canvas[layer].write(' Z')
	
	canvas[layer].write(
		'" stroke-width="' + str(st_w) + '" stroke="' + st + '" fill="' + fill + '" stroke-linejoin="round" />\n'
	)
