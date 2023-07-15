"""
File: largest_digit.py
Name:廖悠行
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))      # 5
    print(find_largest_digit(281))        # 8
    print(find_largest_digit(6))          # 6
    print(find_largest_digit(-111))       # 1
    print(find_largest_digit(-9453))      # 9


def find_largest_digit(n, curr_max=0):
    n = abs(n)
    last_digit = n % 10
    if n // 10 == 0:
        if last_digit > curr_max:
            return last_digit
        else:
            return curr_max
    else:
        x = find_largest_digit(n // 10, curr_max)
        if last_digit > x:
            return last_digit
        else:
            return x



if __name__ == '__main__':
    main()
