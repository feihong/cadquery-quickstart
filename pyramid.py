"""
You can use this to generate pyramids with any kind of regular polygon as the base.
"""

import math
import itertools
import cadquery as cq

# Parameters
radius = 2 * math.sqrt(2)
height = 5
sides = 4

# Apex point
apex = cq.Vector(0, 0, height)

ngon = cq.Sketch().regularPolygon(radius, sides).val()
base_corner_points = [v.Center() for v in ngon.Vertices()]
print([(v.x,v.y) for v in base_corner_points])

face_vertices = itertools.chain(
    itertools.pairwise(base_corner_points),
    [(base_corner_points[-1], base_corner_points[0])])
face_vertices = [vs + (apex,) for vs in face_vertices] + [base_corner_points]

# for vs in face_vertices:
#     print(vs)

faces = [cq.Face.makeFromWires(cq.Wire.makePolygon(vs, close=True)) for vs in face_vertices]

# Sew the faces into a shell, then make a solid
shell = cq.Shell.makeShell(faces)
pyramid = cq.Solid.makeSolid(shell)

print(f'Volume: {pyramid.Volume()}, area: {pyramid.Area()}')
