from OpenGL import GL


def BoardLines():
    x: int = 0.1
    y: int = 10
    distance: int = 3.5
    color: int = 0.35

    GL.glPushMatrix()
    GL.glColor3f(color, color, color)

    GL.glPushMatrix()
    GL.glTranslatef(distance, 0, 0)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-x, -y)
    GL.glVertex2f(x, -y)
    GL.glVertex2f(x, y)
    GL.glVertex2f(-x, y)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPushMatrix()
    GL.glTranslatef(-distance, 0, 0)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-x, -y)
    GL.glVertex2f(x, -y)
    GL.glVertex2f(x, y)
    GL.glVertex2f(-x, y)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPushMatrix()
    GL.glTranslatef(0, distance, 0)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-y, -x)
    GL.glVertex2f(y, -x)
    GL.glVertex2f(y, x)
    GL.glVertex2f(-y, x)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPushMatrix()
    GL.glTranslatef(0, -distance, 0)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(-y, -x)
    GL.glVertex2f(y, -x)
    GL.glVertex2f(y, x)
    GL.glVertex2f(-y, x)
    GL.glEnd()
    GL.glPopMatrix()

    GL.glPopMatrix()

    GL.glFlush()
