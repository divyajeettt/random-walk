from constants import WIDTH, ORIGIN, NEAR, Color, Point
import random
import math


def convert(point: Point, grid: bool|None = False) -> Point:
    """converts pygame co-ordinates to Cartesian Co-ordinates
    if grid is True, then return the Point as a pair of floats, else of ints"""

    div = "/" if grid else "//"
    return eval(f"[((point[0]-300) {div} WIDTH), ((300-point[1]) {div} WIDTH)]")


def quadrant(point: Point) -> int:
    """returns the Quadrant in which the given Cartesian Point lies
    return value = 0 -> Point lies on an axis, or is the Origin"""

    if 0 in point:
        return 0
    elif point[0] > 0:
        return 1 if point[1] > 0 else 4
    else:
        return 2 if point[1] > 0 else 3


def near(point1: Point, point2: Point) -> bool:
    """returns True if the Euclidean distance of Points is less than or equal to
    one, and False in all other cases"""

    return math.dist(point1, point2) <= NEAR


class Walker:
    """
    represents a Walker used for Random Walk
    attributes:
        self.color: color of the Walker as to be displayed
        self.current: represents the current position of the Walker
        self.visited: list of grid points the Walker has visited
    """

    color: Color
    current: Point
    visited: list[Point, ...]

    def __init__(self) -> None:
        self.color = tuple(random.randrange(256) for _ in range(3))
        self.current = ORIGIN.copy()
        self.visited = [ORIGIN.copy()]

    def walk(self) -> None:
        """updates the previous and current position of the Walker"""

        dx, dy = random.choice(
            [[0, +WIDTH], [0, -WIDTH], [+WIDTH, 0], [-WIDTH, 0]]
        )
        self.current = self.current.copy()
        self.current[0] += dx
        self.current[1] += dy
        self.visited.append(self.current)
        if len(self.visited) > 10:
            self.visited.pop(0)


def walk(walkers: list[Walker]) -> None:
    """advance the random walk by one step"""

    for walker in walkers:
        walker.walk()


def dist(
    walker: Walker|None = None, point: Point|None = None,
    euclidean: bool|None = False, taxicab: bool|None = False
) -> float:
    """point = walker.current if walker is not None else point
    returns the Euclidean / Taxi-Cab distance of the Walker from the
    Origin if the corresponding boolean is True"""

    point = convert(walker.current if point is None else point)
    if euclidean:
        return math.dist(point, [0, 0])
    if taxicab:
        return abs(point[0]) + abs(point[1])