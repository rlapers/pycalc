import sys

def calc(nb1, nb2, ope) :
    if ope == "+" :
        return nb1+nb2
    elif ope == "-" :
        return nb1-nb2
    elif ope == "*" :
        return nb1*nb2
    elif ope == "/" :
        return nb1/nb2
    return None

calc(float(sys.agrv[1]), float(sys.argv[3]), sys.argv[2])
