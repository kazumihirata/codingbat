# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
def make_bricks(small, big, goal):
    if big :
        for i in range(1, big+1) :
            amari = goal - (5 * i)
            if amari == 0 :
                return True
            if amari <= small and 0 < amari :
                return True
        return False
    else :
        if goal <= small :
            return True
        else :
            return False