import math
from OpenGL import GL

LETTER_O_ONE_POSITION: dict = {'X': -7, 'Y': 7}
LETTER_O_TWO_POSITION: dict = {'X': 0, 'Y': 7}
LETTER_O_THREE_POSITION: dict = {'X': 7, 'Y': 7}

LETTER_O_FOUR_POSITION: dict = {'X': -7, 'Y': 0}
LETTER_O_FIVE_POSITION: dict = {'X': 0, 'Y': 0}
LETTER_O_SIX_POSITION: dict = {'X': 7, 'Y': 0}

LETTER_O_SEVEN_POSITION: dict = {'X': -7, 'Y': -7}
LETTER_O_EIGHT_POSITION: dict = {'X': 0, 'Y': -7}
LETTER_O_NINE_POSITION: dict = {'X': 7, 'Y': -7}


def LetterO(position: dict = {'X': 0, 'Y': 0}):
    GL.glPushMatrix()

    GL.glTranslatef(position.get('X'), position.get('Y'), 0)
    GL.glColor3f(0.7, 0.7, 0)
    GL.glPointSize(3)

    GL.glBegin(GL.GL_POINTS)
    for i in range(1000):
        GL.glVertex3f(
            math.cos(2 * math.pi * i / 1000) * 2.2,
            math.sin(2 * math.pi * i / 1000) * 2.2, 0)

    GL.glEnd()
    GL.glFlush()

    GL.glPopMatrix()
