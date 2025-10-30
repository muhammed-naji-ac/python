# cuboid.py
def area(length, breadth, height):
    """Return the surface area of a cuboid"""
    return 2 * (length*breadth + breadth*height + length*height)

def perimeter(length, breadth, height):
    """Return the perimeter (sum of all edges) of a cuboid"""
    return 4 * (length + breadth + height)
