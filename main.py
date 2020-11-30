import sys

from OpenGL.GL import *
from OpenGL.GLUT import *

from gui.BoardLines import BoardLines
from gui.LetterO import (LetterO, LETTER_O_ONE_POSITION, LETTER_O_TWO_POSITION,
                         LETTER_O_THREE_POSITION, LETTER_O_FOUR_POSITION,
                         LETTER_O_FIVE_POSITION, LETTER_O_SIX_POSITION,
                         LETTER_O_SEVEN_POSITION, LETTER_O_EIGHT_POSITION,
                         LETTER_O_NINE_POSITION)


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


# Keyboard Down
def Keyboard_Down(key: bytes, x: int, y: int):
    key: str = key.decode("utf-8")
    print(f"Down \"{key}\"")


# Keyboard Up
def Keyboard_Up(key: bytes, x: int, y: int):
    key: str = key.decode("utf-8")
    if key == '1':
        LetterO(LETTER_O_ONE_POSITION)
    elif key == '2':
        LetterO(LETTER_O_TWO_POSITION)
    elif key == '3':
        LetterO(LETTER_O_THREE_POSITION)
    elif key == '4':
        LetterO(LETTER_O_FOUR_POSITION)
    elif key == '5':
        LetterO(LETTER_O_FIVE_POSITION)
    elif key == '6':
        LetterO(LETTER_O_SIX_POSITION)
    elif key == '7':
        LetterO(LETTER_O_SEVEN_POSITION)
    elif key == '8':
        LetterO(LETTER_O_EIGHT_POSITION)
    elif key == '9':
        LetterO(LETTER_O_NINE_POSITION)
    else:
        print(f"UP \"{key}\"")

    glutSwapBuffers()


# Main
def main():
    glutInit(sys.argv)

    # Position the window's center
    width = height = 350
    glutInitWindowPosition((glutGet(GLUT_SCREEN_WIDTH) - width) // 2,
                           (glutGet(GLUT_SCREEN_HEIGHT) - height) // 2)
    glutInitWindowSize(width, height)

    # Create a double-buffer RGBA window.   (Single-buffering is possible.
    # So is creating an index-mode window.)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # Create a window, setting its title
    glutCreateWindow('Tic-Tac-Toe')

    # Initialization
    initialize()

    # Set the display callback.  You can set other callbacks for the keyboard and mouse events.
    glutDisplayFunc(display)

    glutKeyboardFunc(Keyboard_Down)
    glutKeyboardUpFunc(Keyboard_Up)

    # Reshape
    glutReshapeFunc(reshape)

    # Timer
    # glutTimerFunc(1000, timer, 0)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()


if __name__ == '__main__':
    main()
