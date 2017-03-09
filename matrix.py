import math

def make_translate( x, y, z ):
    trans = new_matrix(4,4)
    trans[0] = [1, 0, 0, 0]
    trans[1] = [0, 1, 0, 0]
    trans[2] = [0, 0, 1, 0]
    trans[3] = [x, y, z, 1]
    return trans

def make_scale( x, y, z ):
    s = new_matrix(4,4)
    s[0] = [x, 0, 0, 0]
    s[1] = [0, y, 0, 0]
    s[2] = [0, 0, z, 0]
    s[3] = [0, 0, 0, 1]
    return s

def make_rotX( theta ):
    angle_x = math.radians(theta)
    rot_x = ident(new_matrix(4,4))
    rot_x[0] = [1,0, 0, 0]
    rot_x[1] = [0, math.cos(angle_x), math.sin(angle_x), 0]
    rot_x[2] = [0, -1*math.sin(angle_x), math.cos(angle_x), 0]
    rot_x[3] = [0, 0, 0, 1]
    return rot_x

def make_rotY( theta ):
    angle_y = math.radians(theta)
    rot_y = ident(new_matrix(4,4))
    rot_y[0] = [math.cos(angle_y),0, math.sin(angle_y), 0]
    rot_y[1] = [0, 1, 0, 0]
    rot_y[2] = [-1*math.sin(angle_y), 0, math.cos(angle_y), 0]
    rot_y[3] = [0, 0, 0, 1]
    return rot_y

def make_rotZ( theta ):
    angle_z = math.radians(angle_z)
    rot_z = ident(new_matrix(4,4))
    rot_z[0] = [math.cos(angle_z), math.sin(angle_z), 0, 0]
    rot_z[1] = [-1*math.sin(angle_z), math.cos(angle_z), 0,  0]
    rot_z[2] = [0, 0, 1, 0]
    rot_z[3] = [0, 0, 0, 1]
    return rot_z

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
