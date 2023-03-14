password = input("Veuillez entrer votre mot de passe : ")

def mot_de_passe():
    lettres_min = ["a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lettres_maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    caracteres_speciaux = ["!", "@", "#", "$", "%", "^", "&", "*"]

    # Vérifie si le mot de passe a au moins 8 caractères
    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        return

    # Vérifie si le mot de passe a au moins une lettre minuscule
    lettre_min_trouvee = False
    for char in password:
        if char in lettres_min:
            lettre_min_trouvee = True
            break
    if not lettre_min_trouvee:
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        return

    # Vérifie si le mot de passe a au moins une lettre majuscule
    lettre_maj_trouvee = False
    for char in password:
        if char in lettres_maj:
            lettre_maj_trouvee = True
            break
    if not lettre_maj_trouvee:
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        return

    # Vérifie si le mot de passe a au moins un chiffre
    chiffre_trouve = False
    for char in password:
        if char in chiffres:
            chiffre_trouve = True
            break
    if not chiffre_trouve:
        print("Le mot de passe doit contenir au moins un chiffre.")
        return

    # Vérifie si le mot de passe a au moins un caractère spécial
    caractere_special_trouve = False
    for char in password:
        if char in caracteres_speciaux:
            caractere_special_trouve = True
            break
    if not caractere_special_trouve:
        print("Le mot de passe doit contenir au moins un caractère spécial.")
        return

    print("Le mot de passe est correct.")

mot_de_passe()
