from math import sqrt, pi 


toiture = int(input("Saisissez la surface de la toiture en m²: "))
print(f"La toiture mesure {toiture} m².")
print(f"La descente d'eau est donc de {toiture} cm².")

nb_dep = int(input("Saisissez le nombre de DEP: "))
surf_dep = toiture/nb_dep                               #calcul de la surface (quelle surface?)
diam_dep = sqrt((4*surf_dep)/pi)*10                     #calcul du diamètre des DEP
print("\n")
print(f"Diamètre des DEP obtenu: {diam_dep} mm.")
print("Veuillez consulter le catalogue pour trouver le DEP le mieux adapté (avec la taille la plus proche de celle calculée).")

#____________________________________________________________________________________________________________________

nb_section = int(input("Saisissez le nombre de sections: "))
surf_section = (toiture/nb_section)*2
taille_section = sqrt(surf_section)

print("\n")
print(f"Taille du chéneau obtenu: {taille_section} cm de côté, soit {taille_section*10} mm.")
print("Veuillez consulter le catalogue pour trouver les dimensions de chéneau les mieux adaptées (avec la taille la plus proche de celle calculée).")