import math

def saisir_equation():
    print("Equation sous la forme de ax^2+bx+c")
    a = int(input("Saisir a : "))
    b = int(input("Saisir b : "))
    c = int(input("Saisir c : "))
    return a,b,c

def solution_equation(a, b, c):
    if a!=0:
        delta = ((b^2)-(4*a*c))
        if (delta<0):
            #print("Pas de solution");
            return ()
        elif (delta==0):
            x=(-1*(b))/(2*a)
            #print("x= ", x)
            return (x)
        else:
            x = ((-1 * b) - (math.sqrt(delta))) / (2 * a)
            y = ((-1 * b) + (math.sqrt(delta))) / (2 * a)
            #print("x = ", x, "y = ",y)
            return (x,y)
    else:
        if (b!=0 and c==0):
            x = (-1 * c)/b
            #print("x= ",x)
            return (x)
        if (b==0 and c!=0):
            #print("Pas de solution");
            return ()
        if(b==0 and c==0):
            return ('infini')

def afficher_solution(tuple):
    if len(tuple)==0:
        print("Pas de solution")
    elif len(tuple)==1:
        print("Solution : ",tuple[0])
    elif len(tuple)==2:
        print("x = ", tuple[0], "y = ", tuple[1])
    else:
        print("Solution infini")

a,b,c=saisir_equation()
t=solution_equation(a,b,c)
afficher_solution(t)
