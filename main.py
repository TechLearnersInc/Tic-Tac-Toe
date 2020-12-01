import sys
from time import sleep

from OpenGL.GL import *
from OpenGL.GLUT import *

from gui.BoardLines import BoardLines
from gui.LetterO import LetterO, LetterO_State_Change
from gui.LetterX import LetterX, LetterX_State_Change
from MLPlayer import GameStatus, NextMove

# Global Variable
BOARD_STATE: list = [2, 2, 2, 2, 2, 2, 2, 2, 2]


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
    global BOARD_STATE
    key: int = int(key.decode("utf-8"))

    if key == 1 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))
    elif key == 2 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        print(COMPUTER)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))
    elif key == 3 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))
    elif key == 4 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))
    elif key == 5 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))
    elif key == 6 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))
    elif key == 7 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))
    elif key == 8 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))
    elif key == 9 and BOARD_STATE[key - 1] == 2:
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))

    print(BOARD_STATE[0], BOARD_STATE[1], BOARD_STATE[2])
    print(BOARD_STATE[3], BOARD_STATE[4], BOARD_STATE[5])
    print(BOARD_STATE[6], BOARD_STATE[7], BOARD_STATE[8])

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

    # Keyboard
    glutKeyboardFunc(Keyboard_Down)
    glutKeyboardUpFunc(Keyboard_Up)

    # Reshape
    glutReshapeFunc(reshape)

    # Timer
    # glutTimerFunc(1000, timer, 0)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()


if __name__ == '__main__':
    print("Hello World")