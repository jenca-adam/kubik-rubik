from rubik._backend import *

c=Cube()

rotate_row(c,2,True)
rotate_row(c,2,True)
print(c)
rotate_face(c,5,True)
print(c)
