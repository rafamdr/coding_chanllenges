# Given a positive integer n, write a function that finds the number of zeros at the end of n! in base 10.
#
# Example:
#
# $ zerosEndingFactorial(1)
# $ 0
#
# $ zerosEndingFactorial(5)
# $ 1
#
# $ zerosEndingFactorial(100)
# $ 24


# Input	|	Expected	|	Result
# 1		    0		        0.20
# 5		    1		        1.20
# 10		2		        2.45
# 15		3		        3.70
# 100		24		        24.95
# 200		49		        49.95
# 400		99		        99.95
# 453		111		        113.20
# 1000		249		        249.95
# 1235		306		        308.70

# ----------------------------------------------------------------------------------------------------------------------
import math


def zeros_ending_factorial_ref(num: int) -> int:
    res = 1
    count_zeros = 0
    while num > 0:
        res *= num
        num -= 1
    while res > 0 and res % 10 == 0:
        count_zeros += 1
        res //= 10
    return count_zeros
# ----------------------------------------------------------------------------------------------------------------------


def zeros_ending_factorial_opt1(num: int) -> int:
    count2 = count5 = 0
    while num > 0:
        num_temp = num
        while num_temp % 2 == 0:
            num_temp = num_temp // 2
            count2 = count2 + 1
        while num_temp % 5 == 0:
            num_temp = num_temp // 5
            count5 = count5 + 1
        num -= 1
    return count2 if count2 < count5 else count5
# ----------------------------------------------------------------------------------------------------------------------


def zeros_ending_factorial_opt2(num: int) -> int:
    s = 0
    while num > 0:
        # num = math.floor(num / 5)
        num = num // 5
        s += num
    return s
# ----------------------------------------------------------------------------------------------------------------------


def zeros_ending_factorial_opt3(num: int) -> float:
    # Considering geometric progression
    # Formula to get n-term:
    # EQ1:   An = A1 * r ˆ(n - 1)
    # considering A1 = 100, An (last element) = 1 and r = 1/5
    # EQ1:   1 = 100 * 1/5 ˆ(n - 1)
    # EQ1:   1 / 100 = 1/5 ˆ(n - 1)
    # EQ1:   1 / 100 = (1/5 ˆ n) / (1/5)
    # EQ1:   1 / (100 * 5) = 1/5ˆn
    # switching sides
    # 1/5ˆn = 1 / (100 * 5)
    # Formula to get sum where "i" is between "m" and "n"
    # EQ2:   sum(A*rˆk) = A * (rˆm - rˆ(n+1)) / (1 - r)
    # Considering m = 1 and A = 100
    # EQ2:   sum(A*rˆk) = 100 * (1/5ˆ1 - 1/5ˆ(n+1)) / (1 - 1/5)
    # EQ2:   sum(A*rˆk) = 100 * (1/5 - 1/5ˆ(n+1)) / (1 - 1/5)
    # EQ2:   sum(A*rˆk) = 100 * (1/5 - 1/5ˆn * 1/5ˆ1) / (1 - 1/5)
    # Applying EQ1 on EQ2
    # EQ2:   sum(A*rˆk) = 100 * (1/5 - 1 / (100 * 5) * 1/5ˆ1) / (1 - 1/5)
    # EQ2:   sum(A*rˆk) = 100 * (1/5 - 1 / (100 * 5) * 1/5) / (1 - 1/5)

    # sum = num * (1/5 - (1 / (num * 5) * 1/5)) / (1 - 1/5)

    # sum = num * (1/5 - (1 / (num * 25))) / (4 / 5)

    # sum = num * (1 / 5 - (1 / (num * 25))) * (5 / 4)

    # sum = num * (1 - (1 / (num * 5))) / 4

    # sum = num/4 - (num / (num * 5)) / 4

    # sum = num/4 - (1 / 5) / 4

    # sum = (num - 1/5) / 4

    sum = (num * 100 - 20) // 400

    return sum
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    # 1: 0,
    5: 1,
    # 10: 2,
    # 15: 3,
    # 100: 24,
    # 200: 49,
    # 400: 99,
    # 453: 111,
    # 1000: 249,
    # 1235: 306,
    # 4097: 1021,
    # 8193: 2045,
    10000: 2499,
    # 35437: 8856,
}

print('Expected\t|\tExpected\t|\tResult')
for ex in examples:
    # print('Ref..: %d = %d -> %s' % (ex, examples[ex], zeros_ending_factorial_ref(ex)))
    # print('Opt1.: %d = %d -> %s' % (ex, examples[ex], zeros_ending_factorial_opt1(ex)))
    print('Opt2.: %d = %d -> %s' % (ex, examples[ex], zeros_ending_factorial_opt2(ex)))
    print('%d\t\t%d\t\t%.2f' % (ex, examples[ex], zeros_ending_factorial_opt3(ex)))
# ----------------------------------------------------------------------------------------------------------------------
