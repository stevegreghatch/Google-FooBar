def solution(n):
    n = int(n)
    count = 0
    while n > 1:
        if n % 2 == 0:
            # get int result of dividing n by 2
            n = n // 2
        elif n == 3 or n % 4 == 1:
            # make number even by subtracting 1
            n = n - 1
        else:
            # make number even by adding 1
            n = n + 1
        count += 1
    # print(count)
    return count
