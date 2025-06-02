"""
This pyramid takes more effort to construct, but it's more accurate than the hobo pyramid.
"""

import cadquery as cq

# Parameters
base = 4
height = 5
half = base / 2

# Base corner points
p1 = cq.Vector(-half, -half, 0)
p2 = cq.Vector(half, -half, 0)
p3 = cq.Vector(half, half, 0)
p4 = cq.Vector(-half, half, 0)

# Apex point
apex = cq.Vector(0, 0, height)

# Create triangular faces
faces = [
    cq.Face.makeFromWires(cq.Wire.makePolygon([p1, p2, apex, p1])),
    cq.Face.makeFromWires(cq.Wire.makePolygon([p2, p3, apex, p2])),
    cq.Face.makeFromWires(cq.Wire.makePolygon([p3, p4, apex, p3])),
    cq.Face.makeFromWires(cq.Wire.makePolygon([p4, p1, apex, p4])),
    cq.Face.makeFromWires(cq.Wire.makePolygon([p1, p2, p3, p4, p1]))
]

# Sew the faces into a shell, then make a solid
shell = cq.Shell.makeShell(faces)
pyramid = cq.Solid.makeSolid(shell)

print(f'Volume: {pyramid.Volume()}, area: {pyramid.Area()}')
