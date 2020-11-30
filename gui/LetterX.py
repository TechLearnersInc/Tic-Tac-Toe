from OpenGL import GL

LETTER_X_ONE_POSITION: dict = {'X': -7, 'Y': 7}
LETTER_X_TWO_POSITION: dict = {'X': 0, 'Y': 7}
LETTER_X_THREE_POSITION: dict = {'X': 7, 'Y': 7}

LETTER_X_FOUR_POSITION: dict = {'X': -7, 'Y': 0}
LETTER_X_FIVE_POSITION: dict = {'X': 0, 'Y': 0}
LETTER_X_SIX_POSITION: dict = {'X': 7, 'Y': 0}

LETTER_X_SEVEN_POSITION: dict = {'X': -7, 'Y': -7}
LETTER_X_EIGHT_POSITION: dict = {'X': 0, 'Y': -7}
LETTER_X_NINE_POSITION: dict = {'X': 7, 'Y': -7}


def LetterX(position: dict):
    x: int = 0.2
    y: int = 3.0

    GL.glPushMatrix()
    GL.glTranslatef(position.get('X'), position.get('Y'), 0)
    GL.glColor3f(0.7, 0.7, 0)

    GL.glPushMatrix()
    GL.glRotatef(45, 5, 1, -10)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-x, -y)
    GL.glVertex2f(x, -y)
    GL.glVertex2f(x, y)
    GL.glVertex2f(-x, y)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPushMatrix()
    GL.glRotatef(45, 5, 1, 10)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-x, -y)
    GL.glVertex2f(x, -y)
    GL.glVertex2f(x, y)
    GL.glVertex2f(-x, y)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPopMatrix()
    GL.glFlush()