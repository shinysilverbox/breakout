# play.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Subcontroller module for Breakout

This module contains the subcontroller to manage a single game in the Breakout App. 
Instances of Play represent a single game.  If you want to restart a new game, you are 
expected to make a new instance of Play.

The subcontroller Play manages the paddle, ball, and bricks.  These are model objects.  
Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer."""
import bricks
# future: import paddle
# future: import ball

from constants import *
from game2d import *
from models import *


# PRIMARY RULE: Play can only access attributes in models.py via getters/setters
# Play is NOT allowed to access anything in breakout.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)

class Play(object):
    """An instance controls a single game of breakout.
    
    This subcontroller has a reference to the ball, paddle, and bricks. It animates the 
    ball, removing any bricks as necessary.  When the game is won, it stops animating.  
    You should create a NEW instance of Play (in Breakout) if you want to make a new game.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See 
    subcontrollers.py from Lecture 25 for an example.
    
    INSTANCE ATTRIBUTES:
        _paddle [Paddle]: the paddle to play with 
        _bricks [list of Brick]: the list of bricks still remaining 
        _ball   [Ball, or None if waiting for a serve]:  the ball to animate
        _tries  [int >= 0]: the number of tries left 
    
    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Breakout. It is okay if you do, but you MAY NOT ACCESS 
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that 
    you need to access in Breakout.  Only add the getters and setters that you need for 
    Breakout.
    
    You may change any of the attributes above as you see fit. For example, you may want
    to add new objects on the screen (e.g power-ups).  If you make changes, please list
    the changes with the invariants.
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    def __init__(self):
        self._bricks = []

    def setMessage(self, message):
        self._mssg = message

    def getMessage(self):
        # this needs to return a message, not define what welcome_message is. Fix this.
        #welcome_message = GLabel(text='Press any key to play', font_size = 24, font_name = 'Colfax-Regular.otf', x = 240, y = 310)
        return self._mssg

    def has_game_been_won(self):
        # check if there are still bricks remaining to determine game over
        pass

    def is_out_of_lives(self):
        # check number of lives remaining to determine if game is over
        # if game is over, display success message, set state
        pass

    def determine_message_to_display(self):
        # depending on state, call method to display the appropriate message
        pass

    def create_bricks():
        bricks = self.construct_bricks()
        self.setBricks(bricks)

    

    def update_paddle(self, dt):
        # include min/max check to prevent paddle from going off the screen (with conditionals)
        
        # I'm not sure that this belongs here either. It calls this method.
        #x = 0
        #if self.input.is_key_down('left'):
        #    x += PADDLE_STEP
        #    self.update_paddle(x) # ???
        #if self.input.is_key_down('right'):
        #    x -= PADDLE_STEP
        #    self.update_paddle(x) # ???
        # if paddle moved left, and if the updated position would be <= PADDLE_WIDTH, then cut off input response
        # if paddle moved right, and if the updated position would be >= (GAME_WIDTH - (PADDLE_WIDTH/2)), then cut off input response
        # if y-value of the right side of the brick is >= GAME_WIDTH, cut off input response
        pass

    def serve(self):
        pass

    def move_paddle(self):
        pass

    def move_ball(self):
        pass

    def create_ball(self):
        pass

    def serve_ball(self):
        pass

    def bounce_ball(self):
        pass

    def collision_check(self):
        pass

    def draw(self, view):
        # draw the welcome message when state is STATE_INACTIVE
        #if self.getState() == STATE_INACTIVE:
        #    self.state_inactive()
        #    self._mssg.draw(self.view)
        # draw the bricks
        #if self.getState() == STATE_NEWGAME:
        #    self._state_newgame()
        #    bricks = self.getBricks()
        #    for brick in bricks:
        #        brick.draw(self.view)
        # draw paddle
        pass
        
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER (standard form) TO CREATE PADDLES AND BRICKS
    
    # UPDATE METHODS TO MOVE PADDLE, SERVE AND MOVE THE BALL
    
    # DRAW METHOD TO DRAW THE PADDLES, BALL, AND BRICKS
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
