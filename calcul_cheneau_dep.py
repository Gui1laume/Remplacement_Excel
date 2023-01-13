from math import sqrt, pi 

#DEP
toiture = int(input("Saisissez la surface de la toiture en m²: "))
print(f"La toiture mesure {toiture} m².")
print(f"La descente d'eau est donc de {toiture} cm².")

nb_dep = int(input("Saisissez le nombre de DEP: "))
surf_dep = toiture//nb_dep                               #calcul de la surface du disque du DEP
diam_dep = sqrt((4*surf_dep)//pi)*10                     #calcul du diamètre des DEP
print("\n")
print(f"Diamètre des DEP obtenu: {round(diam_dep)} mm.")
print("Veuillez consulter le catalogue pour trouver la DEP la mieux adaptée (avec la taille la plus proche de celle calculée).")


#____________________________________________________________________________________________________________________

#CHENEAU
nb_section = int(input("Saisissez le nombre de sections: "))
surf_section = (toiture//nb_section)*2                  #calcul de la surface d'un chéneau carré (de face)
taille_section = sqrt(surf_section)                     #calcul d'un côté du même chéneau carré

print("\n")
print(f"Taille du chéneau (carré) obtenue: {round(taille_section)}cm de côté, soit {round(taille_section)*10}mm.")
print("Veuillez choisir une taille adaptée à la charpente ou proche d'une déjà réalisée.")