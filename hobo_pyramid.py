"""
This pyramid looks OK but its apex is actually a very small circle.
"""

import cadquery as cq

result = (cq
  .Workplane('XY')
  .rect(4,4)
  .workplane(offset=5)
  .circle(0.000001)
  .loft()
)

shape = result.val()

print(f'Volume: {shape.Volume()}, area: {shape  .Area()}')
