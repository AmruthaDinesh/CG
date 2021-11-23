from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import pi, tan, radians, sin, cos

import sys
import playsound

WINDOW_SIZE = 500

X = Y = 0
SPEED = 1
OFFSET = 0
TO_RIGHT = True
def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def get_input():
    global SPEED, ANGLE, RADIUS, X1, Y1, X2, Y2, TO_RIGHT,Y
    ANGLE= float(input("Enter angle of inclination of the line: "))
    RADIUS = 20
    SPEED = float(input("Speed Multiplier: "))
    X1, Y1 = -WINDOW_SIZE, -WINDOW_SIZE * tan(radians(ANGLE))
    X2, Y2 = WINDOW_SIZE, WINDOW_SIZE * tan(radians(ANGLE))
    Y=RADIUS
    if ANGLE >= 0:
        TO_RIGHT = False
    else:
        TO_RIGHT = True

def create_line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(X1, Y1)
    glVertex2f(X2, Y2)
    glEnd()

def update(value):
    global X, Y, SPEED, TO_RIGHT, OFFSET
    if TO_RIGHT:    
        X += SPEED * cos(radians(ANGLE))
        Y += SPEED * sin(radians(ANGLE))
        OFFSET -= 0.01 * SPEED
    else: 
        X -= SPEED * cos(radians(ANGLE))
        Y -= SPEED * sin(radians(ANGLE))
        OFFSET += 0.01 * SPEED
    if X > WINDOW_SIZE - RADIUS:
        TO_RIGHT = False
    elif X < -WINDOW_SIZE + RADIUS:
        TO_RIGHT = True    
    glutPostRedisplay()
    glutTimerFunc(int(1000/60), update, 0)




def draw_circle(x, y):
    global OFFSET
    glBegin(GL_TRIANGLE_FAN)
    for i in range(361):
        glColor3f(0,sin(i),0)
        glVertex2f(RADIUS * cos(OFFSET + pi * i / 180) + x, RADIUS * sin(OFFSET + pi * i / 180) + y)
    glEnd()
    
def draw_car():
	#glClear(GL_COLOR_BUFFER_BIT)
	y_2=Y + 250*tan(radians(ANGLE))
	
	x_2=X+200
	glColor3f(1.0, 1.0, 0.0)
	glBegin(GL_POLYGON);
	glVertex2f(X - 100,Y-100*sin(radians(ANGLE))) #car bottom
	glVertex2f(X - 100,Y-100*sin(radians(ANGLE)) + 60)
	glVertex2f(X + 250,y_2 + 60)
	glVertex2f(X + 250,y_2)
	glEnd()
	
	#car top
	glBegin(GL_POLYGON)
	glVertex2f(X - 50,Y-100*sin(radians(ANGLE)) + 60)
	glVertex2f(X     ,Y + 100)
	glVertex2f(X + 200,y_2 + 100)
	glVertex2f(X + 250,y_2+ 60)
	glEnd()
	
	draw_circle(X,Y)
	y_2=Y + 200*tan(radians(ANGLE))
	draw_circle(x_2,y_2)

def display():
    global X, Y
    create_line()
    draw_car()
    #draw_circle(X + RADIUS * sin(radians(ANGLE)), Y + RADIUS * cos(radians(ANGLE)))
    glutSwapBuffers()
    #glutKeyboardFunc(controls)

def controls(key, x,y):
	global TO_RIGHT,SPEED
	if key == b"d":
		TO_RIGHT = True
	elif key == b"a":
		TO_RIGHT = False
	elif key == b"w":
		SPEED += 1
	elif key == b"s":
		SPEED -= 1
		
		if SPEED < 0:
			SPEED = 0
	elif key == b"h":
		playsound.playsound("./horn.mpeg", block=False)
	
def main():
    get_input()
    print("Creating window...")
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(1360, 768)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("CAR MOVING | Amrutha Dinesh")
    glutDisplayFunc(display)
    glutKeyboardFunc(controls)
    glutTimerFunc(0, update, 0)
    glutIdleFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
