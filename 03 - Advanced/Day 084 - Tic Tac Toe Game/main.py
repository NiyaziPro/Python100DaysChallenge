import random
import os


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board represented as a list
        self.current_player = 'X'
        self.game_mode = None

    def clear_screen(self):
        """Clear the terminal screen for better user experience"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self):
        """Display the current state of the game board"""
        print("\n   |   |   ")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   ")
        print()

    def display_positions(self):
        """Show the position numbers for reference"""
        print("Position numbers:")
        print("\n   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   ")
        print()

    def is_valid_move(self, position):
        """Check if the move is valid"""
        return 1 <= position <= 9 and self.board[position - 1] == ' '

    def make_move(self, position, player):
        """Make a move on the board"""
        if self.is_valid_move(position):
            self.board[position - 1] = player
            return True
        return False

    def check_winner(self):
        """Check if there's a winner"""
        # Winning combinations (indices)
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]
                    and self.board[combo[0]] != ' '):
                return self.board[combo[0]]
        return None

    def is_board_full(self):
        """Check if the board is full (tie game)"""
        return ' ' not in self.board

    def switch_player(self):
        """Switch between X and O"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_move(self):
        """Get move from human player"""
        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter your move (1-9): "))
                if self.is_valid_move(position):
                    return position
                else:
                    print("Invalid move! That position is already taken or out of range.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

    def get_available_moves(self):
        """Get list of available positions"""
        return [i + 1 for i, spot in enumerate(self.board) if spot == ' ']

    def minimax(self, board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
        """Minimax algorithm with alpha-beta pruning for AI"""
        # Create a temporary board state
        temp_board = self.board[:]
        self.board = board[:]

        winner = self.check_winner()

        # Restore original board
        self.board = temp_board[:]

        # Base cases
        if winner == 'O':  # AI wins
            return 10 - depth
        elif winner == 'X':  # Human wins
            return depth - 10
        elif ' ' not in board:  # Tie
            return 0

        if is_maximizing:  # AI's turn
            max_eval = -float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    eval_score = self.minimax(board, depth + 1, False, alpha, beta)
                    board[i] = ' '
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break
            return max_eval
        else:  # Human's turn
            min_eval = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    eval_score = self.minimax(board, depth + 1, True, alpha, beta)
                    board[i] = ' '
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break
            return min_eval

    def get_ai_move(self):
        """Get the best move for AI using minimax algorithm"""
        best_score = -float('inf')
        best_move = None

        # Try all available moves
        for i in range(9):
            if self.board[i] == ' ':
                # Make the move
                board_copy = self.board[:]
                board_copy[i] = 'O'

                # Calculate score
                score = self.minimax(board_copy, 0, False)

                # If this move is better than the best so far, save it
                if score > best_score:
                    best_score = score
                    best_move = i + 1

        return best_move

    def choose_game_mode(self):
        """Let player choose game mode"""
        print("🎮 Welcome to Tic Tac Toe! 🎮")
        print("\nChoose game mode:")
        print("1. Two Players (X vs O)")
        print("2. Player vs AI (You are X, AI is O)")

        while True:
            try:
                choice = int(input("\nEnter your choice (1 or 2): "))
                if choice in [1, 2]:
                    self.game_mode = choice
                    break
                else:
                    print("Please enter 1 or 2.")
            except ValueError:
                print("Please enter a valid number.")

    def play_game(self):
        """Main game loop"""
        self.choose_game_mode()
        self.clear_screen()

        if self.game_mode == 1:
            print("🎮 Two Player Mode 🎮")
        else:
            print("🤖 Player vs AI Mode 🤖")
            print("You are X, AI is O")

        self.display_positions()

        while True:
            self.display_board()

            # Get move based on game mode and current player
            if self.game_mode == 1 or self.current_player == 'X':
                # Human player move
                position = self.get_player_move()
            else:
                # AI move
                print("🤖 AI is thinking...")
                position = self.get_ai_move()
                print(f"AI chooses position {position}")

            # Make the move
            self.make_move(position, self.current_player)

            # Check for winner
            winner = self.check_winner()
            if winner:
                self.clear_screen()
                self.display_board()
                if self.game_mode == 2 and winner == 'O':
                    print(f"🤖 AI (O) wins! Better luck next time!")
                elif self.game_mode == 2 and winner == 'X':
                    print(f"🎉 Congratulations! You (X) beat the AI!")
                else:
                    print(f"🎉 Player {winner} wins! Congratulations!")
                break

            # Check for tie
            if self.is_board_full():
                self.clear_screen()
                self.display_board()
                print("🤝 It's a tie! Good game!")
                break

            # Switch players
            self.switch_player()

    def play_again(self):
        """Ask if players want to play again"""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'.")


def main():
    """Main function to run the game"""
    print("🎮 Welcome to Tic Tac Toe! 🎮")

    while True:
        game = TicTacToe()
        game.play_game()

        if not game.play_again():
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()