class Head:
    def __init__(self):
        pass
class Torso:
    def __init__(self,_head,_right_arm, _left_arm, _right_leg, _left_leg):
        self.head = _head
        self.left_arm = _left_arm
        self.right_arm = _right_arm
        self.left_leg = _left_leg
        self.right_leg = _right_leg
class Arm:
    def __init__(self, _hand):
        self.hand = _hand
class Hand:
    def __init__(self):
        pass
class Leg:
    def __init__(self,_feet):
        self.feet = _feet
class Feet:
    def __init__(self):
        pass
class Human:
    def __init__(self,_torso):
        self.torso = _torso

left_hand = Hand
left_arm = Arm(left_hand)
right_hand = Hand
right_arm = Arm(right_hand)
left_feet = Feet
left_leg = (left_feet)
right_feet = Feet
right_leg = (right_feet)
head = Head
torso = Torso(head,right_arm,left_arm,right_leg,left_leg)
human = Human(torso)