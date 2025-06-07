
##  Note explicative du projet : Calculatrice Python Basique

### Objectif pédagogique

Ce projet a été conçu comme un **exercice de consolidation des bases en Python**, en mettant l'accent sur :

* La **gestion des erreurs (exceptions)** ;
* Les **boucles `while True` imbriquées** ;
* La **validation des entrées utilisateur** ;
* La **structure logique d’un petit programme interactif** ;
* Le **nettoyage des entrées** avec `.strip()` et `.lower()`.

Il s'agit de mon **premier dépôt GitHub**, destiné à documenter ma progression dans l’apprentissage de Python en vue d’une reconversion vers la data science.

---

### Fonctionnement du programme

Le script Python `calculatrice_python_basique.py` propose une **calculatrice interactive** capable d’effectuer les opérations suivantes entre deux nombres saisis par l'utilisateur :

1. Addition
2. Soustraction
3. Multiplication
4. Division (avec gestion du cas interdit de division par zéro)
5. Quitter le programme

Chaque étape de saisie est **protégée par une boucle `while True`** pour forcer l'utilisateur à entrer une donnée correcte, jusqu’à ce que ce soit le cas.

---

### Détails du fonctionnement

#### Entrées :

* Deux nombres (float), avec gestion des erreurs (`ValueError`).
* Choix de l’opération (entre 1 et 5), avec gestion des erreurs (`ValueError` et `ZeroDivisionError`).
* Requête pour continuer ou non les calculs : saisie `"oui"` ou `"non"`.

#### Nettoyage :

* Les entrées sont nettoyées avec `.strip()` pour supprimer les espaces et `.lower()` pour standardiser la casse.

#### Sorties :

* Le résultat de l'opération, arrondi à deux décimales.
* Un message de fin si l'utilisateur choisit de quitter ou de ne pas continuer.

---

### Structure du code (avec commentaires)

* `while True` principal : boucle globale pour permettre plusieurs opérations successives.
* 3 autres boucles `while True` imbriquées :

  * Pour le 1er nombre
  * Pour le 2e nombre
  * Pour le choix d’opération
* À chaque mauvaise saisie, l'utilisateur est **re-bouclé automatiquement** dans la bonne section.
* Chaque `break` permet de sortir **uniquement** de la boucle dans laquelle on se trouve (exemple : après une saisie correcte).
* Le `return` est utilisé pour **quitter complètement le programme** (par exemple si l'utilisateur choisit de quitter).

---

### Ce que j’ai appris / appliqué

* Utilisation du `try`/`except` pour capturer et gérer les erreurs utilisateur.
* Bonne maîtrise des boucles `while True` pour **forcer la bonne saisie sans casser le programme**.
* Nettoyage des entrées pour éviter les erreurs liées à des espaces ou à la casse.
* Différence entre `if` et `elif` : `if` teste toujours, `elif` est une alternative **testée seulement si les conditions précédentes sont fausses**.
* Gestion d’une exception spécifique : **division par zéro** (`ZeroDivisionError`) gérée avec un `raise`.

---

### Perspectives d’amélioration

* Refactoriser le code avec des **fonctions séparées** (ex : `saisir_nombre()`, `choisir_operation()`)
* Ajouter la gestion de plusieurs opérations (calcul en chaîne).
* Ajouter un historique des calculs.
* Traduire en anglais pour rendre le projet plus universel.
* Créer une version avec **interface graphique** (ex : avec Tkinter) plus tard.

---

### 🧾 Fichier concerné

* `calculatrice_python_basique.py` : script principal

