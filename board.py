# board.py

class Board:
        def __init__(self, size):
            # Inicializa un objeto de tablero con un tamaño dado
            self.size = size
            # Crea una matriz vacía del tamaño especificado
            self.board = [[' ' for _ in range(size)] for _ in range(size)]

            # Inicializa el tablero con las fichas iniciales en el centro
            mid = size // 2
            self.board[mid - 1][mid - 1] = 'O'
            self.board[mid][mid] = 'O'
            self.board[mid - 1][mid] = 'X'
            self.board[mid][mid - 1] = 'X'

        def set_size(self, size):
            # Cambia el tamaño del tablero
            self.size = size
            # Crea una nueva matriz vacía del nuevo tamaño
            self.board = [[' ' for _ in range(size)] for _ in range(size)]

        def place_piece(self, row, col, player):
            # Coloca una ficha en una posición específica si el movimiento es válido
            if self.is_valid_move(row, col, player):
                self.board[row][col] = player

        def is_valid_move(self, row, col, player):
            # Comprueba si un movimiento es válido para un jugador dado
            if self.board[row][col] != ' ':
                return False

            # Comprobar si hay una ficha adyacente del oponente en alguna dirección
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
            opponent = 'X' if player == 'O' else 'O'
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == opponent:
                    while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == opponent:
                        r += dr
                        c += dc
                    if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                        return True

            return False

        def get_valid_moves(self, player):
            # Obtiene una lista de movimientos válidos para un jugador dado
            valid_moves = []
            for row in range(self.size):
                for col in range(self.size):
                    if self.is_valid_move(row, col, player):
                        valid_moves.append((row, col))
            return valid_moves

        def get_board_state(self):
            # Obtiene el estado actual del tablero (matriz)
            return self.board

        def print_board(self):
            # Imprime el tablero en la consola con un formato visual
            for row in self.board:
                print(' | '.join(row))
                print('-' * (4 * self.size - 1))

        def reset_board(self):
            # Reinicia el tablero, estableciendo todas las casillas en ' '
            for row in range(self.size):
                for col in range(self.size):
                    self.board[row][col] = ' '
