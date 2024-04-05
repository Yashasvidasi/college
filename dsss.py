class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-------------')

    def drop_disc(self, column):
        for i in range(5, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.current_player
                return True
        return False

    def check_winner(self):
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if (self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3]) and \
                        self.board[row][col] != ' ':
                    return True

        # Check vertical
        for row in range(3):
            for col in range(7):
                if (self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col]) and \
                        self.board[row][col] != ' ':
                    return True

        # Check diagonal (left to right)
        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3]) and \
                        self.board[row][col] != ' ':
                    return True

        # Check diagonal (right to left)
        for row in range(3):
            for col in range(3, 7):
                if (self.board[row][col] == self.board[row + 1][col - 1] == self.board[row + 2][col - 2] == self.board[row + 3][col - 3]) and \
                        self.board[row][col] != ' ':
                    return True

        return False

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def play(self):
        while True:
            self.print_board()
            column = int(input(f"Player {self.current_player}, enter column (0-6): "))
            if column < 0 or column > 6:
                print("Column out of range. Please choose a number between 0 and 6.")
                continue
            if not self.drop_disc(column):
                print("Column is full. Choose another column.")
                continue
            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            if all(self.board[i][j] != ' ' for i in range(6) for j in range(7)):
                self.print_board()
                print("It's a tie!")
                break
            self.switch_player()


if __name__ == "__main__":
    game = ConnectFour()
    game.play()

