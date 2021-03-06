"""Find the overlap area of 2 triangles
"""
from vedo import Mesh, precision, show
import numpy as np

verts1 = [(1.9, 0.5), (2.1, 0.8), (2.4, 0.4)]
verts2 = [(2.3, 0.8), (1.7, 0.4), (2.1, 0.3)]
faces  = [(0,1,2)]

m1 = Mesh([verts1, faces]).c('g').lw(4).wireframe()
m2 = Mesh([verts2, faces]).c('b').lw(4).wireframe()

a1 = precision(m1.area(),3) + " \mum\^2"
a2 = precision(m2.area(),3) + " \mum\^2"
vig1 = m1.vignette('Triangle 1\nA=' + a1,
                   pt=verts1[1], s=0.012, offset=(0.1,0.05))
vig2 = m2.vignette('Triangle 2\nA=' + a2,
                   pt=verts2[2], s=0.012, offset=(0.1,-0.1))

m3 = m1.clone().wireframe(False).c('tomato').lw(0)

zax = (0,0,1)
v0,v1,v2 = np.insert(np.array(verts2), 2, 0, axis=1)

m3.cutWithPlane(origin=v0, normal=np.cross(zax, v1-v0))
if m3.NPoints():
    m3.cutWithPlane(origin=v1, normal=np.cross(zax, v2-v1))
if m3.NPoints():
    m3.cutWithPlane(origin=v2, normal=np.cross(zax, v0-v2))

txt = __doc__ + "\nArea = " + precision(m3.area(), 3) + " \mum\^2"

show(m1, m2, m3, txt, vig1, vig2, axes=1)
