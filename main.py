#ABCABCABCDDDFFFFFF 1A1B1C1A1B1C1A1B1C3D6F FFFFDS 4F1D1S#s = str(input())
def F():
    s = str(input())
    d = 1
    k = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            d += 1
            i += 1
            ch = d
        else:
            k += str(d) + str(s[i])
            m = d
            d = 1
            i += 1
    m = k + str(ch) + str(s[-1])
    return m
print(F())
