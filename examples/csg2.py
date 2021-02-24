import sys
import gmsh

from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Plane
from compas.geometry import Sphere
from compas.geometry import Cylinder
from compas.geometry import Box
from compas.geometry import Torus
from compas.geometry import Capsule

from compas.datastructures import Mesh
from compas.utilities import rgb_to_hex

from compas_view2.app import App
from compas_gmsh.model import Model

# ==============================================================================
# Geometry
# ==============================================================================

R = 1.4

O = Point(0, 0, 0)
X = Vector(1, 0, 0)
Y = Vector(0, 1, 0)
Z = Vector(0, 0, 1)
YZ = Plane(O, X)
ZX = Plane(O, Y)
XY = Plane(O, Z)

box = Box.from_width_height_depth(2 * R, 2 * R, 2 * R)
sphere = Sphere(O, 1.25 * R)

cylinderx = Cylinder((YZ, 0.7 * R), 4 * R)
cylindery = Cylinder((ZX, 0.7 * R), 4 * R)
cylinderz = Cylinder((XY, 0.7 * R), 4 * R)

# ==============================================================================
# Solid Model
# ==============================================================================

model = Model(name="boolean")
model.length_min = 0.5
model.length_max = 1.0

BOX = model.add_box(box)
SPHERE = model.add_sphere(sphere)
CX = model.add_cylinder(cylinderx)
CY = model.add_cylinder(cylindery)
CZ = model.add_cylinder(cylinderz)

I = model.boolean_intersection(BOX, SPHERE)
U = model.boolean_union(model.boolean_union(CX, CY), CZ)
D = model.boolean_difference(I, U)

model.generate_mesh(2)
model.refine_mesh()

# ==============================================================================
# COMPAS mesh
# ==============================================================================

mesh = model.mesh_to_compas()

# ==============================================================================
# Visualization with viewer
# ==============================================================================

viewer = App()

viewer.add(mesh)
viewer.run()