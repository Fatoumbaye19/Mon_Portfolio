"""def somme(n1, n2, n3, n4, n5):
    somme = n1 + n2 + n3 + n4 + n5
    print(f"la somme est {somme}")
    return somme 
def moyenne(n1, n2, n3, n4, n5):
    moy = (somme(n1, n2, n3, n4, n5)/5)
    print(f"la moyenne est {moy}")
    return moy 
def ecart(n1, n2, n3, n4, n5):
    ecart = ((n1 - (somme(n1, n2, n3, n4, n5)/5) ) ** 2 + (n2 - (somme(n1, n2, n3, n4, n5)/5)) ** 2 + (n3 - (somme(n1, n2, n3, n4, n5)/5)) ** 2 + (n4 - (somme(n1, n2, n3, n4, n5)/5)) ** 2 + (n5 - (somme(n1, n2, n3, n4, n5)/5)) ** 2)
    print(f"l'écart type est {ecart}")
    return ecart
def var(n1, n2, n3, n4, n5):
    from math import sqrt
    var = sqrt(var)
    print(f"la variance est {var}")
    return var 
n1 = int(input("saisir la 1ere note: "))
n2 = int(input("saisir la 2eme note: "))
n3 = int(input("saisir la 3eme note: "))
n4 = int(input("saisir la 4eme note: "))
n5 = int(input("saisir la 5eme note: "))

somme(n1, n2, n3, n4, n5)
moyenne(n1, n2, n3, n4, n5)
ecart(n1, n2, n3, n4, n5)
var(n1, n2, n3, n4, n5)
"""
"""texte = "Python est un merveilleux langage de programmation"
mot = texte.split()
print(mot)
index = 0
mot = mot[0]
print(mot)
texte.split()
print(texte[0])
"""

#nombre parfait
"""n = int(input("saisir un nombre: "))
s = 0
for cpt in range(1, n):
    if n % cpt == 0:
        s += cpt
        print(s)
if s == n:
    print(f"{n} est un nombre parfait.")
else:
    print(f"{n} n'est pas un nombre parfait.")
"""   
# exercice sur les chaines de caractères et les listes
"""chaine = "Python.org"
for cpt in chaine:
    occurence = chaine.count(cpt)
    print(f"le caractère {cpt} apparait {occurence} fois")
"""
#exercice sur les bloques d'une chaine de caractères 
"""chaine = "programme est un peu difficile"
chaine = chaine.split()
index = 4
print(chaine[4])
"""
#exercice sur la position d'un caractère dans la chaine 
"""chaine = "langage"
n = len(chaine)
for cpt in range(0, n + 1):
    if (chaine[cpt] == "a"):
        print("la lettre a est présent dans la chaine à la position", cpt)
"""
"""chaine = "anticonstitutionnellement"
i = 0
for cpt in chaine:
    if cpt == "e" or cpt == "a" or cpt == "i" or cpt == "o" or cpt == "u":
        i += 1
print(f"cette chaine contient {i} voyelles") 
"""
"""def afficheCube(r):
    puissance = (r ** 3)
    print(puissance)
r = int(input("saisir le nombre a :"))
def surface(r):
    aire = (4 * 3.14 / 3) * (r ** 3)
    print(aire)
afficheCube(r)
surface(r)
"""
"""liste = [0] * 10
print(liste)
"""

"""n1 = int(input("saisir un nombre: "))
liste = [n1]
i = 0
while i != 9:
    n1 = int(input("saisir un nombre: "))
    liste = liste + [n1]
    i += 1
print(liste)
somme = 0
produit = 1
for cpt in liste:
    somme += cpt
    produit *= cpt
print(f"la somme des éléments de la liste est de {somme}")
print(f"le produit des éléments de la liste est {produit}")
moy = somme / len(liste)
print(f"la moyenne de la liste est de {moy}")
"""
"""n1 = int(input("saisir un element de la liste: "))
liste1 = [n1]
i = 0
while i != 2:
    n1 = int(input("saisir un element de la liste: "))
    liste1 = liste1 + [n1]
    i += 1
print(f"la première liste est {liste1}")
n2 = int(input("saisir un element de la liste: "))
liste2 = [n2]
i = 0
while i != 2:
    n2 = int(input("saisir un element de la liste: "))
    liste2 = liste2 + [n2]
    i += 1
print(f"la seconde liste est {liste2}")
#première méthode:
scalaire = (liste1[0] * liste2[0]) + (liste1[1] * liste2[1]) + (liste1[2] * liste2[2])
print(f"le produit scalaire est {scalaire}")
"""
"""n = int(input("saisir un élémént de la liste: "))
liste = [n]
i = 0
while i != 9:
    n = int(input("saisir un élémént de la liste: "))
    liste = liste + [n]
    i += 1
print(liste)
for cpt in liste:
    occurence = liste.count(cpt)
    if occurence < 2:
        print("les éléménts uniques de cette liste sont", cpt, end=" ")
"""
"""n = int(input("saisir un élémént de la liste: "))
liste = [n]
i = 0
while i != 9:
    n = int(input("saisir un élémént de la liste: "))
    liste = liste + [n]
    i += 1
max = liste [0]
for cpt in liste:
    if cpt >= max:
        max = cpt

print("le maximum de cette liste est ", max(liste))
print("le minimum de cette liste est ", min(liste))
"""
"""grandeListe = []
nom1 = input("saisir un nom: ")
liste1 = [nom1]
note = int(input("saisir une note: "))
liste1 = liste1 + [note]
j = 0
while note != 4:
    note = int(input("saisir une note: "))
    liste1 = liste1 + [note]
    j += 1
somme = 0
for cpt in liste1[1:5]:
    somme += cpt
moy = (somme / len(liste1))
liste1 = liste1 + [moy]
print(liste1)
grandeListe = [liste1]
i = 0
while i != 9:
    nom2 = input("saisir un nom: ")
    liste2 = [nom2]
    note = int(input("saisir une note: "))
    liste2 = liste2 + [note]
    j = 0
    while note != 4:
        note = int(input("saisir une note: "))
        liste2 = liste2 + [note]
        j += 1
        somme = 0
        for cpt in liste2[1:5]:
             somme += cpt
    moy = (somme / len(liste2))
    liste2 = liste2 + [moy]
    print(liste2)
    grandeListe = [liste1] + [liste2]
    i += 1
    print(grandeListe)
"""
"""def saisirIp():
    ip = input("saisir une adresse ip au format pontillé: ")
    return ip 
def decoupIp(adrIp):
    ip = ip.split(".")
    for cpt in range(len(ip)):
        ip[cpt] = int(ip[cpt])
        return ip 
def classeIp(ip):
    ipList = decoupIp(ip)
    octet1 = ipList[0]
    if octet1 <= 127:
        return "A"
    elif octet1 <= 191:
        return "B"
    elif octet1 <= 223:
        return "C"
    elif octet1 <= 239:
        return "D"
    else:
        return "E"
def masqueStandard(ip):
    classip = classeIp()
"""
def  vitesseMoyenne(d, t):
    """Fonction qui donne la vitesse moyenne en fonction de deux paramètres que sont:
    d: la distance en mètres
    t: le temps mis
    """
    d = d / 1000
    t = t / 3600
    vitMoy = (d / t)
    print("la vitesse moyenne est", round(vitMoy, 2))
    return vitMoy
"""
d = int(input("saisir la distance d: "))
t = float(input("saisir le temps mis: "))
vitesseMoyenne(d, t)
"""
"""f = lambda x: 2 * x ** 2 - 3 * x + 2
for cpt in range(-10, 21):
    x = cpt / 10
    res = round(f(x), 2)
    print(f"f({x}) = {res}")
"""
"""def afficheDiviseurs(n):
    for cpt in range(1, n + 1):
        if n % cpt == 0:
            print(cpt, end=" ")
    
n = int(input("saisir un nombre: "))
afficheDiviseurs(n)
"""
"""prixHt = float(input("prix HT (en £): "))
tauxTva = int(input("TVA(en %): "))
prixHTT = prixHt * (1 + tauxTva / 100)
print(f"prix TTC = ", round(prixHTT, 2))
"""
"""prenom = input("quelle est votre prénom: ")
anneeNaiss = int(input("votre date de naissance: "))
age = 2023 - anneeNaiss
print(f"pour ton anniversaire {prenom}")
print("  {} " * age) 
print(" _||_" * age)
print("|" + (" " * 4)  * age + "|")
"""

"""n = int(input("saisir un nombre: "))
for cpt in range(1, n):
    if n % cpt == 0:
        div = cpt
    print(div)
print(div)
"""
#n = int(input("saisir un nombre: "))
"""fact = 1
for cpt in range(1, n + 1):
    fact *= cpt
print(fact)
"""
"""fact = 1
cpt = 1
while n != 0:
    fact *= cpt
    cpt += 1
    n = n - 1
print(fact) 
"""
#n = int(input("saisir la table: "))
"""for cptTable in range(10):
    print(f"la table de {cptTable}")
    for cptOp in range(10):
        print(f"{cptTable} * {cptOp} = {cptTable * cptOp:>2d}", end=" ")
    print()
"""
"""cadreHaut = "\u2554" + "\u2550\u2566" * 5 + "\u2550\u2557"
print(cadreHaut)
ligneInt = "\u2560" + "\u2550\u256C" * 5 + "\u2550\u2563"
#print(ligneInt)
cadreBas = "\u255A" + "\u2550\u2569" * 5 + "\u2550\u255D"
#print(cadreBas)
for cptLigne in range(5):
    #print(ligneInt)
    for cptCol in range(6):
        uneLettre = chr(65 + cptCol + cptLigne * 6)
        if ord(uneLettre) > ord("Z"):
            uneLettre = " "
        print("\u2551" + uneLettre, end="")
    print("\u2551")
    if cptLigne != 4:
        print(ligneInt)
print(cadreBas)
"""

"""temps = int(input("saisir un temps: "))
jour = temps //86400
rest = temps % 86400
heure = rest // 3600
rest = rest % 3600
minute = rest // 60
seconde = rest % 60
print(temps, "secondes représente:", end= "")
if jour > 0:
     print(" ", jour, "jour", end="")
     if jour > 1:
          print("jours", end="")
if heure > 0:
     print(heure, "heure", end="")
     if heure > 1:
          print("heures", end="")
if minute > 0:
     print(" ", minute, "minute", end="")
     if minute > 1:
          print("minutes", end="")
if seconde > 0:
     print(" ", seconde, "seconde", end=" ")
     if seconde > 1:
          print("secondes")
print(".")
"""
"""stop = False
while not (stop):
    col = int(input("combien de colonnes entre 1 et 26: "))
while not (col >= 1 and col <= 26 or col == -1):
    print(f"{col} n'est bien compris entre 1 et 26.")
    col = int(input("combien de colonnes entre 1 et 26: "))
    if col == -1:
        stop = True
        if not (stop):
          cadreHaut = "\u2554" + "\u2550\u2566" * 5 + "\u2550\u2557"
          ligneInt = "\u2560" + "\u2550\u256C" * 5 + "\u2550\u2563"
          cadreBas = "\u255A" + "\u2550\u2569" * 5 + "\u2550\u255D"
          nbLigne = 26 // col
          if 26 % col != 0:
            nbLigne += 1
          for cptLigne in range(nbLigne):
             for cptCol in range(col):
                uneLettre = chr(65 + cptCol + cptLigne * 6)
                if ord(uneLettre) > ord("Z"):
                    uneLettre = " "
          print("\u2551" + uneLettre, end="") 
          print("\u2551")
          if cptLigne != nbLigne - 1: 
             print("\u2560" + "\u2550\u256C" * (col - 1) + "\u2550\2563") 
    col = int(input("combien de colonnes entre 1 et 26: ")) 
"""
"""hauteur = int(input("saisir la hauteur: "))
for nbLigne in range(1, hauteur + 1):
    for nbespace in range(1, hauteur - nbLigne + 1):
        print("", end="")
    for nbCar in range(2 * nbLigne - 1):
        print(" x")
        print()
"""


"""hauteur = int(input("Saisir une hauteur: "))

for cpt in range(1, hauteur + 1):
    if cpt == 1:
        print(" " * (hauteur - 1) + "^")
    else:
        espaces = " " * (hauteur - cpt)
        uneChaine = ("+o" * (cpt - 2) + "+")
        print(espaces + "^" + uneChaine + "^")
pipe = " " * (hauteur - 1) + "|"
socle = " " * (hauteur - 2) + "==="
print(pipe)
print(socle)
"""
#exercice sur les fonctions:
"""f = lambda x: 2 * x ** 2 - 3 * x + 2
for cpt in range(-10, 21):
    x = cpt / 10
    res = round(f(x), 2)
    print(f"f{x} = {res}") 
"""
#exercice fonction récursive avec la factorielle:
"""def factorielle(n):
    if n ==  0:
        return 1
    else:
        return n * factorielle (n - 1)
for cpt in range(0, 10):
        print(f"{cpt}! = {factorielle(cpt)}")

#fonction récurssive avec la suite de fibonnassi
"""
"""def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)
for cpt in range(10):
        print(f"U{cpt} = {fibo(cpt)}") 
"""
#def puissance(a, n):
 # """fonction qui retourne la puissance d'un nombre 
  #  paramètres:
   # a = le nombre
    #n = la puissance
    #"""
    #if n == 0:
     #   return 1
    #else:
     #   return a * puissance(a, n - 1)
#a = int(input("donner un nombre: "))
#n = int(input("donner la puissance: "))
#print(f"{a} ^ {n} = {puissance(a, n)}")
#"""
"""def maxDeuxNombres(a, b):
    if a > b:
       return a
    else:
        return b 
    
def maxtroisNombres(x, y, z):
    result = maxDeuxNombres(x, y)
    if z > result:
        return z
    else:
       return result
    
a = int(input("saisir un nombre: "))
b = int(input("saisir un nombre: "))
c = int(input("saisir un nombre: "))
resultat = maxtroisNombres(a, b, c)
print(f"le résultat est {resultat}")
"""
"""def maxtroisNombres(k, l , m):
    if k > l:
        res = k 
        #print(k) 
        if m > res:
          print(f"le max est {m}") 
        else:
         print(f"le max est {res}") 
    else:
        res = l
        #print(l)
        if m > l:
          print(f"le meax est {m}") 
        else:
           print(f"le max est {res}") 
k = int(input("donner le 1er: "))
l = int(input("donner le second: "))
m = int(input("donner le 3eme: "))  
maxtroisNombres(k, l, m) 
"""
"""def checkParfait(n):
    somme = 0
    for cpt in range(1, n):
        if n % cpt == 0:
            somme += cpt
    if somme == n:
        print(f"le nombre {n} est parfait.")
    else:
        print(f"le nombre {n} n'est pas parfait.")
n = int(input("saisir un nombre: "))
checkParfait(n)
"""
"""def addition(n):
    "fonction qui retourne la somme des nombres entre 0 et n 
    paramètre:
    le nombre n
    "
    somme = 0
    for cpt in range(n + 1):
        somme += cpt
    print(somme)

n = int(input("saisir un nombre: "))
addition(n)
"""
"""def checkSomme(a, b, c):
    somme = (a + b + c)
    if somme < 21:
        print(f"la somme est {somme}")
    else:
        print("C'est fini")
    if somme > 21 and (a == 11 or b == 11 or c == 11):
        somme = somme  - 10
        print(f"la somme est {somme}")
a = int(input("a ? : "))
b = int(input("b ? : "))
c = int(input("c ? : "))
checkSomme(a, b, c)
"""
"""def palindrome(n):
    #convertissons ce nombre en chaine de caractères
    caractere = str(n)
    #inversons la chaine de caracrère
    inverse = caractere[::-1]
    if caractere == inverse:
        print("est un palindrome")
    else:
        print("n'est pas un palindrome")
n = int(input("saisir un nombre: "))
palindrome(n)
"""
"""n = 123
inverse = 0
while n != 0:
    rest = n % 10
    inverse = (inverse * 10) + rest 
    n = n // 10
print(inverse)
"""
#exercice 1 sur les dictionnaires 
"""from random import randrange
listeNotes = []
for cptE in range(10):
    unEtudiant = {}
    unEtudiant["Nom"] = f"Nom{cptE + 1}"
    listeN =[]
    for cptN in range(4):
        listeN.append(randrange(0, 20))
    unEtudiant["Notes"] = listeN
    unEtudiant["Moyenne"] = round(sum(listeN) /4,2)
    listeNotes.append(unEtudiant)
for unEtu in listeNotes:
    print(unEtu) 
"""     
#exercice 2 sur les dictionnaires

   

        



    

 
 


      


    





    



    
            





    





    









    










    
  



        












































































































































































































































































































































































































































































































































   

