i = 0.0

while i < 2.1:
    j = 1.0
    while j < 3.1:
        if (i > 0 and i < 1) or (i > 1 and i < 2):
            print("I={:.1f} J={:.1f}".format(i, i + j))
        else:
            a = int(i)
            b = int(i + j)
            print("I={} J={}".format(a, b))

        j += 1
    
    i = round(i + 0.2, 1)
