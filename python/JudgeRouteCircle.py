"""
* Algorithms: Judge Route Circle
*
* Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
* judge if this robot makes a circle, which means it moves back to the original
* place. The move sequence is represented by a string. And each move is
* represent by a character. The valid robot moves are R (Right), L (Left),
* U (Up) and D (down). The output should be true or false representing whether
* the robot makes a circle.
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        UD = 0
        RL = 0

        for idx in range(0, len(moves)):
            if(moves[idx] == "U"):
                UD += 1
            elif (moves[idx] == "D"):
                UD -= 1
            elif (moves[idx] == "R"):
                RL += 1
            elif (moves[idx] == "L"):
                RL -= 1

        if (UD == 0 and RL == 0):
            return(True)
        else:
            return(False)
