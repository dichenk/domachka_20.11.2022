def solve(n, repeats):
    a = 0
    b = 1
    repeats = int(repeats)
    while repeats > 0:
        a += int(repeats) * int(n) * b
        b *= 10
        repeats -= 1

    return a

n = input('please input a nubmer: ')
repeats = input('please input amount of repeats: ')
print()
print('result: ', solve(n, repeats))

