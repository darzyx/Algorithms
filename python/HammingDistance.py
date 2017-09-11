"""
* Algorithms: Hamming Distance
*
* The Hamming distance between two integers is the number of positions at which
* the corresponding bits are different. Given two integers x and y, calculate
* the Hamming distance. Note: 0 ≤ x, y < 231.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        count = 0

        # Returns 0 if bits different, 1 if bits same
        exclusiveOrBinStr = str(bin(x ^ y))

        # Counts up the 1s
        for idx in range(2, len(exclusiveOrBinStr)):
          if (int(exclusiveOrBinStr[idx]) == 1):
            count += 1

        return(count)
