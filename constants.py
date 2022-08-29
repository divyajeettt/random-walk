"""
Constants required in the project.
Required constants to be imported in each file.
"""


# Type Aliases
Color = tuple[int, int, int]
Point = list[float, float]

# width of each integer gap on the number-line grid
WIDTH: int = 10

# side of the screen
SIDE: int = 600

# total number of boxes that form in the grid
NUM: int = SIDE // WIDTH

# center of the screen, in pygame co-ordinates
ORIGIN: Point = [SIDE//2, SIDE//2]

# size of the head of each Walker
HEAD: int = 4

# size of the tail of each Walker
TAIL: int = 2

# distance to consider 'near' in distance comparison
NEAR: float = WIDTH * 2**0.5