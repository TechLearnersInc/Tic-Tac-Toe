import sys

from OpenGL.GL import *
from OpenGL.GLUT import *

ANIMATION_VARS: dict = {"STATE": True, "Angle": 0, "AngleChangeRate": 0.0}


def RectangleCircleShape():
    global ANIMATION_VARS
    glPushMatrix()
    glRotatef(ANIMATION_VARS.get('Angle'), 0, 0, 1)
    glPushMatrix()

    a, b, c = 0.1, 10, 0.5

    for i in range(18):
        glRotatef(20, 0, 0, 1)

        glBegin(GL_POLYGON)

        glColor3f(a, b, c)
        glVertex3f(0, 0, 0.0)

        glColor3f(a, c, b)
        glVertex3f(2, 0, 0.0)

        glColor3f(b, c, a)
        glVertex3f(2, 6, 0.0)

        glColor3f(a, b, c)
        glVertex3f(0, 6, 0.0)

        glEnd()

    glPopMatrix()
    glPopMatrix()


def TriangleCircleShape():
    global ANIMATION_VARS
    glPushMatrix()
    glRotatef(ANIMATION_VARS.get('Angle'), 0, 0, 1)
    glPushMatrix()

    for i in range(18):
        glRotatef(20, 0, 0, 1)
        glBegin(GL_POLYGON)

        glColor3f(1, 1, 1)
        glVertex3f(0, 6, 0)

        glColor3f(1, 1, 0)
        glVertex3f(2, 6, 0)

        glColor3f(0, 1, 1)
        glVertex3f(1, 7, 0)
        glEnd()

    glPopMatrix()
    glPopMatrix()


# Timer
def timer(_: int):
    glutPostRedisplay()
    glutTimerFunc(1000 // 100, timer, 0)

    global ANIMATION_VARS

    if ANIMATION_VARS.get('STATE'):
        if ANIMATION_VARS.get('Angle') < 360:
            ANIMATION_VARS['Angle'] += ANIMATION_VARS.get('AngleChangeRate')
            ANIMATION_VARS['AngleChangeRate'] += 0.0025
        else:
            ANIMATION_VARS['STATE'] = False

    else:
        if ANIMATION_VARS.get('Angle') > 0:
            ANIMATION_VARS['Angle'] -= ANIMATION_VARS.get('AngleChangeRate')
            ANIMATION_VARS['AngleChangeRate'] -= 0.0025
        else:
            ANIMATION_VARS['STATE'] = True


# Display
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    TriangleCircleShape()
    RectangleCircleShape()

    glutSwapBuffers()


# Reshaping
def reshape(w: GLsizei, h: GLsizei):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)


# Initialization
def initialize():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)


def keyboard_down(key: bytes, x: int, y: int):
    key: str = key.decode("utf-8")
    print(f"Pressed DOWN Func \"{key}\"")


def keyboard_up(key: bytes, x: int, y: int):
    global ANIMATION_VARS
    rate: int = 0.5
    key: str = key.decode("utf-8")
    if key == 'u':
        ANIMATION_VARS['AngleChangeRate'] += rate
        print(f"Speeding UP \"{key}\"")
    elif key == 'd':
        if ANIMATION_VARS['AngleChangeRate'] > 0:
            ANIMATION_VARS['AngleChangeRate'] -= rate
            print(f"Speeding Down \"{key}\"")
        else:
            print(f"[0] Speeding Down \"{key}\"")
    elif key == 'r':
        print(f"Speed Reset \"{key}\"")
        ANIMATION_VARS['AngleChangeRate'] = 0


# Main
def main():
    glutInit(sys.argv)

    # Position the window's center
    width = height = 512
    glutInitWindowPosition((glutGet(GLUT_SCREEN_WIDTH) - width) // 2,
                           (glutGet(GLUT_SCREEN_HEIGHT) - height) // 2)
    glutInitWindowSize(width, height)

    # Create a double-buffer RGBA window.   (Single-buffering is possible.
    # So is creating an index-mode window.)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # Create a window, setting its title
    glutCreateWindow('Flower Shape Circle')

    # Initialization
    initialize()

    # Set the display callback.  You can set other callbacks for the keyboard and mouse events.
    glutDisplayFunc(display)

    glutKeyboardFunc(keyboard_down)
    glutKeyboardUpFunc(keyboard_up)

    # Reshape
    glutReshapeFunc(reshape)

    # Timer
    glutTimerFunc(1000, timer, 0)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()


if __name__ == '__main__':
    main()
