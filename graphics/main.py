from twod.rectangle import area as ra
from twod.rectangle import perimeter as pe
from twod.circle import area
from twod.circle import perimeter
from twod.threed.cuboid import area as ca
from twod.threed.cuboid import perimeter as cp
from twod.threed.sphere import area as sa
from twod.threed.sphere import area as sp

print("Rectangle area:", ra(10, 5))
print("Rectangle perimeter:", pe(10, 5))

print("Circle area:", area(7))
print("Circle perimeter:", perimeter(7))

print("Cuboid area:", ca(2, 3, 4))
print("Cuboid perimeter:", cp(2, 3, 4))

print("Sphere area:", sa(5))
print("Sphere perimeter:", sp(5))
