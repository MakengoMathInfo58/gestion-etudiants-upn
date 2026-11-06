# Projet UPN - Par MakengoMathInfo58
etudiants = []

def ajouter_etudiant():
    nom = input("Nom: ")
    matricule = input("Matricule: ")
    etudiants.append({"nom": nom, "matricule": matricule})
    print(f"{nom} ajoute!")

def afficher():
    for e in etudiants:
        print(f"- {e['nom']} | {e['matricule']}")

while True:
    print("\n1.Ajouter 2.Afficher 3.Quitter")
    choix = input("Choix: ")
    if choix == "1":
        ajouter_etudiant()
    elif choix == "2":
        afficher()
    elif choix == "3":
        break
