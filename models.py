# models.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Models module for Breakout

This module contains the model classes for the Breakout game. That is anything that you
interact with on the screen is model: the paddle, the ball, and any of the bricks.

Technically, just because something is a model does not mean there has to be a special 
class for it.  Unless you need something special, both paddle and individual bricks could
just be instances of GRectangle.  However, we do need something special: collision 
detection.  That is why we have custom classes.

You are free to add new models to this module.  You may wish to do this when you add
new features to your game.  If you are unsure about whether to make a new class or 
not, please ask on Piazza."""
import random # To randomly generate the ball velocity

from constants import *
from game2d import *
from bricks import *



# PRIMARY RULE: Models are not allowed to access anything except the module constants.py.
# If you need extra information from Play, then it should be a parameter in your method, 
# and Play should pass it as a argument when it calls the method.


class Paddle(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball, as well as move it
    left and right.  You may wish to add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    # inherited attributes: x, y, width, height, linecolor, fillcolor
    def __init__():
        pass

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A NEW PADDLE
    
    # METHODS TO MOVE THE PADDLE AND CHECK FOR COLLISIONS
    def collides(self, ball):
        # returns True if the ball has collided with this paddle
        pass
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Brick(GRectangle):
    """An instance is a single brick object.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    def __init__(self, xx, yy, color_string):
        # print 'color_string == ' + str(color_string) + ", type is " + str(type(color_string))
        if color_string == 'red':
            #color = [1,0,0,1]
            color = colormodel.RED
        if color_string == 'orange':
            color = colormodel.ORANGE
            #color = [1,0.6470588235,0,1]
        if color_string == 'yellow':
            color = colormodel.YELLOW
            #color = [1,1,0,1]
        if color_string == 'green':
            #color = [0,1,0,1]
            color = colormodel.GREEN
        if color_string == 'cyan':
            #color = [0,1,1,1]
            color = colormodel.BLUE
        # print 'color == ' + str(color) + ", type is " + str(type(color))
        # removed width = BRICK_WIDTH and height = BRICK_HEIGHT because they're not attributes of GObject
        # also removed linecolor=color just in case GObject's __init__ has to have the same number of arguments as the one it's nested inside
        GObject.__init__(self, x=xx, y=yy, width=BRICK_WIDTH, height=BRICK_HEIGHT, fillcolor=color, linecolor=color)

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE THE BRICKS

    # METHOD TO CHECK FOR COLLISION
    
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

class Ball(GEllipse):
    """Instance is a game ball.
    
    We extend GEllipse because a ball must have additional attributes for velocity.
    This class adds this attributes and manages them.
    
    INSTANCE ATTRIBUTES:
        _vx [int or float]: Velocity in x direction 
        _vy [int or float]: Velocity in y direction 
    
    The class Play will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with no
    setters for the velocities.
    
    How? The only time the ball can change velocities is if it hits an obstacle
    (paddle or brick) or if it hits a wall.  Why not just write methods for these
    instead of using setters?  This cuts down on the amount of code in Gameplay.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    def __init__(self, x, y, fillcolor):
        # initializer needs to override the one for GEllipse, with additional attributes _vx and _vy
        # suggested _vy start value of -.5
        # _vx should be generated randomly. Use random module
        self._vx = random.uniform(1.0, 5.0)
        self._vx = self._vx * random.choice([-1, 1])
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO SET RANDOM VELOCITY
    
    # METHODS TO MOVE AND/OR BOUNCE THE BALL
    # the following 5 methods take no arguments and return no value
    def move():
        pass

    def bounce_left():
        pass

    def bounce_right():
        pass

    def bounce_up():
        pass

    def bounce_down():
        pass

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE