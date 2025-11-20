import random

def afficher(board):
    print(board[1], "|", board[2], "|", board[3])
    print("--+---+--")
    print(board[4], "|", board[5], "|", board[6])
    print("--+---+--")
    print(board[7], "|", board[8], "|", board[9])
    print()

def victoire(board, s):
    combinaisons = [
        (1,2,3), (4,5,6), (7,8,9),
        (1,4,7), (2,5,8), (3,6,9),
        (1,5,9), (3,5,7)
    ]
    return any(board[a] == board[b] == board[c] == s for a,b,c in combinaisons)

def minimax(board, joueur):
    # IA = O
    # Humain = X

    if victoire(board, "O"):
        return 1
    if victoire(board, "X"):
        return -1
    if " " not in board[1:]:
        return 0

    coups_possibles = [i for i in range(1, 10) if board[i] == " "]

    if joueur == "O":  
        meilleur_score = -999
        for move in coups_possibles:
            board[move] = "O"
            score = minimax(board, "X")
            board[move] = " "
            meilleur_score = max(meilleur_score, score)
        return meilleur_score

    else:
        meilleur_score = 999
        for move in coups_possibles:
            board[move] = "X"
            score = minimax(board, "O")
            board[move] = " "
            meilleur_score = min(meilleur_score, score)
        return meilleur_score

#ia minimax

def ia_parfaite(board):
    coups_possibles = [i for i in range(1, 10) if board[i] == " "]

    meilleur_score = -999
    meilleur_coup = None

    for move in coups_possibles:
        board[move] = "O"
        score = minimax(board, "X")
        board[move] = " "
        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = move

    return meilleur_coup

def jouer():
    board = [" "] * 10
    joueur = "X"

    afficher(board)

    while True:

        if joueur == "X":
            try:
                case = int(input("Votre coup (1-9) : "))
                if case < 1 or case > 9:
                    print("Saisissez un nombre entre 1 et 9.\n")
                    continue
            except ValueError:
                print("Veuillez entrer un nombre valide.\n")
                continue

            if board[case] != " ":
                print("Case déjà occupée !\n")
                continue

        else:
            print("L’IA joue...\n")
            case = ia_parfaite(board)

        board[case] = joueur
        afficher(board)

        if victoire(board, joueur):
            print("Le joueur", joueur, "a gagné !")
            break

        if " " not in board[1:]:
            print("Match nul !")
            break

        joueur = "O" if joueur == "X" else "X"

jouer()