import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class GameOfLife(object):

    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        assert x_dim > 0 and y_dim > 0
        assert type(x_dim) == type(y_dim) == int

        self.width = x_dim
        self.height = y_dim
        self.grid_map = np.array([[0] * self.width] * self.height)

    def get_grid(self):
        # Implement a getter method for your grid.
        return self.grid_map

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        for row in self.grid_map[::-1]:
            for elem in row:
                print("{} |".format(str(elem)), end=" ")
            print("\n-" + " -" * ((2 * self.width) - 1))

    def populate_grid(self, coord):
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        for cor in coord:
            x, y = cor
            self.grid_map[y, x] = 1

    def make_step(self):
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        alive_grid = np.array([
            [self.count_neighbour_alive((x, y)) for x in range(self.width)]
            for y in range(self.height)]
        )
        for y in range(self.height):
            for x in range(self.width):
                if alive_grid[y, x] == 3 and self.grid_map[y, x] == 0:
                    self.grid_map[y, x] = 1
                elif (alive_grid[y, x] < 2 or alive_grid[y, x] > 3) and self.grid_map[y, x] == 1:
                    self.grid_map[y, x] = 0

    def make_n_steps(self, n):
        # Implement a method that applies the make_step method n times.
        for i in range(n):
            self.make_step()

    def draw_grid(self):
        # Draw the current state of the grid.
        cmap = ListedColormap(["#ffffff", "#000000"])
        fig, ax = plt.subplots(figsize=(self.width, self.height))
        ax.imshow(self.grid_map, cmap=cmap, interpolation='nearest', origin="lower")
        rows, cols = self.grid_map.shape
        ax.set_xticks(np.arange(-.5, cols, 1), minor=True)
        ax.set_yticks(np.arange(-.5, rows, 1), minor=True)
        ax.grid(which="minor", color="lightgray", linestyle='-', linewidth=0.8)
        ax.tick_params(which='both', bottom=False, left=False, labelbottom=False, labelleft=False)

        plt.tight_layout()
        plt.show()

    def count_neighbour_alive(self, coord):
        x, y = coord
        x_b, x_a = max(x - 1, 0), min(self.width - 1, x + 1)
        y_b, y_a = max(y - 1, 0), min(self.height - 1, y + 1)

        result = {
            (x_b, y_b), (x, y_b), (x_a, y_b),
            (x_b, y), (x_a, y),
            (x_b, y_a), (x, y_a), (x_a, y_a)
        }
        result.discard((x, y))  # remove the value of itself
        return sum([self.grid_map[b, a] for (a, b) in result])


r = GameOfLife(30,30)
r.populate_grid([(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
(16, 14), (16, 15), (16, 17), (16, 18),
(18, 14), (18, 15), (18, 17), (18, 18),
(14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)])
r.draw_grid()
r.make_n_steps(6)
r.draw_grid()