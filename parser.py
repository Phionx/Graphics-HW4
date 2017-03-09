from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    lines = [line.rstrip('\n') for line in open(fname)]
    i = 0
    temp = []
    while i < len(lines):
        if lines[i] == "line":
            i += 1
            temp = lines[i].split()
            add_edge(points, float(temp[0]), float(temp[1]), float(temp[2]), float(temp[3]), float(temp[4]), float(temp[5]))
        elif lines[i] == "ident":
            ident(transform)
        elif lines[i] == "scale":
            i += 1
            temp = lines[i].split()
            matrix_mult(make_scale(float(temp[0]), float(temp[1]), float(temp[2])), transform)
        elif lines[i] == "move":
            i += 1
            temp = lines[i].split()
            matrix_mult(make_translate(float(temp[0]), float(temp[1]), float(temp[2])), transform)
        elif lines[i] == "rotate":
            i += 1
            temp = lines[i].split()
            if temp[0] == "x":
                matrix_mult(make_rotX(float(temp[1])), transform)
            elif temp[0] == "y":
                matrix_mult(make_rotY(float(temp[1])), transform)
            elif temp[0] == "z":
                matrix_mult(make_rotZ(float(temp[1])), transform)
        elif lines[i] == "apply":
            matrix_mult(transform, points)
        elif lines[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif lines[i] == "save":
            i += 1
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            save_ppm(screen, lines[i])
        i += 1
    pass
