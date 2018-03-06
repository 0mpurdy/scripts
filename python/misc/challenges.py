# Some example exercises made for the python teacher
# course. Showcases loops and some basic mathematical
# operators.

size = 7

print(size, "layers from left")
for i in range(1, size + 1):
    print("*" * i)

print(size, "layers from right")
for i in range(1, size + 1):
    print(" " * (size - i), "*" * i)

print("Pyramid with", size, "layers")
for i in range(size + 1):
    print(" " * (size - i), "*" * ((i * 2) + 1))

print("Pyramid with maximum layer of", size, "*s")
for i in range((size + 1) // 2):
    print(" " * ((size // 2) - i), "*" * ((i * 2) + 1))
    
print("Alternative to above")
smallSize = size // 2
for i in range(smallSize + 1):
    print(" " * (smallSize - i), "*" * ((i * 2) + 1))
