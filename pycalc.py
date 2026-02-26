import sys

def calc(nb1, nb2, ope) :
    if ope == "+" :
        return nb1+nb2
    elif ope == "-" :
        return nb1-nb2
    elif ope == "*" :
        cmp = 0
        res = 0
        while cmp < int(nb2) :
            res += nb1
            cmp += 1
        return res
    elif ope == "/" :
        return nb1/nb2
    return None

print(calc(float(sys.argv[1]), float(sys.argv[3]), sys.argv[2]))
        
