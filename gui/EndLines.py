from OpenGL import GL


def EndLineDraw(cells: list):
    x: float = 0.3
    y: float = 9.3

    posX = posY = 0

    if cells == [0, 1, 2]:
        x, y = y, x
        posY = 7
    elif cells == [3, 4, 5]:
        x, y = y, x
    elif cells == [6, 7, 8]:
        x, y = y, x
        posY = -7
    elif cells == [0, 3, 6]:
        pass
    elif cells == [1, 4, 7]:
        pass
    elif cells == [2, 5, 8]:
        pass
    elif cells == [0, 4, 8]:
        pass
    elif cells == [0, 4, 6]:
        pass

    GL.glPushMatrix()
    GL.glColor3ub(255, 0, 0)

    GL.glPushMatrix()
    GL.glTranslatef(posX, posY, 0)
    # GL.glRotatef(45, 1, 1, 20)
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