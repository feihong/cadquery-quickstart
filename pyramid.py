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

def get_face_vertices(polygon : cq.occ_impl.shapes.Face, apex):
    # Vertices for base
    yield [v.Center() for v in polygon.Vertices()]

    for edge in polygon.Edges():
        # Vertices for triangle formed by edge and apex
        yield [apex, *(v.Center() for v in edge.Vertices())]

ngon = cq.Sketch().regularPolygon(radius, sides).val()
face_vertices = get_face_vertices(ngon, apex)
faces = [cq.Face.makeFromWires(cq.Wire.makePolygon(vs, close=True)) for vs in face_vertices]

# Sew the faces into a shell, then make a solid
shell = cq.Shell.makeShell(faces)
pyramid = cq.Solid.makeSolid(shell)

print(f'Volume: {pyramid.Volume()}, area: {pyramid.Area()}')
