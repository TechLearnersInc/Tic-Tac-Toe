import sys
from time import sleep
from threading import Thread

from OpenGL.GL import *
from OpenGL.GLUT import *

from gui.BoardLines import BoardLines, BoardLinesTimer
from gui.LetterO import LetterO, LetterO_State_Change
from gui.LetterX import LetterX, LetterX_State_Change
from MLPlayer import GameStatus, NextMove

# Global Variable
BOARD_STATE: list = [2 for _ in range(9)]
KEY_PRESSED: bool = False
PRESSED_KEY: bytes = bytes()
GAME_STATUS: bool = True


# Game Reset
def GameReset():
    global BOARD_STATE, KEY_PRESSED, PRESSED_KEY, GAME_STATUS

    BOARD_STATE = [2 for _ in range(9)]
    KEY_PRESSED = False
    PRESSED_KEY = bytes()
    GAME_STATUS = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    BoardLines()
    BoardLinesTimer(reset=True)

    glutPostRedisplay()


# GamePlay
def GamePlay():

    global BOARD_STATE, KEY_PRESSED, PRESSED_KEY, GAME_STATUS

    if KEY_PRESSED and PRESSED_KEY.decode("utf-8") == 'r':
        GameReset()
        return

    if GAME_STATUS is False:
        print('Game Finished')
        return

    if KEY_PRESSED:
        key: int = int(PRESSED_KEY.decode("utf-8"))
        KEY_PRESSED = False
    else:
        return

    glutSwapBuffers()

    def KeyAction():
        global BOARD_STATE
        LetterX(LetterX_State_Change(key))
        BOARD_STATE[key - 1] = 0
        COMPUTER: int = NextMove(BOARD_STATE)
        BOARD_STATE[COMPUTER] = 1
        LetterO(LetterO_State_Change(COMPUTER + 1))

    if key == 1 and BOARD_STATE[key - 1] == 2:
        KeyAction()
    elif key == 2 and BOARD_STATE[key - 1] == 2:
        KeyAction()
    elif key == 3 and BOARD_STATE[key - 1] == 2:
        KeyAction()
    elif key == 4 and BOARD_STATE[key - 1] == 2:
        KeyAction()
    elif key == 5 and BOARD_STATE[key - 1] == 2:
        KeyAction()
    elif key == 6 and BOARD_STATE[key - 1] == 2:
        KeyAction()
    elif key == 7 and BOARD_STATE[key - 1] == 2:
        KeyAction()
    elif key == 8 and BOARD_STATE[key - 1] == 2:
        KeyAction()
    elif key == 9 and BOARD_STATE[key - 1] == 2:
        KeyAction()

    print(BOARD_STATE[0], BOARD_STATE[1], BOARD_STATE[2])
    print(BOARD_STATE[3], BOARD_STATE[4], BOARD_STATE[5])
    print(BOARD_STATE[6], BOARD_STATE[7], BOARD_STATE[8])


# Display
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    BoardLines()
    GamePlay()

    glutSwapBuffers()


# Reshaping
def reshape(width: GLsizei, height: GLsizei):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)


# Timer
def timer(_: int):
    global GAME_STATUS, WINDOWS_TITLE

    glutTimerFunc(1000 // 60, timer, 0)

    if BoardLinesTimer(reset=False):
        glutPostRedisplay()

    if GameStatus(BOARD_STATE).get('Winner') is not None:
        GAME_STATUS = False
    else:
        GAME_STATUS = True


# Initialization
def initialize():
    glClearColor(28 / 255, 170 / 255, 156 / 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)


# Keyboard Down
def Keyboard_DOWN(key: bytes, x: int, y: int):
    # key: str = key.decode("utf-8")
    # print(f"Down \"{key}\"")
    pass


# Keyboard Up
def Keyboard_UP(key: bytes, x: int, y: int):
    global KEY_PRESSED, PRESSED_KEY
    KEY_PRESSED = True
    PRESSED_KEY = key
    print(f"Up \"{key}\"")

    glutPostRedisplay()


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
    glutCreateWindow('Tic Tac Toe (You\'re X)')

    # Initialization
    initialize()

    # Set the display callback.  You can set other callbacks for the keyboard and mouse events.
    glutDisplayFunc(display)

    # Keyboard
    glutKeyboardUpFunc(Keyboard_UP)
    glutKeyboardFunc(Keyboard_DOWN)

    # Reshape
    glutReshapeFunc(reshape)

    # Timer
    glutTimerFunc(1000, timer, 0)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()


if __name__ == '__main__':
    main()