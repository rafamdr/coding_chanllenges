# Change Endianness
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def change_endian_ref(self, num: int):
        result = 0
        result |= (num << 24) & 0xFF000000
        result |= (num <<  8) & 0x00FF0000
        result |= (num >>  8) & 0x0000FF00
        result |= (num >> 24) & 0x000000FF
        return result

    def change_endian_fast(self, num: int):
        num = (num >> 16) | (num << 16)
        num = ((num & 0xff00ff00) >> 8) | ((num & 0x00ff00ff) << 8)
        return num
# ----------------------------------------------------------------------------------------------------------------------


examples = [
   0x12345678, 0x78563412
]

sol = Solution()

for ex in examples:
    print('Ref.: %s  ->  %s' % (hex(ex), hex(sol.change_endian_ref(ex))))
    print('Fast: %s  ->  %s' % (hex(ex), hex(sol.change_endian_fast(ex))))
    print()
# ----------------------------------------------------------------------------------------------------------------------
