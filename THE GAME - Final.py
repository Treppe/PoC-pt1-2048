"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def slide(line):
    """
    Function slides a single row of column in 2048
    """
    slide_line = []
    for num in line:
        if num != 0:
            slide_line.append(num)
    
    dif_size = len(line) - len(slide_line)
    for gap in range(dif_size):
        slide_line.append(0)
    return slide_line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    slide_line = slide(line)
    for idx in range(len(slide_line)):
        if idx != len(slide_line) - 1 and slide_line[idx] == slide_line[idx+1] and slide_line[idx] != 0:
            slide_line[idx] = 2 * slide_line[idx]
            slide_line[idx+1] = 0
            idx += 1
    slide_line = slide(slide_line)        
    return slide_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.grid = []
        self.init_tiles = {UP: [(0, col_idx) for col_idx in range(self.width)],
                           DOWN: [(self.height - 1, col_idx) for col_idx in range(self.width)], 
                           LEFT: [(row_idx, 0) for row_idx in range(self.height)],
                           RIGHT: [(row_idx, self.width - 1) for row_idx in range(self.height)]}
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.width)]
                        for row in range(self.height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        is_changed = False
        if direction == LEFT or direction == RIGHT:
            line_len = self.width
        else:
            line_len = self.height
        for init_tile in self.init_tiles[direction]:
            moving_line = []
            for i in range(line_len):
                moving_line.append(self.grid[init_tile[0] + i*OFFSETS[direction][0]][init_tile[1] + i*OFFSETS[direction][1]])
            moving_line = merge(moving_line)
            for i in range(line_len):
                cell_in_grid = self.grid[init_tile[0] + i*OFFSETS[direction][0]][init_tile[1] + i*OFFSETS[direction][1]]
                if cell_in_grid != moving_line[i]:
                    is_changed = True
                self.grid[init_tile[0] + i*OFFSETS[direction][0]][init_tile[1] + i*OFFSETS[direction][1]] = moving_line[i]
                    
        if is_changed:
            self.new_tile()
           

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        # make a list of null cells indexes
        null_idx_list = []
        for row_idx in range(self.height):
            for col_idx in range(self.width):
                cell_val = self.grid[row_idx][col_idx]
                if cell_val == 0:
                    null_idx_list.append([row_idx, col_idx])
                    
        # ceate a proportion list of "2" and "4" values
        rand_roll_list = []
        for step in range(10):
            if step == 9:
                rand_roll_list.append(4)
            else:
                rand_roll_list.append(2) 
                
        # create a tile randomy and set it random value in right proportion
        if null_idx_list != []:
            rand_cell_idx = random.choice(null_idx_list)
            self.grid[rand_cell_idx[0]][rand_cell_idx[1]] = random.choice(rand_roll_list)  

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
print TwentyFortyEight(4, 4)
