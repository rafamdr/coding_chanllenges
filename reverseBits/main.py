# Reverse bits of a given 32 bits unsigned integer.
#
# Example 1:
#
# Input: 00000010100101000001111010011100 Output: 00111001011110000010100101000000 Explanation: The input binary
# string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its
# binary representation is 00111001011110000010100101000000. Example 2:
#
# Input: 11111111111111111111111111111101 Output: 10111111111111111111111111111111 Explanation: The input binary
# string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its
# binary representation is 10111111111111111111111111111111.
#
#
# Note:
#
# Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output
# will be given as signed integer type and should not affect your implementation, as the internal binary
# representation of the integer is the same whether it is signed or unsigned. In Java, the compiler represents the
# signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed
# integer -3 and the output represents the signed integer -1073741825.
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def reverse_bits_ref(self, num: int):
        result = 0
        for i in range(0, 32):
            if ((num >> i) & 1) == 1:
                result |= (1 << (32 - 1 - i))
        return result

    def reverse_bits_fast(self, num: int):
        num = (num >> 16) | (num << 16)
        num = ((num & 0xff00ff00) >> 8) | ((num & 0x00ff00ff) << 8)
        num = ((num & 0xf0f0f0f0) >> 4) | ((num & 0x0f0f0f0f) << 4)
        num = ((num & 0xcccccccc) >> 2) | ((num & 0x33333333) << 2)
        num = ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)
        return num
# ----------------------------------------------------------------------------------------------------------------------


examples = [
   11, 0b11111111111111111111111111111101
]

sol = Solution()

for ex in examples:
    print('Ref.: %s  ->  %s' % (bin(ex), bin(sol.reverse_bits_ref(ex))))
    print('Fast: %s  ->  %s' % (bin(ex), bin(sol.reverse_bits_fast(ex))))
    print()
# ----------------------------------------------------------------------------------------------------------------------
