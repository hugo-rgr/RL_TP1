class TicTacToe:
    def __init__(self):
        self.grille = ['.', '.','.','.','.','.','.','.','.',]
        self.joueur = 'x'


    def play(self, number):
        if self.grille[number] != '.':
            return print('erreur')
        else:
            if self.joueur == 'x':
                self.grille[number] = 'x'
                self.joueur = 'o'
            else:
                self.grille[number] = 'o'
                self.joueur = 'x'

    def __str__(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.grille[j+i])

        return ''

    def has_winner(self):
        linear_win = self.grille[0] == self.grille[1] == self.grille[2] or self.grille[3] == self.grille[4] == self.grille[5] or self.grille[6] == self.grille[7] == self.grille[8] == self.joueur
        vertical_win =  self.grille[0] == self.grille[3] == self.grille[6] or self.grille[1] == self.grille[4] == self.grille[7] or self.grille[2] == self.grille[5] == self.grille[8] == self.joueur
        diagonal_win = self.grille[0] == self.grille[4] == self.grille[9] or self.grille[2] == self.grille[4] == self.grille[6] == self.joueur

        return linear_win or vertical_win or diagonal_win

    def is_draw(self):
        return not self.has_winner()


    def reset(self):
        self.__init__()

    def undo(self, index):
        self.grille[index]='.'


    def allowed_moves(self):
        for i in range(len(self.grille)):
            if self.grille[i]=='.':
                print(i)


    
