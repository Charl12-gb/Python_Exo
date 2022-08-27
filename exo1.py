def min_max():
    min =0
    max = 0
    for i in range(10):
        val = int(input("Entrez une valeur : "));
        if i==0:
            min =val
            max=val
        else:
            if val < min :
                min = val
            if val > max:
                max = val
    return min, max

def affiche():
    a,b = min_max()
    print("Min = ", a)
    print("Max = ", b)

affiche()