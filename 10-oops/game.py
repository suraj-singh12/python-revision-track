class Controller:
    def isLeftPressed(self):
        pass
    def isRightPressed(self):
        pass

class Player:
    def moveLeft(self):
        pass
    def moveRight(self):
        pass

controller1 = Controller()
player1 = Player()

if controller1.isLeftPressed():
    player1.moveLeft()
if controller1.isRightPressed():
    player1.moveRight()

# See how obvious and natural OOPS makes everything for us.
# if controller1.isLeftPressed() then player1.moveLeft()