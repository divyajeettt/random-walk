from constants import WIDTH, SIDE, NUM, ORIGIN, HEAD, TAIL, NEAR, Color, Point
import logging
import pygame
import graph
import walk


"""
This is a Random Walk simulator.
In a Random Walk, the direction at each step is chosen randomly. In this case of
Random Walk, backtracking (going back on the same path) is allowed. The data so
collected will be used to analyze the final positions where the Walkers landed.

Controls:
    Press Enter Key to advance the Random Walk
    Press 'A' to toggle the automation the Random Walk
    Press 'L' to log the current state of the Walkers into the log file
    Press 'T' to toggle the visibility of the tails of the Walkers
    Press 'V' to toggle the visibility of the Vector joining the Walkers' heads
    to the Origin
    Left-click anywhere on the grid to display the co-ordinates of that Point
    Right-click anywhere to display the number of Walkers within a Euclidean
        distance of √2 unit(s) near that point
"""


# number of random walks to perform (Walkers)
SIMLULTIONS: int = 100

# number of blocks to perform random walks for
BLOCKS: int = 1000

WINDOW = pygame.display.set_mode((SIDE, SIDE))
FPS: int = 60

# colors
WHITE: Color = (255, 255, 255)
BLACK: Color = (  0,   0,   0)
GRAY:  Color = (190, 190, 190)

WALKERS: list[walk.Walker] = [walk.Walker() for _ in range(SIMLULTIONS)]

pygame.display.set_caption("Random Walk Simulator")


LOG_FORMAT: str = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(
    filename="random_walk.log", level=logging.INFO, format=LOG_FORMAT
)
logger = logging.getLogger()


def draw_lines() -> None:
    """draws the (x, y) grid and Origin (0, 0) on the screen"""

    pygame.draw.circle(WINDOW, BLACK, ORIGIN, 6)

    for i in range(NUM + 1):
        for j in range(2):
            pygame.draw.line(
                WINDOW, GRAY, ((WIDTH*i-1, 0) if j else (0, WIDTH*i-1)),
                ((WIDTH*i-1, SIDE) if j else (SIDE, WIDTH*i-1)), 2
            )

    middle = WIDTH*(NUM//2) - 1
    pygame.draw.line(WINDOW, BLACK, (middle, 0), (middle, SIDE), 3)
    pygame.draw.line(WINDOW, BLACK, (0, middle), (SIDE, middle), 3)


def draw_walkers(tail: bool, vector: bool) -> None:
    """draws the Walkers on the screen
    if tail is True, draw the Walkers with their tail, else without them
    if vector is True, draw the vector joining the Origin to the Walkers"""

    for walker in WALKERS:
        pygame.draw.circle(WINDOW, walker.color, walker.current, HEAD)
        if tail:
            for pos1, pos2 in zip(walker.visited[1::], walker.visited):
                pygame.draw.line(WINDOW, walker.color, pos1, pos2, TAIL)
        if vector:
            pygame.draw.line(WINDOW, walker.color, ORIGIN, walker.current, TAIL)


def draw_near(point: Point, count: int) -> None:
    """draws a circle centered at given position and displays the number of
    Walkers near that point (inside that circle)"""

    pygame.draw.circle(WINDOW, BLACK, point, NEAR, width=2)
    print(f"Number of Walkers near {walk.convert(point, grid=True)}: {count}")


def main() -> None:
    step_counter = 0
    tail, vector, automate = True, False, False

    clock = pygame.time.Clock()

    logger.info(f"initialized random walk for {BLOCKS=}, {SIMLULTIONS=}")

    RUN = True
    while RUN:
        clock.tick(FPS)

        WINDOW.fill(WHITE)
        draw_lines()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            elif event.type == pygame.KEYDOWN:
                if not automate and event.key == pygame.K_RETURN:
                    step_counter += 1
                    walk.walk(WALKERS)

                elif event.key == pygame.K_t:
                    tail = not tail

                elif event.key == pygame.K_a:
                    automate = not automate

                elif event.key == pygame.K_v:
                    vector = not vector

                elif event.key == pygame.K_l:
                    posns = [walk.convert(walker.current) for walker in WALKERS]
                    logger.info(f"Current Positions of Walkers: \n{posns}")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(walk.convert(event.pos, grid=True))

                elif event.button == 3:
                    count = 0
                    for walker in WALKERS:
                        if walk.near(walker.current, event.pos):
                            count += 1
                    draw_near(event.pos, count)

        if automate:
            step_counter += 1
            walk.walk(WALKERS)

        draw_walkers(tail=tail, vector=vector)
        pygame.display.update()

        if step_counter == BLOCKS:
            if SIMLULTIONS != 1:
                graph.analyze1(WALKERS)
            else:
                graph.analyze2(*WALKERS)

            posns = [walk.convert(walker.current) for walker in WALKERS]
            logger.info(f"Final Positions of Walkers: \n{posns}")

            RUN = False


if __name__ == "__main__":
    main()