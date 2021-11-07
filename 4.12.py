def SUM(n):

    # 0! = 1, 1! = 1
    if n==1:
        return 1
    # n! = n * (n-1)!
    if n > 1:
        return n+SUM(n-1)
