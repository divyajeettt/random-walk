# random-walk

# About random-walk

random-walk is a simple, interactive simulation of two-dimensional [Random Walks](https://en.wikipedia.org/wiki/Random_walk), which is built using [`pygame`](https://www.pygame.org/docs/) in Python. It is a graphical-user interface based project. 

*Date of creation:* `11 August, 2021`

## Features

### class `walk.Walker`

A class `Walker` is defined in the module [`walk.py`](https://github.com/divyajeettt/random-walk/blob/main/walk.py). This models the *dots* that perform the walk on the screen.

### Other features

The following features are provided in the simualtor:

- Ability to change the number of simulations and blocks of the walk
- Ability to view the number of walkers in a *neighbourhood*
- Ability to toggle the visibility of the walkers' tracks
- Ability to toggle the visibility of the walkers' position vectors
- Generation of logs

### Edit the logging settings

To modify the level of the `logger`, modify:

```python
logging.basicConfig(
    filename="random-walk.log", level=logging.INFO, format=LOG_FORMAT
)
```

 on [Line 47](https://github.com/divyajeettt/random-walk/blob/8990397adde141d6f2243ee544b0aa9b07fb2ad0/main.py#L47) of `main.py` to:
 
 ```python
logging.basicConfig(
    filename="random-walk.log", level=LEVEL, format=LOG_FORMAT
)
 ```
 
 where `LEVEL` can be one of:
 - `logging.INFO`
 - `logging.DEBUG`
 - `logging.WARNING`
 - `logging.ERROR`
 - `logging.CRITICAL`

### Edit the number of simulations and blocks

To edit the **number of simulations** of the random-walk, change [Line 28](https://github.com/divyajeettt/random-walk/blob/8990397adde141d6f2243ee544b0aa9b07fb2ad0/main.py#L28) of `main.py` to

```python
# number of random walks to perform (Walkers)
SIMLULTIONS: int = X
```

where `X` is your desired number of simulations.

To edit the number of blocks of the random-walk, change [Line 31](https://github.com/divyajeettt/random-walk/blob/8990397adde141d6f2243ee544b0aa9b07fb2ad0/main.py#L31) of `main.py` to

```python
# number of blocks to perform random walks for
BLOCKS: int = Y
```

where `Y` is your desired number of blocks for the random-walk.

Note that a large number of walkers and blocks is recommended for a good analysis.

## Controls

- Left-click (anywhere on the grid): Display the co-ordinates of that Point
- Right-click (anywhere on the grid): Display the number of Walkers within a Euclidean distance of √2 unit(s) of that Point
- Enter: Advance the Random Walk
- A: Toggle the automation the Random Walk
- L: Log the current state of the Walkers into the log file
- T: Toggle the visibility of the tails (last 50 positions visited) of the Walkers
- V: Toggle the visibility of the Walkers' position Vectors

## Run

To run, clone the repository on your device, navigate to the folder, and execute:

```
python3 main.py
```

## Future plans

- The plot of final positions of the Walkers can be changed to a heat-map based on distance
- A heat-map of the total number of times a point on the grid is visited
- Addition of a GUI starting-window that takes the number of walkers and the number of blocks as input
- The ability to switch off backtracking
