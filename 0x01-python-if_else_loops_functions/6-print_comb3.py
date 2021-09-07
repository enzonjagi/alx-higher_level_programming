#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        a = str(i)
        b = str(j)
        comb = str("{}{}".format(i, j))
        if (i == j):
            continue
        # add a check for a repeat combination
        elif (j < i):
            continue
        else:
            if (comb == "89"):
                print("{}".format(comb))
            else:
                print("{}".format(comb), end=", ")
