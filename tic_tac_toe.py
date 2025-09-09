class TicTacToe:
    def __init__(self):
        self.grille = ['.', '.','.','.','.','.','.','.','.',]
        self.joueur = 'x'


    def play(self, number):
        if not (0 <= number <= 8):
            raise ValueError("Le numéro doit être entre 0 et 8")
        if self.grille[number] != '.':
            raise ValueError("Cette case est déjà occupée")
        else:
            if self.joueur == 'x':
                self.grille[number] = 'x'
                self.joueur = 'o'
            else:
                self.grille[number] = 'o'
                self.joueur = 'x'

    def __str__(self):
        result = ""
        for i in range(3):
            for j in range(3):
                result += self.grille[i * 3 + j] + " "
            result += "\n"
        return result.strip()

    def has_winner(self):
        linear_win = (self.grille[0] == self.grille[1] == self.grille[2] != '.') or \
                     (self.grille[3] == self.grille[4] == self.grille[5] != '.') or \
                     (self.grille[6] == self.grille[7] == self.grille[8] != '.')

        vertical_win = (self.grille[0] == self.grille[3] == self.grille[6] != '.') or \
                       (self.grille[1] == self.grille[4] == self.grille[7] != '.') or \
                       (self.grille[2] == self.grille[5] == self.grille[8] != '.')

        diagonal_win = (self.grille[0] == self.grille[4] == self.grille[8] != '.') or \
                       (self.grille[2] == self.grille[4] == self.grille[6] != '.')

        return linear_win or vertical_win or diagonal_win

    def is_draw(self):
        return not self.has_winner() and '.' not in self.grille


    def reset(self):
        self.__init__()

    def undo(self, index):
        if self.grille[index] != '.':
            self.grille[index] = '.'
            self.joueur = 'o' if self.joueur == 'x' else 'x'


    def allowed_moves(self):
        moves = []
        for i in range(len(self.grille)):
            if self.grille[i] == '.':
                moves.append(i)
        return moves


    
