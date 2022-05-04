from .helpers.lists import const,dupl
import re
import numpy as np
import random

TRANS_PATTERN=re.compile("^([RrMLlEUuSDdxFfyBbz])('?)$")
transs="RrMLlEUuSDdxFfyBbz"
def rotate_face(cube,i,reverse=False):
    face=cube[i]
    face=np.rot90(face)
    if not reverse:
        face=np.rot90(np.rot90(face))
    cube[i]=face
    
def rotate_column(cube,i,reverse=False):
    column=[cube[0][x][i] for x in range(3)]
    l=[4,5,1,0] if reverse else [1,5,4,0]
    for ix in l:
        col=column
        column=[cube[ix][x][i] for x in range(3)]
        for a,j in enumerate(col):
            cube[ix][a][i]=j
def rotate_row(cube,i,reverse=False):
    row=cube[4][i]
    l = [2,1,3,4] if (not reverse) else [3,1,2,4]
    for ix in l:
        rw=dupl(row)
        row=dupl(cube[ix][i])
        cube[ix][i]=dupl(rw)
def rotate_zrow(cube,i,reverse=False):
    row=cube[0][i]
    l = [3,5,2,0] if (not reverse) else [2,5,3,0]
    for ix in l:
        rw=dupl(row)
        row=dupl(cube[ix][i])
        cube[ix][i]=dupl(rw)

def rotate_columns(cube,columns,reverse=False):
    for column in columns:
        rotate_column(cube,column,reverse)
def rotate_rows(cube,rows,reverse=False):
    for row in rows:
        rotate_row(cube,row,reverse)
def rotate_zrows(cube,zrows,reverse=False):
    for zrow in zrows:
        rotate_zrow(cube,zrow,reverse)
class Transformation:
    def __init__(self,n):
        m=TRANS_PATTERN.search(n)
        if m is None:
            raise ValueError(f"invalid transformation: {m}, please note that 2 on the end of transformation is not allowed")
        g=m.groups()
        self.type,self.reverse=g
        self.reverse = self.reverse == "'"
    def apply(self,cube):
        if self.type=='R':
            rotate_face(cube,3,self.reverse)
            rotate_column(cube,2,self.reverse)
        elif self.type=='r':
            rotate_face(cube,3,self.reverse)
            rotate_columns(cube,[1,2],self.reverse)
        elif self.type=='M':
            rotate_column(cube,1,not self.reverse)
        elif self.type=='L':
            rotate_face(cube,2,not self.reverse)
            rotate_column(cube,0,not self.reverse)
        elif self.type == 'l':
            rotate_face(cube,2,not self.reverse)
            rotate_columns(cube,[0,1],not self.reverse)
        elif self.type == 'x':
            rotate_face(cube,2,self.reverse)
            rotate_face(cube,3,self.reverse)
            rotate_columns(cube,[0,1,2],self.reverse)
        elif self.type == 'U':
            rotate_face(cube,0,self.reverse)
            rotate_row(cube,0,self.reverse)
        elif self.type == 'u':
            rotate_face(cube,0,self.reverse)
            rotate_rows(cube,[0,1],self.reverse)
        elif self.type == 'D':
            rotate_face(cube,4,not self.reverse)
            rotate_row(cube,2,not self.reverse)
        elif self.type == 'd':
            rotate_face(cube,4,not self.reverse)
            rotate_rows(cube,[1,2], not self.reverse)
        elif self.type == 'E':
            rotate_row(cube,1,not self.reverse)
        elif self.type == 'y':
            rotate_rows(cube,[0,1,2], self.reverse)
            rotate_face(cube,0,self.reverse)
            rotate_face(cube,4,self.reverse)
        elif self.type == 'F' :
            rotate_zrow(cube,2,self.reverse)
            rotate_face(cube,4,self.reverse)
        elif self.type == 'f':
            rotate_zrows(cube,[1,2],self.reverse)
            rotate_face(cube,4,self.reverse)
        elif self.type == 'B':
            rotate_zrow(cube,0,not self.reverse)
            rotate_face(cube,1,not self.reverse)
        elif self.type == 'b':
            rotate_zrows(cube,[0,1],not self.reverse)
            rotate_face(cube,1,not self.reverse)
        elif self.type == "S":
            rotate_zrow(cube,1,self.reverse)
        elif self.type == "z":
            rotate_zrows(cube,[0,1,2], self.reverse)
            rotate_face(cube,1,self.reverse)
            rotate_face(cube,4,self.reverse)

        else:
            raise NotImplementedError
class Cube:
    def __init__(self):
        self.faces=np.array([const(i,9) for i in "wgroby"])
    def transform(self,tr):
        Transformation(tr).apply(self)
    def run(self,alg):
        for x in alg.split():
            self.transform(x)
    def scramble(self):
        nmoves=random.randrange(50,100)
    
        moves=random.choices(transs,k=nmoves)
        for move in moves:
            self.transform(move)
    def __setitem__(self,ix,i):
        self.faces[ix]=i
    def __getitem__(self,ix):
        return self.faces[ix]
    def __repr__(self):
        return repr(self.faces) 

