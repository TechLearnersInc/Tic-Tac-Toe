import math
from OpenGL import GL


def LetterO_State_Change(key: int):
    LETTER_O_ONE_POSITION: dict = {'X': -7, 'Y': 7}
    LETTER_O_TWO_POSITION: dict = {'X': 0, 'Y': 7}
    LETTER_O_THREE_POSITION: dict = {'X': 7, 'Y': 7}

    LETTER_O_FOUR_POSITION: dict = {'X': -7, 'Y': 0}
    LETTER_O_FIVE_POSITION: dict = {'X': 0, 'Y': 0}
    LETTER_O_SIX_POSITION: dict = {'X': 7, 'Y': 0}

    LETTER_O_SEVEN_POSITION: dict = {'X': -7, 'Y': -7}
    LETTER_O_EIGHT_POSITION: dict = {'X': 0, 'Y': -7}
    LETTER_O_NINE_POSITION: dict = {'X': 7, 'Y': -7}

    if key == 1:
        return LETTER_O_ONE_POSITION
    elif key == 2:
        return LETTER_O_TWO_POSITION
    elif key == 3:
        return LETTER_O_THREE_POSITION
    elif key == 4:
        return LETTER_O_FOUR_POSITION
    elif key == 5:
        return LETTER_O_FIVE_POSITION
    elif key == 6:
        return LETTER_O_SIX_POSITION
    elif key == 7:
        return LETTER_O_SEVEN_POSITION
    elif key == 8:
        return LETTER_O_EIGHT_POSITION
    elif key == 9:
        return LETTER_O_NINE_POSITION


def LetterO(position: dict = {'X': 0, 'Y': 0}):
    GL.glPushMatrix()

    GL.glTranslatef(position.get('X'), position.get('Y'), 0)
    GL.glColor3ub(238, 238, 238)
    GL.glPointSize(4)

    GL.glBegin(GL.GL_POINTS)
    for i in range(1000):
        GL.glVertex3f(
            math.cos(2 * math.pi * (i / 1000)) * 2.1,
            math.sin(2 * math.pi * (i / 1000)) * 2.1, 0)

    GL.glEnd()

    GL.glPopMatrix()


if __name__ == '__main__':
    print("Hello World")