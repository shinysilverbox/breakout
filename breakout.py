# breakout.py
# Tim Kautsky, tbk29
# DATE COMPLETED HERE
"""Primary module for Breakout application

This module contains the main controller class for the Breakout application. There is no
need for any any need for additional classes in this module.  If you need more classes, 
99% of the time they belong in either the play module or the models module. If you 
are ensure about where a new class should go, 
post a question on Piazza."""

from constants import *
from game2d import *
from play import Play


# PRIMARY RULE: Breakout can only access attributes in play.py via getters/setters
# Breakout is NOT allowed to access anything in models.py

class Breakout(GameApp):
    """Instance is the primary controller for the Breakout App
    
    This class extends GameApp and implements the various methods necessary for processing 
    the player inputs and starting/running a game.
    
        Method start begins the application.
        
        Method update either changes the state or updates the Play object
        
        Method draw displays the Play object and any other elements on screen
    
    Because of some of the weird ways that Kivy works, you SHOULD NOT create an
    initializer __init__ for this class.  Any initialization should be done in
    the start method instead.  This is only for this class.  All other classes
    behave normally.
    
    Most of the work handling the game is actually provided in the class Play.
    Play should have a minimum of two methods: updatePaddle(input) which moves
    the paddle, and updateBall() which moves the ball and processes all of the
    game physics. This class should simply call that method in update().
    
    The primary purpose of this class is managing the game state: when is the 
    game started, paused, completed, etc. It keeps track of that in an attribute
    called _state.
    
    INSTANCE ATTRIBUTES:
        view    [Immutable instance of GView; it is inherited from GameApp]:
                the game view, used in drawing (see examples from class)
        input   [Immutable instance of GInput; it is inherited from GameApp]:
                the user input, used to control the paddle and change state
        _state  [one of STATE_INACTIVE, STATE_COUNTDOWN, STATE_PAUSED, STATE_ACTIVE]:
                the current state of the game represented a value from constants.py
        _game   [Play, or None if there is no game currently active]: 
                the controller for a single game, which manages the paddle, ball, and bricks
        _mssg   [GLabel, or None if there is no message to display]
                the currently active message
    
    STATE SPECIFIC INVARIANTS: 
        Attribute _game is only None if _state is STATE_INACTIVE.
        Attribute _mssg is only None if  _state is STATE_ACTIVE or STATE_COUNTDOWN.
    
    For a complete description of how the states work, see the specification for the
    method update().
    
    You may have more attributes if you wish (you might need an attribute to store
    any text messages you display on the screen). If you add new attributes, they
    need to be documented here.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
#!!!! Create attribute called missed for if the ball goes off the bottom edge of the
    # screen. When true, go to STATE_PAUSED, wait for an input before starting again.
    # Once the input is received, enter STATE_COUNTDOWN. Maximum of 3 balls before
    # game over.
    
    # DO NOT MAKE A NEW INITIALIZER!
    
    # THREE MAIN GAMEAPP METHODS
    def start(self):
        """Initializes the application.
        
        This method is distinct from the built-in initializer __init__ (which you 
        should not override or change). This method is called once the game is running. 
        You should use it to initialize any game-specific attributes.
        
        This method should make sure that all of the attributes satisfy the given 
        invariants. When done, it sets the _state to STATE_INACTIVE and creates a message 
        (in attribute _mssg) saying that the user should press a key to play a game."""
        # print 'running start method'
        self._game = None
        self._state = STATE_INACTIVE
        self.previous_number_of_keys_pressed = 0
        self.time = 0

        #if self._state == STATE_INACTIVE:
        self._mssg = GLabel(text='Press any key to play', font_size = 24, font_name = 'Colfax-Regular.otf', x = 240, y = 310)
        # print 'assigned %s' % self._mssg
        #else:
        #    self._mssg = None
        #    print 'wiped out welcome_message'
    
    def update(self, dt):
        """Animates a single frame in the game.
        
        It is the method that does most of the work. It is NOT in charge of playing the
        game.  That is the purpose of the class Play.  The primary purpose of this
        method is to determine the current state, and -- if the game is active -- pass
        the input to the Play object _game to play the game.
        
        As part of the assignment, you are allowed to add your own states.  However, at
        a minimum you must support the following states: STATE_INACTIVE, STATE_NEWGAME,
        STATE_COUNTDOWN, STATE_PAUSED, and STATE_ACTIVE.  Each one of these does its own
        thing, and so should have its own helper.  We describe these below.
        
        STATE_INACTIVE: This is the state when the application first opens.  It is a 
        paused state, waiting for the player to start the game.  It displays a simple
        message on the screen.
        
        STATE_NEWGAME: This is the state creates a new game and shows it on the screen.  
        This state only lasts one animation frame before switching to STATE_COUNTDOWN.
        
        STATE_COUNTDOWN: This is a 3 second countdown that lasts until the ball is 
        served.  The player can move the paddle during the countdown, but there is no
        ball on the screen.  Paddle movement is handled by the Play object.  Hence the
        Play class should have a method called updatePaddle()
        
        STATE_ACTIVE: This is a session of normal gameplay.  The player can move the
        paddle and the ball moves on its own about the board.  Both of these
        should be handled by methods inside of class Play (NOT in this class).  Hence
        the Play class should have methods named updatePaddle() and updateBall().
        
        STATE_PAUSED: Like STATE_INACTIVE, this is a paused state. However, the game is
        still visible on the screen.
        
        The rules for determining the current state are as follows.
        
        STATE_INACTIVE: This is the state at the beginning, and is the state so long
        as the player never presses a key.  In addition, the application switches to 
        this state if the previous state was STATE_ACTIVE and the game is over 
        (e.g. all balls are lost or no more bricks are on the screen).
        
        STATE_NEWGAME: The application switches to this state if the state was 
        STATE_INACTIVE in the previous frame, and the player pressed a key.
        
        STATE_COUNTDOWN: The application switches to this state if the state was
        STATE_NEWGAME in the previous frame (so that state only lasts one frame).
        
        STATE_ACTIVE: The application switches to this state after it has spent 3
        seconds in the state STATE_COUNTDOWN.
        
        STATE_PAUSED: The application switches to this state if the state was 
        STATE_ACTIVE in the previous frame, the ball was lost, and there are still
        some tries remaining.
        
        You are allowed to add more states if you wish. Should you do so, you should 
        describe them here.
        
        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """


        """
        Gameply logic happens here

        STATE_INACTIVE  = 0
        #: state when we are initializing a new game
        STATE_NEWGAME   = 1
        #: state when we are counting down to the ball serve
        STATE_COUNTDOWN = 2
        #: state when we are waiting for user to click the mouse
        STATE_PAUSED    = 3
        #: state when the ball is in play and being animated
        STATE_ACTIVE    = 4
        #: state when either the player has lost all lives, or all bricks are eliminated
        STATE_COMPLETE  = 5

        """
        self.determine_state()
        #if self._state == STATE_INACTIVE:
            #print 'state is STATE_INACTIVE, calling self.start()'
            #self.start()

        if self._state == STATE_NEWGAME:
            '''
            create a play instance
            '''
            # print 'state is STATE_NEWGAME, calling self.newgame()'
            self.newgame()
            self.setState(STATE_COUNTDOWN)
        elif self._state == STATE_COUNTDOWN:
            self.countdown()
        elif self._state == STATE_ACTIVE:
            self.active()
        elif self._state == STATE_PAUSED:
            self.paused()
        elif self._state == STATE_COMPLETE:
            self.complete()
    
    def draw(self):
        """Draws the game objects to the view.
        
        Every single thing you want to draw in this game is a GObject.  To draw a GObject 
        g, simply use the method g.draw(self.view).  It is that easy!
        
        Many of the GObjects (such as the paddle, ball, and bricks) are attributes in Play. 
        In order to draw them, you either need to add getters for these attributes or you 
        need to add a draw method to class Play.  We suggest the latter.  See the example 
        subcontroller.py from class."""
        # IMPLEMENT ME
        if self.getMessage() != None:
            self._mssg.draw(self.view) # This should create a welcome message.
        # When assigning None to a welcome_message, a 'simple change' is needed here to
        # manage this method.
        if self.getState() == STATE_NEWGAME:
            self._game.draw_play(self.view)
    
    def getState(self):
        return self._state

    def setState(self, state):
        self._state = state
    
    def setMessage(self, message):
        self._mssg = message

    def getMessage(self):
        return self._mssg

    def determine_state(self):
        """Processes key presses and regulates game state changes accordingly. Handlers for each game state to follow."""
        
        # TODO: think about the state model. Progressing through states is not always linear

        number_of_keys_pressed = self.input.key_count
        # if number_of_keys_pressed > 0:
        #     print 'number_of_keys_pressed == ' + str(number_of_keys_pressed)
        # True if at least 1 key was pressed in this frame, and no keys were pressed in the last frame
        keys_have_been_pressed = number_of_keys_pressed > 0 and self.previous_number_of_keys_pressed == 0
        # situation 1: program launch + key press. Starts at STATE_INACTIVE. If key pressed, go to STATE_NEWGAME.
        if keys_have_been_pressed:
            # print 'key input received; moving to next state'
            # use a setter here
            # TODO: BUG; account for nonlinear state progression
            self._state = (self._state + 1 % NUMBER_OF_STATES)
            # print 'new state is ' + str(self._state)
        self.previous_number_of_keys_pressed = number_of_keys_pressed

    def newgame(self):
        '''
        clear screen
        create new play instance
        initialize play instance -> create bricks, draw self

        :return: None
        '''
        # print 'setting message to None'
        self.setMessage(None)
        # print 'self._mssg == ' + str(self.getMessage())
        # print 'executing newgame method'
        self._game = Play()
        # print 'new Play object created & saved in self._game'
        self._game.create_bricks()
        self._game.draw_play(self.view)
