from OpenGL import GL
from OpenGL import GLUT

BOARD_LINE_X: float = 0.2  # Perfect in 0.2
BOARD_LINE_Y: float = 10  # Perfect in 10
BOARD_PLACEMENT: float = 0  # Perfect in 3.5
BOARD_PLACEMENT_CHANGE_RATE: float = 0.1


def BoardLines():
    global BOARD_LINE_X
    global BOARD_LINE_Y
    global BOARD_PLACEMENT

    x: float = BOARD_LINE_X
    y: float = BOARD_LINE_Y
    placement: float = BOARD_PLACEMENT

    GL.glPushMatrix()
    GL.glColor3ub(23, 145, 135)

    GL.glPushMatrix()
    GL.glTranslatef(placement, 0, 0)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-x, -y)
    GL.glVertex2f(x, -y)
    GL.glVertex2f(x, y)
    GL.glVertex2f(-x, y)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPushMatrix()
    GL.glTranslatef(-placement, 0, 0)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-x, -y)
    GL.glVertex2f(x, -y)
    GL.glVertex2f(x, y)
    GL.glVertex2f(-x, y)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPushMatrix()
    GL.glTranslatef(0, placement, 0)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-y, -x)
    GL.glVertex2f(y, -x)
    GL.glVertex2f(y, x)
    GL.glVertex2f(-y, x)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPushMatrix()
    GL.glTranslatef(0, -placement, 0)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-y, -x)
    GL.glVertex2f(y, -x)
    GL.glVertex2f(y, x)
    GL.glVertex2f(-y, x)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPopMatrix()


def BoardLinesTimer():
    global BOARD_PLACEMENT
    global BOARD_PLACEMENT_CHANGE_RATE

    if BOARD_PLACEMENT <= 3.5:
        BOARD_PLACEMENT += BOARD_PLACEMENT_CHANGE_RATE
        return True
    else:
        return False


if __name__ == '__main__':
    print("Hello World")