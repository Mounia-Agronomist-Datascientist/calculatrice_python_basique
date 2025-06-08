def calculatrice_python_basique():
    print("\n ----Bienvenue dans cette calculatrice !---\n")

    while True:

        # ----- 1. Saisie du premier nombre et conversion en float -----
        while True:
            try:
                num1 = float(input("Entrez un premier nombre : ").strip())
                break
            except ValueError:
                print("Attention, saisie incorrecte, veuillez entrer un nombre\n ")

        # ----- 2. Saisie du deuxième nombre et conversion en float -----
        while True:
            try:
                num2 = float(input("Entrez un deuxième nombre : ").strip())
                break
            except ValueError:
                print("Attention, saisie incorrecte, veuillez entrer un nombre\n ")

        # ----- 3. Choix de l'opération à effectuer et affichage du résultat -----
        while True:
            try:
                choix = input(
                    "\n Quelle opération souhaitez-vous effectuer?\n\n"
                    "1. Addition (+)\n"
                    "2. Soustraction(-)\n"
                    "3. Multiplication (*)\n"
                    "4. Division (/)\n"
                    "5. Quitter \n\n"
                ).strip()

                if choix == "1":
                    total = num1 + num2
                    print(
                        f"\nLe résultat de l'addition de {num1} et {num2} est : {total:.2f}\n"
                    )
                    break
                elif choix == "2":
                    total = num1 - num2
                    print(
                        f"\nLe résultat de la soustraction de {num1} et {num2} est : {total:.2f}\n"
                    )
                    break
                elif choix == "3":
                    total = num1 * num2
                    print(
                        f"\nLe résultat de la multiplication de {num1} et {num2} est : {total:.2f}\n"
                    )
                    break
                elif choix == "4":
                    if num2 == 0:
                        raise ZeroDivisionError("Division par 0 Impossible")
                    else:
                        total = num1 / num2
                        print(
                            f"\nLe résultat de la division de {num1} et {num2} est : {total:.2f}\n"
                        )
                        break
                elif choix == "5":
                    print("Merci d'avoir utilisé cette calculatrice. Au revoir!\n")
                    return
                else:
                    raise ValueError(
                        "Votre saisie n'est pas correcte veuillez entrer un nombre entre 1 et 5!\n"
                    )

            except (ValueError, ZeroDivisionError) as e:
                print(e)

        # ----- 4. Demande à l'utilisateur s'il souhaite poursuivre les calculs avec de nouveaux chiffres -----
        while True:
            suite = (
                input("Voulez-vous effectuer une autre opération? (oui/non) : ")
                .lower()
                .strip()
            )
            if suite == "oui":
                break
            elif suite == "non":
                print("Merci d'avoir utilisé cette calculatrice. Au revoir!\n")
                return
            else:
                print(
                    "Votre saisie n'est pas correcte veuillez répondre par 'oui' ou 'non'\n"
                )


calculatrice_python_basique()
