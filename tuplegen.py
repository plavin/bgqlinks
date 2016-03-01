tups = open("tups.out","w+")

for i0 in range(0,2):
    for i1 in range(0,2):
        for i2 in range(0,2):
            for i3 in range(0,2):
                for i4 in range(0,2):
                    for i5 in range(0,2):
                        for i6 in range(0,2):
                            for i7 in range(0,2):
                                for i8 in range(0,2):
                                    for i9 in range(0,2):
                                        for i10 in range(0,2):
                                            for i11 in range(0,2):
                                                for i12 in range(0,2):
                                                    for i13 in range(0,2):
                                                        for i14 in range(0,2):
                                                            for i15 in range(0,2):
                                                                tup = (i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15)
                                                                if sum(x for x in tup) == 8:
                                                                    tups.write("%s\n" % (tup,))
