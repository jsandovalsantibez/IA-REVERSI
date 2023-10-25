# gameLogic.py
import random

class ReversiGame:
    def __init__(self, board):
        # Inicializa el juego con el tablero y el jugador actual
        self.board = board
        self.current_player = 'X'  # Comienza el jugador X

    def initialize_game(self):
        # Inicializa el juego colocando las fichas iniciales en el tablero
        mid = self.board.size // 2
        self.board.board[mid - 1][mid - 1] = 'O'
        self.board.board[mid][mid] = 'O'
        self.board.board[mid - 1][mid] = 'X'
        self.board.board[mid][mid - 1] = 'X'

    def make_move(self, row, col):
        # Coloca una ficha en el tablero si el movimiento es válido
        if self.board.is_valid_move(row, col, self.current_player):
            self.board.board[row][col] = self.current_player
            self.flip_pieces(row, col, self.current_player)
            self.current_player = 'O' if self.current_player == 'X' else 'X'

            # Llama a la función para que la computadora realice una jugada al azar
            self.computer_move()

    def computer_move(self):
        if self.current_player == 'O':
            valid_moves = self.board.get_valid_moves('O')
            if valid_moves:
                row, col = random.choice(valid_moves)
                self.board.place_piece(row, col, 'O')
                self.flip_pieces(row, col, 'O')
                self.current_player = 'X'

    def reset_game(self):
        # Reinicia el juego
        self.board.reset_board()  # Agrega esta línea para reiniciar el tablero
        self.current_player = 'X'  # Reinicia al jugador actual

    def flip_pieces(self, row, col, player):
        # Voltea las fichas del oponente en las direcciones válidas
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            pieces_to_flip = []
            while 0 <= r < self.board.size and 0 <= c < self.board.size and self.board.board[r][c] != player:
                if self.board.board[r][c] != ' ':
                    pieces_to_flip.append((r, c))
                else:
                    break
                r += dr
                c += dc
            if 0 <= r < self.board.size and 0 <= c < self.board.size and self.board.board[r][c] == player:
                for pr, pc in pieces_to_flip:
                    self.board.board[pr][pc] = player

    def change_turn(self):
        # Cambia el turno al siguiente jugador
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_game_over(self):
        # Verifica si el juego ha terminado
        valid_moves_x = self.board.get_valid_moves('X')
        valid_moves_o = self.board.get_valid_moves('O')
        return len(valid_moves_x) == 0 and len(valid_moves_o) == 0

    def get_winner(self):
        # Determina al ganador del juego
        x_count = sum(row.count('X') for row in self.board.get_board_state())
        o_count = sum(row.count('O') for row in self.board.get_board_state())
        if x_count > o_count:
            return 'X'
        elif o_count > x_count:
            return 'O'
        else:
            return 'Empate'
