import sys

from OpenGL.GL import *
from OpenGL.GLUT import *

from gui.BoardLines import BoardLines


# Display
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    BoardLines()

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
    print(f"Down \"{key}\"")


def keyboard_up(key: bytes, x: int, y: int):
    key: str = key.decode("utf-8")
    print(f"UP \"{key}\"")


# Main
def main():
    glutInit(sys.argv)

    # Position the window's center
    width = height = 400
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
    # glutTimerFunc(1000, timer, 0)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()


if __name__ == '__main__':
    main()
