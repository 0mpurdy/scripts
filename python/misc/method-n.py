# Testing python with big numbers

def method(n):
    r = 1
    for i in range(n):
        if (i % 1000 == 0):
            print(i)
        r = r * 2
    return r

print(method(40000))

