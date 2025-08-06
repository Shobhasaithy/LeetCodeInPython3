class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0 
        i = 5
        while n // i >= 1:
            count += n // i
            i *= 5
        return count

'''
Maths 
Trailing zeroes in n! are created by multiplying pairs of 2 and 5.
Since there are always more 2s than 5s in n!, 
we just count the number of times 5 is a factor in the numbers from 1 to n.
This includes 5, 25, 125, etc.
'''
