import bricks
from constants import *

testBricks = bricks.Bricks()

testBricks.initialize_bricks()

gotten_bricks = testBricks.getBricks()
for brick in gotten_bricks:
    print 'Brick with x == ' + str(brick.x) + ', y == ' + str(brick.y) + ', and fillcolor == ' + str(brick.fillcolor)

is_first_brick = True
for brick in gotten_bricks:
    if is_first_brick:
        is_first_brick = False
        testBricks.remove_brick(brick)
        print testBricks
        print 'removed brick here'
print '\nBricks after removal:'
gotten_bricks = testBricks.getBricks()
for brick in gotten_bricks:
    print 'Brick with x == ' + str(brick.x) + ', y == ' + str(brick.y) + ', linecolor == ' + str(brick.linecolor) + ', and fillcolor == ' + str(brick.fillcolor)