import matplotlib.pyplot as plt
import walk


def analyze1(walkers: list[walk.Walker]) -> None:
    """detailed analysis of the conducted Random Walk
    Plot-1: Euclidean Distance of Walkers from the Origin vs no. of Walkers
    Plot-2: number of Walkers that land in each quadrant
    Plot-3: Taxi-Cab Distance of Walkers from the Origin vs no. of Walkers
    PLot-4: final positions of all the Walkers"""

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

    for ax in (axes := (ax1, ax2, ax3, ax4)):
        ax.axhline(y=0, color="black", linewidth=3)
        ax.axvline(x=0, color="black", linewidth=3)
        ax.plot(0, 0, color="black", linewidth=3, marker="o")
        ax.grid(True)

    functions = (euclidean, quadrants, taxicab, positions)
    for analysis, ax in zip(functions, axes):
        analysis(walkers, ax=ax)

    plt.show()


def euclidean(walkers: list[walk.Walker], ax: plt.axes) -> None:
    """histogram: the Euclidean Distance of the Walkers from the Origin by the
    number of Walkers in each integral interval, marked with the mean distance
    of the Walkers from the Origin"""

    distances = [walk.dist(walker=walker, euclidean=True) for walker in walkers]
    mean = sum(distances) / len(distances)

    ax.hist(distances, bins=range(int(max(distances)) + 1))
    ax.axvline(
        x=mean, color="red", linewidth=2, linestyle="--", label="Mean Distance"
    )

    ax.set_xlabel("Euclidean Distance from Origin")
    ax.set_ylabel("Number of Walkers")
    ax.legend()


def quadrants(walkers: list[walk.Walker], ax: plt.axes) -> None:
    """bar graph: the number of Walkers that land in each quadrant
    quadrant = 0 -> Walker landed on an axis, or on the origin"""

    quads = [0, 0, 0, 0, 0]
    for walker in walkers:
        quads[walk.quadrant(walk.convert(walker.current))] += 1

    ax.bar(range(5), quads, width=0.5, edgecolor="black")

    ax.set_xlabel("Quadrant (Ⅰ - Ⅳ)")
    ax.set_ylabel("Number of Walkers")


def taxicab(walkers: list[walk.Walker], ax: plt.axes) -> None:
    """line plot: the Taxi-Cab Distance of the Walkers from the Origin by the
    number of Walkers at each integral distance, marked with the mean distance
    of the Walkers from the Origin"""

    distances = [walk.dist(walker=walker, taxicab=True) for walker in walkers]
    counts = [distances.count(dist) for dist in range(max(distances) + 1)]
    mean = sum(distances) / len(distances)

    ax.plot(range(max(distances) + 1), counts, linewidth=2)
    ax.axvline(
        x=mean, color="red", linewidth=2, linestyle="--", label="Mean Distance"
    )

    ax.set_xlabel("Taxi-Cab Distance from Origin")
    ax.set_ylabel("Number of Walkers")
    ax.legend()


def positions(walkers: list[walk.Walker], ax: plt.axes) -> None:
    """scatter plot: the final positions of the Walkers as a graph"""

    for walker in walkers:
        ax.plot(*walk.convert(walker.current), linewidth=2, marker=".")

    ax.set_xlabel("X - Axis")
    ax.set_ylabel("Y - Axis")


def analyze2(walker: walk.Walker) -> None:
    """detailed analysis of the conducted Random Walk
    Plot-1: Euclidean Distance of the Walker from the Origin by no. of blocks
    Plot-2: Mean Euclidean Distance of the Walker by no. of blocks
    Plot-3: Taxi-Cab Distance of the Walker from the Origin by no. of blocks
    PLot-4: Mean Taxi-Cab Distance of the Walker by no. of blocks"""

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

    for ax in (ax1, ax2, ax3, ax4):
        ax.axhline(y=0, color="black", linewidth=3)
        ax.axvline(x=0, color="black", linewidth=3)
        ax.plot(0, 0, color="black", linewidth=3, marker="o")
        ax.set_xlabel("Number of Blocks")
        ax.grid(True)

    points = [walk.convert(point) for point in walker.visited]

    dist1 = [walk.dist(point=point, euclidean=True) for point in walker.visited]
    mean1 = sum(dist1) / len(dist1)

    ax1.plot(range(1, len(dist1)+1), dist1, linewidth=2)
    ax1.axhline(
        y=mean1, color="red", linewidth=2, linestyle="--", label="Mean Distance"
    )

    dist2 = [walk.dist(point=point, taxicab=True) for point in walker.visited]
    mean2 = sum(dist2) / len(dist2)

    ax3.plot(range(1, len(dist2)+1), dist2, linewidth=2)
    ax3.axhline(
        y=mean2, color="red", linewidth=2, linestyle="--", label="Mean Distance"
    )

    y1 = [sum(dist1[:i]) / i for i in range(1, len(dist1)+1)]
    y2 = [sum(dist2[:i]) / i for i in range(1, len(dist2)+1)]

    ax2.plot(range(len(dist1)), y1, linewidth=2)
    ax4.plot(range(len(dist2)), y2, linewidth=2)

    ax1.set_ylabel("Euclidean Distance")
    ax2.set_ylabel("Mean Euclidean Distance")
    ax3.set_ylabel("Taxi-Cab Distance")
    ax4.set_ylabel("Mean Taxi-Cab Distance")

    ax1.legend(loc="upper left")
    ax3.legend(loc="upper left")
    plt.show()
