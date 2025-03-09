# Question 1

def initHanoi(n):
    # Création de la première liste avec les entiers de n à 1
    tour1 = []
    for cpt in range(n, 0, -1):
        tour1.append(cpt)

    # Création des deux autres listes vides
    tour2 = []
    tour3 = []
    
    # Retourne la liste de trois éléments
    grandeListe =  [tour1, tour2, tour3]
    return grandeListe

# Exemple d'utilisation
resultat = initHanoi(4)
print(resultat)


#Question 2
def afficheHanoi(tours):
    max_height = 0
    for tour in tours:
      max_height = max(max_height, len(tour)) #on détermine la hauteur de la grande tour  
    
    for i in range(max_height - 1, -1, -1): #avec la boucle for, on itère chaque element 
        for tour in tours:
            if i < len(tour):
                print(f"{tour[i]}", end=" ") #on affiche la tour que lorsque sa hauteur est inférieure à la largeur de la tour 
            else:
                print("   ", end=" ")
        print()                              # Nouvelle ligne après chaque niveau

    for indiceTour in range(len(tours)):
        print(f"[{indiceTour}]", end=" ")
    print()                                 # Nouvelle ligne pour l'affichage des indices

# Exemples d'utilisation
afficheHanoi([[4, 3, 2, 1], [], []])

#Question 3
def joueHanoi(tours):
    while len(tours[0]) != 0 or len(tours[1]) != 0: #tant que la tour 1 et 2 ne sont pas vides 
        afficheHanoi(tours)
        source = int(input("Source : "))   # l'utilisateur saisit une soure et une destination
        
        
        if len(tours[source]) == 0:
            print("La tour source est vide.")
        else:
            destination = int(input("Destination : "))

        

        if  len(tours[destination]) == 0 or (len(tours[source]) > 0 and tours[source][-1] < tours[destination][-1]):
            #avec cette condition on vérifie si la tour de destiation est vide ou que Cela vérifie si le disque du dessus de la tour source (tours[source][-1])
            # est plus petit que le disque du dessus de la tour destination (tours[destination][-1])
           
             disque_a_deplacer = tours[source].pop()  #si cette condition est vérifiée, alors on retire l'élémént 
             #qui se trouve au dessus de la source et on le stocke dans une variable
             tours[destination].append(disque_a_deplacer)   #dans la tour destination, on rajoute cet élément à déplacer 
            
        else:
            print("Mouvement impossible. Le disque source est plus grand que le disque destination.")
            #si toutes ces conditions ne sont pas remplis alors le mouvement est impossible.

    afficheHanoi(tours)


# Exemple d'utilisation
joueHanoi([[3, 2, 1], [], []])

#Question 4
def bougeHanoi(tours, n, depuisTour, versTour):
    #pour le première partie, on déplace les n - 1ème éléménts de la tour vers une tour dénomée transit qui est 
    #intermédiaire
    if n > 0: 
      transitTour = 3 - depuisTour - versTour
      bougeHanoi(tours, n - 1, depuisTour, transitTour)
    #pour la deuxième partie, je récupère le nème élement de cette tour que je place dans la tour finale versTour
    disque_a_deplacer = tours[depuisTour].pop()
    tours[versTour].append(disque_a_deplacer)
    afficheHanoi(tours)
    #pour cette dernière partie, je transfère les n - 1 ème éléments dans la tour finale 
    bougeHanoi(tours, n - 1, transitTour, versTour)
bougeHanoi([[3, 2, 1], [], []], 3, 0, 2)



