import svg_build
import shape
import palettes
import random

title = "tree"
x_in = 1920
y_in = 1080

origin = [(x_in/2),(y_in/2)]

frames = 1

planted = [960, 1080]

def tree(root, size):

	
	weight = int(size/4.5)
	inv_weight = size - weight
	
	end = [1,1]
	end[0] = (root[0] + random.uniform(-2* inv_weight, 2* inv_weight))
	end[1] = (root[1] - (size * 0.88))

	branch = [root, end]
		
	svg_build.generate_path(branch, st_w = weight, st="darkgreen")
			  
	branch_size = size * 0.68	
	
	if (branch_size < 3 ):
		return
	else:
		
		tree(end, branch_size)
		
		branches = random.randrange(1, 3, 1)
		
		for x in range (0, branches, 1):
						
			branch_length = shape.divide_line(root, end, factor=10, last_pt=0)
			node = random.choice(branch_length)
		
			tree(node, branch_size)
			
		
for z in range (0, frames, 1):
	
	svg_build.start(title, z, x_in, y_in, fill="lightblue")

	tree(planted, 360) 
		
	svg_build.end(z)
	

	