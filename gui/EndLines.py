from OpenGL import GL


def EndLineDraw(cells: list):
    x: float = 0.3
    y: float = 9.3
    posX: int = 0
    posY: int = 0
    angle: int = 0

    if cells == [0, 1, 2]:
        x, y = y, x
        posY = 7
    elif cells == [3, 4, 5]:
        x, y = y, x
    elif cells == [6, 7, 8]:
        x, y = y, x
        posY = -7
    elif cells == [0, 3, 6]:
        posX = 0
    elif cells == [1, 4, 7]:
        pass
    elif cells == [2, 5, 8]:
        posX = 7
    elif cells == [0, 4, 8]:
        y = 12
        angle = 45
    elif cells == [2, 4, 6]:
        y = 12
        angle = -45
    else:
        return

    GL.glPushMatrix()
    GL.glColor3ub(69, 90, 100)

    GL.glPushMatrix()
    GL.glTranslatef(posX, posY, 0)
    GL.glRotatef(angle, 1, 1, 20)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-x, -y)
    GL.glVertex2f(x, -y)
    GL.glVertex2f(x, y)
    GL.glVertex2f(-x, y)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPopMatrix()


if __name__ == '__main__':
    print("Hello World")