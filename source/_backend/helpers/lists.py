import copy
import numpy
def const(j,t):
    return numpy.array(list(zip(*(iter(const_l(j,t)),) * 3)))
def const_l(j,t):
    return [copy.copy(j) for _ in range(t)]
def dupl(r):
    return [copy.copy(i) for i in r]
