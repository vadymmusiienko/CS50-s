# returns fibonachi number n
def fibonachi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


# prints fibonachi number
print(fibonachi(19))