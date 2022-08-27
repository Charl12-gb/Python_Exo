from random import randint

val = randint(0,20);
x=1;
trouver = False;
while (x<=6):
    val2 = int(input("Saisir la valeur : "));
    if val == val2:
        trouver=True;
        print("Felicitation");
        print("Vous avez gagne apres ", x, "essai");
        break
    else:
        if val < val2 :
            print("Valeur plus petit");
        else:
            if x<6:
                print("Valeur plus grande");
        x=x+1;
if ((val!=val2) and (x==6)):
    print("Vous n'avez pas trouve");
