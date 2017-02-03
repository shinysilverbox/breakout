from constants import *
from models import *
from game2d import *

class Bricks(object):
    
    """ Manages the list of bricks, of which each one is created in the Brick class in methods.py.
    Each brick has location, color, size attributes. """

    """def __init__(self, x=0, y=0, linecolor=None, fillcolor=None, left=0, right=0, bottom=0, top=0, scale=1, angle=0, name=None, linewidth=0):
        # values that might go into constants at some point
        self.x = x
        self.y = y
        self.left = self.x - BRICK_WIDTH / 2
        self.right = self.x + BRICK_WIDTH / 2
        self.bottom = self.y - BRICK_HEIGHT / 2
        self.top = self.y + BRICK_HEIGHT / 2
        self.linecolor = linecolor
        self.fillcolor = fillcolor
        self.scale = scale
        self.angle = angle
        self.name = name
        self.linewidth = linewidth
        self.colors_by_row_index = []
        self.bricks = []
        self.sep_h_count = 1
        self.sep_v_count = 0
        self.brick_h_count = 0
        self.brick_v_count = 0"""

    def assign_row_colors(self):
        count = 0
        color_index = 0
        self.colors_by_row_index = []
        for row in range(0, BRICK_ROWS):
            if count < 2:
                self.colors_by_row_index.append(BRICK_COLOR[color_index])
                count = count + 1
            else:
                color_index = color_index + 1
                self.colors_by_row_index.append(BRICK_COLOR[color_index])
                count = 1
        return self.colors_by_row_index

    def set_brick_x_coordinates(self):
        sep_h_count = 1
        brick_h_count = 0
        x_coordinates_by_column_index = []
        for column in range(0, BRICKS_IN_ROW):
            x_coordinates_by_column_index.append((sep_h_count * BRICK_SEP_H) + (brick_h_count * BRICK_WIDTH))
            sep_h_count = sep_h_count + 1
            brick_h_count = brick_h_count + 1
        return x_coordinates_by_column_index
        
    def set_brick_y_coordinates(self):
        sep_v_count = 0
        brick_v_count = 0
        y_coordinates_by_row_index = []
        for row in range(0, BRICK_ROWS):
            y_coordinates_by_row_index.append(GAME_HEIGHT - BRICK_Y_OFFSET - (brick_v_count * BRICK_HEIGHT) - (sep_v_count * BRICK_SEP_V))
            sep_v_count = sep_v_count + 1
            brick_v_count = brick_v_count + 1
        return y_coordinates_by_row_index

    def construct_bricks(self):
        self.bricks = []
        colors_by_row_index = self.assign_row_colors() # this is fine
        #print 'colors_by_row_index == ' + str(colors_by_row_index)
        x_coordinates_by_column_index = self.set_brick_x_coordinates() # this is fine
        #print 'x_coordinates_by_column_index == ' + str(x_coordinates_by_column_index)
        y_coordinates_by_row_index = self.set_brick_y_coordinates() # this is fine
        #print 'y_coordinates_by_row_index == ' + str(y_coordinates_by_row_index)
        #print 'entering for loop, presumably'
        for row in range (0, len(y_coordinates_by_row_index)):
        #    print 'new pass through outer for loop for row ' + str(row)
        #    print 'color == ' + str(color)
            for column in range(0, len(x_coordinates_by_column_index)):
                bricks_per_row = len(x_coordinates_by_column_index)
        #        print 'len(x_coordinates_by_column_index) == ' + str(bricks_per_row)
        #        print 'new pass through inner for loop for column ' + str(column)
                x = x_coordinates_by_column_index[column]
        #        print 'x == ' + str(x)
                y = y_coordinates_by_row_index[row]
        #        print 'y == ' + str(y)
        #        print 'fillcolor = ' + str(fillcolor)
                self.bricks.append(Brick(x_coordinates_by_column_index[column], y_coordinates_by_row_index[row], colors_by_row_index[row]))
        #        print 'bricks[' + str(column) + '] == ' + str(self.bricks[column])
                #bricks.append(Brick(x = x_coordinates_by_column_index[column], y = y_coordinates_by_row_index[row], fillcolor=color))
        #print 'bricks == ' + str(self.bricks)
        return self.bricks

    def getBricks(self):
        print 'self.bricks type is ' + str(type(self.bricks))
        bricks_copy = []
        for brick in self.bricks:
            bricks_copy.append(brick)
        return bricks_copy

    def initialize_bricks(self):
        self.construct_bricks()

    def remove_brick(self, brick):
        print self
        print self.getBricks()
        self.bricks.remove(brick)



    # don't use the index, use the brick object itself
    #pass the brick itself, not the index of the brick
    #unit tests are the things in a6test
    #call the initialize method, 1/4 methods I'm testing

    # Tests:
    #testBricks = Brick()
    #testBricks.initialize_bricks()
    #testBricks.getBricks()

    # 3 things the game needs from bricks methods:
    # get (a copy of) the list of bricks [done]
    # set up/initialize/create the bricks for a new game [done]
    # remove a brick
