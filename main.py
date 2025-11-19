import random

def afficher(board):
    print(board[1], "|", board[2], "|", board[3])
    print("--+---+--")
    print(board[4], "|", board[5], "|", board[6])
    print("--+---+--")
    print(board[7], "|", board[8], "|", board[9])

def victoire(board, s):
    combinaisons = [
        (1,2,3), (4,5,6), (7,8,9),
        (1,4,7), (2,5,8), (3,6,9),
        (1,5,9), (3,5,7)
    ]
    for a,b,c in combinaisons:
        if board[a] == board[b] == board[c] == s:
            return True
    return False

#ia aléatoire
def ia_aleatoire(board):
    coups_possibles = [i for i in range(1, 10) if board[i] == " "]
    return random.choice(coups_possibles)


def jouer():
    board = [" "] * 10
    joueur = "X"

    while True:

        afficher(board)

        if joueur == "X":
            case = int(input("Votre coup (1-9) : "))
            if board[case] != " ":
                print("Case déjà occupée !")
                continue
        else:
            print("L’IA joue...")
            case = ia_aleatoire(board)

        board[case] = joueur

        if victoire(board, joueur):
            print("Le joueur", joueur, "a gagné !")
            break

        if " " not in board:
            print("Match nul !")
            break

        joueur = "O" if joueur == "X" else "X"

jouer()