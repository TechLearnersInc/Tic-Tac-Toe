from OpenGL import GL


def BoardLines():
    x: int = 0.1
    y: int = 10
    color: int = 0.35
    placement: int = 3.5

    GL.glPushMatrix()
    GL.glColor3f(color, color, color)

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

    GL.glFlush()


if __name__ == '__main__':
    print("Hello World")