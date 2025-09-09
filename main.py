from tic_tac_toe import TicTacToe
import random


def test_tic_tac_toe():
    print("=== Tests de la classe TicTacToe ===\n")

    # Test 1: Initialisation
    print("Test 1: Initialisation")
    game = TicTacToe()
    print("Grille initiale:")
    print(game)
    print(f"Joueur actuel: {game.joueur}")
    print(f"Cases disponibles: {game.allowed_moves()}")
    print()

    # Test 2: Jouer quelques coups
    print("Test 2: Jouer des coups")
    game.play(0)  # X joue en position 0
    print("Après X joue en 0:")
    print(game)
    print(f"Joueur actuel: {game.joueur}")

    game.play(1)  # O joue en position 1
    print("Après O joue en 1:")
    print(game)
    print(f"Joueur actuel: {game.joueur}")
    print()

    # Test 3: Test d'erreur sur case occupée
    print("Test 3: Erreur case occupée")
    try:
        game.play(0)  # Devrait lever une exception
    except ValueError as e:
        print(f"Exception attendue: {e}")
    print()

    # Test 4: Test de victoire horizontale
    print("Test 4: Victoire horizontale")
    game.reset()
    game.play(0)  # X
    game.play(3)  # O
    game.play(1)  # X
    game.play(4)  # O
    game.play(2)  # X gagne (ligne du haut)
    print("Grille finale:")
    print(game)
    print(f"Has winner: {game.has_winner()}")
    print()

    # Test 5: Test de victoire verticale
    print("Test 5: Victoire verticale")
    game.reset()
    game.play(0)  # X
    game.play(1)  # O
    game.play(3)  # X
    game.play(2)  # O
    game.play(6)  # X gagne (colonne gauche)
    print("Grille finale:")
    print(game)
    print(f"Has winner: {game.has_winner()}")
    print()

    # Test 6: Test de victoire diagonale
    print("Test 6: Victoire diagonale")
    game.reset()
    game.play(0)  # X
    game.play(1)  # O
    game.play(4)  # X
    game.play(2)  # O
    game.play(8)  # X gagne (diagonale principale)
    print("Grille finale:")
    print(game)
    print(f"Has winner: {game.has_winner()}")
    print()

    # Test 7: Test de match nul
    print("Test 7: Match nul")
    game.reset()
    # Simulation d'un match nul
    moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]  # Séquence qui mène à un match nul
    for move in moves:
        game.play(move)
        if game.has_winner():
            print("Victoire détectée prématurément!")
            break
    print("Grille finale:")
    print(game)
    print(f"Has winner: {game.has_winner()}")
    print(f"Is draw: {game.is_draw()}")
    print()

    # Test 8: Test undo
    print("Test 8: Test undo")
    game.reset()
    game.play(0)  # X
    print("Avant undo:")
    print(game)
    print(f"Joueur actuel: {game.joueur}")

    game.undo(0)
    print("Après undo:")
    print(game)
    print(f"Joueur actuel: {game.joueur}")
    print()


if __name__ == "__main__":
    test_tic_tac_toe()




def opponent_random(game):
    allowed = game.allowed_moves
    if allowed:
        move = random.choice(allowed)
        game.play(move)
        return move
    return None
