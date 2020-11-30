import sys

from OpenGL.GL import *
from OpenGL.GLUT import *


def BoardLines():
    x: int = 0.1
    y: int = 10
    distance: int = 3.5
    color: int = 0.35

    glPushMatrix()
    glColor3f(color, color, color)

    glPushMatrix()
    glTranslatef(distance, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-x, -y)
    glVertex2f(x, -y)
    glVertex2f(x, y)
    glVertex2f(-x, y)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-distance, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-x, -y)
    glVertex2f(x, -y)
    glVertex2f(x, y)
    glVertex2f(-x, y)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, distance, 0)
    glBegin(GL_QUADS)
    glVertex2f(-y, -x)
    glVertex2f(y, -x)
    glVertex2f(y, x)
    glVertex2f(-y, x)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -distance, 0)
    glBegin(GL_QUADS)
    glVertex2f(-y, -x)
    glVertex2f(y, -x)
    glVertex2f(y, x)
    glVertex2f(-y, x)
    glEnd()
    glPopMatrix()

    glPopMatrix()

    glFlush()