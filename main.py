import hashlib


def hash_password(password):
    # Fonction pour hacher le mot de passe avec SHA256
    result = hashlib.sha256(password.encode()).hexdigest()
    return result

def mot_de_passe():
    # Fonction pour valider le mot de passe de l'utilisateur
    lettres_min = ["a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lettres_maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    caracteres_speciaux = ["!", "@", "#", "$", "%", "^", "&", "*"]

    while True:
        password = input("Veuillez entrer votre mot de passe : ")
        if len(password) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères.")
        elif not any(char in lettres_min for char in password):
            print("Le mot de passe doit contenir au moins une lettre minuscule.")
        elif not any(char in lettres_maj for char in password):
            print("Le mot de passe doit contenir au moins une lettre majuscule.")
        elif not any(char in chiffres for char in password):
            print("Le mot de passe doit contenir au moins un chiffre.")
        elif not any(char in caracteres_speciaux for char in password):
            print("Le mot de passe doit contenir au moins un caractère spécial.")
        else:
            print("Le mot de passe est valide.")
            hashed_password = hash_password(password)
            return hashed_password

print(mot_de_passe())
