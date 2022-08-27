def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    rendu = (20*x20) + (10*x10) + (5*x5) + (2*x2) + (1*x1);

    if prix > rendu :
        return None,None,None,None,None;
    else:
        monnaie = rendu - prix;
        x20 = monnaie//20;
        reste1 = monnaie%20;
        x10 = reste1//10;
        reste2 = reste1 % 10;
        x5 = reste2 // 5;
        reste3 = reste2 % 5;
        x2 = reste3 // 2;
        reste4 = reste3 % 2;
        x1 = reste4 // 1;
        return x20,x10,x5,x2,x1;

result = rendre_monnaie(10, 1, 1, 1, 1, 1);
print(result);