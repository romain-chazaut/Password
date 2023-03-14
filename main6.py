def mot_de_passe():
    lettres_min = ["a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lettres_maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    caracteres_speciaux = ["!", "@", "#", "$", "%", "^", "&", "*"]
    
    Test_password = False
    
    while not Test_password:
        password = input("Veuillez entrer votre mot de passe : ")
        if len(password) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères.")
            Test_password = False
        elif not any(char in lettres_min for char in password):
            print("Le mot de passe doit contenir au moins une lettre minuscule.")
            Test_password = False
        elif not any(char in lettres_maj for char in password):
            print("Le mot de passe doit contenir au moins une lettre majuscule.")
            Test_password = False
        elif not any(char in chiffres for char in password):
            print("Le mot de passe doit contenir au moins un chiffre.")
            Test_password = False
        elif not any(char in caracteres_speciaux for char in password):
            print("Le mot de passe doit contenir au moins un caractère spécial.")
            Test_password = False
        else:
            Test_password = True
            print("Le mot de passe est valide.")
    
mot_de_passe()