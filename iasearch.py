# iasearch.py

class AIPlayer:
    def __init__(self, board, game_logic):
        # Inicializa el jugador de la IA con el tablero y la lógica del juego
        self.board = board
        self.game_logic = game_logic

    def minimax(self, depth, maximizing_player):
        # Algoritmo Minimax
        pass

    def evaluate_tile_weight(self, row, col):
        # Asigna pesos a las casillas según su ubicación
        if (row == 0 or row == self.board.size - 1) and (col == 0 or col == self.board.size - 1):
            return 10  # Esquina
        elif row == 0 or row == self.board.size - 1 or col == 0 or col == self.board.size - 1:
            return 5  # Borde
        else:
            return 1  # Centro

    def evaluate_mobility(self):
        # Evalúa la movilidad de los jugadores
        valid_moves_x = len(self.board.get_valid_moves('X'))
        valid_moves_o = len(self.board.get_valid_moves('O'))
        return valid_moves_x - valid_moves_o

    def evaluate_stability(self):
        # Evalúa la estabilidad del tablero
        board_state = self.board.get_board_state()
        score = 0
        for row in range(self.board.size):
            for col in range(self.board.size):
                if board_state[row][col] == 'O':
                    score += self.get_tile_stability(row, col, 'O')
                elif board_state[row][col] == 'X':
                    score -= self.get_tile_stability(row, col, 'X')
        return score

    def dificil(self):
        # Evalúa la dificultad del juego combinando diferentes puntuaciones
        tile_weight_score = self.evaluate_tile_weight()
        mobility_score = self.evaluate_mobility()
        stability_score = self.evaluate_stability()
        
        # Combina las puntuaciones según la estrategia
        total_score = tile_weight_score + mobility_score + stability_score
        
        return total_score
