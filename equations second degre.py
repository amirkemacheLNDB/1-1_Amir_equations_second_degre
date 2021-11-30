from math import sqrt

def equations_second_degre ():
    a=float(input("Entrer une valeur de a:"))
    b=float(input("Entrer une valeur de b:"))
    c=float(input("Entrer une valeur de c:"))
    solution_1=0
    solutions_2=0
    delta=0
    liste=[]
    texte="Il n y a pas de solution"
    if a==0:
        return a
    else:
        delta = 0 + b*b-4*a*c
        if delta>0:
            solution_1 = 0 - b + sqrt(delta)/4*a
            solution_2 = 0 - b - sqrt(delta)/4*a
            liste.append(solution_1)
            liste.append(solution_2)
            return liste
        elif delta==0:
                solution_1 = -b/4*a
                return solution_1
        elif delta<0:
            return texte
    

reponse = equations_second_degre ()
print (reponse)
liste=[]
            
