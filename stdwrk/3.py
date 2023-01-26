x = str(input())
mySet = set(x)
for bukva in mySet:
    kolichestvo = 0
    for character in x:
        if character == bukva:
            kolichestvo += 1
    print(" {} -> {}".format(bukva, kolichestvo))