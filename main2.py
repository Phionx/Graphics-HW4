from display import *
from draw import *


screen = new_screen()

color1 = [ 0, 255, 0 ]
color2 = [255, 0, 0]
color3 = [0, 0, 255]
matrix = new_matrix()

def test(matrix):
    for i in range(0, 150, 5):
        matrix = add_edge(matrix, i, 150-i, 0, -i, i - 150, 0)

    draw_lines( matrix, screen, color1 )
    print "Current Edge Matrix"
    print_matrix(matrix)
    print "New Identity Matrix I"
    a = ident(new_matrix())
    print_matrix(a)

    print "Multiplying I x Edge Matrix, here is the resultant matrix:"
    matrix = matrix_mult(a, matrix)
    print_matrix(matrix)

    #print "Now Scaling the Edge Matrix by 1.5"
    #print_matrix(matrix)
    #matrix = scalar_mult(matrix, 2)
    return matrix

def scale(matrix, a, b, c):
    s = new_matrix(4,4)
    s[0] = [a, 0, 0, 0]
    s[1] = [0, b, 0, 0]
    s[2] = [0, 0, c, 0]
    s[3] = [0, 0, 0, 1]
    matrix = matrix_mult(s, matrix)
    return matrix

def rotate(matrix, angle_x, angle_y, angle_z):
    angle_x = math.radians(angle_x)
    angle_y = math.radians(angle_y)
    angle_z = math.radians(angle_z)
    rot_x = ident(new_matrix(4,4))
    rot_y = ident(new_matrix(4,4))
    rot_z = ident(new_matrix(4,4))
    rot_x[0] = [1,0, 0, 0]
    rot_x[1] = [0, math.cos(angle_x), math.sin(angle_x), 0]
    rot_x[2] = [0, -1*math.sin(angle_x), math.cos(angle_x), 0]
    rot_x[3] = [0, 0, 0, 1]

    rot_y[0] = [math.cos(angle_y),0, math.sin(angle_y), 0]
    rot_y[1] = [0, 1, 0, 0]
    rot_y[2] = [-1*math.sin(angle_y), 0, math.cos(angle_y), 0]
    rot_y[3] = [0, 0, 0, 1]

    rot_z[0] = [math.cos(angle_z), math.sin(angle_z), 0, 0]
    rot_z[1] = [-1*math.sin(angle_z), math.cos(angle_z), 0,  0]
    rot_z[2] = [0, 0, 1, 0]
    rot_z[3] = [0, 0, 0, 1]

    rot = matrix_mult(rot_z, rot_y)
    rot = matrix_mult(rot, rot_x)

    matrix = matrix_mult(rot, matrix)
    return matrix
def translate(matrix, a, b, c):
    trans = new_matrix(4,4)
    trans[0] = [1, 0, 0, 0]
    trans[1] = [0, 1, 0, 0]
    trans[2] = [0, 0, 1, 0]
    trans[3] = [a, b, c, 1]
    matrix = matrix_mult(trans, matrix)
    return matrix


matrix = test(matrix)

for i in range(0, 360, 90):
    matrix = rotate(matrix, i)
    draw_lines(matrix, screen, color1)
    matrix = rotate(matrix, i + 45)
    draw_lines(matrix, screen, color3)

matrix = scale(matrix, 2)
matrix = rotate(matrix, 22.5)
for i in range(0, 360, 90):
    matrix = rotate(matrix, i)
    draw_lines(matrix, screen, color3)
    matrix = rotate(matrix, i + 45)
    draw_lines(matrix, screen, color2)
display(screen)
