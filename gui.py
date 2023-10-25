# gui.py
import tkinter as tk

class ReversiGUI:
    def __init__(self, board, game):
        # Inicializa la interfaz gráfica de usuario con el tablero y el juego
        self.board = board
        self.game = game
        self.window = tk.Tk()
        self.window.title("Reversi")

        # Crea un lienzo para representar el tablero
        self.canvas = tk.Canvas(self.window, width=50 * board.size, height=50 * board.size)
        self.canvas.pack()

        # Dibuja el tablero inicialmente
        self.draw_board()

        # Vincula el evento de clic del mouse a la función on_click
        self.canvas.bind("<Button-1>", self.on_click)

        # Agrega un botón para cerrar el juego
        quit_button = tk.Button(self.window, text="Cerrar Juego", command=self.quit_game)
        quit_button.pack()

        # Inicia el ciclo principal de la interfaz gráfica
        self.window.mainloop()

    def draw_board(self):
        # Dibuja el tablero en el lienzo
        for row in range(self.board.size):
            for col in range(self.board.size):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                if self.board.board[row][col] == 'X':
                    self.canvas.create_oval(x1, y1, x2, y2, fill="black")
                elif self.board.board[row][col] == 'O':
                    self.canvas.create_oval(x1, y1, x2, y2, fill="white")

    def on_click(self, event):
        # Maneja el evento de clic en el tablero
        col = event.x // 50
        row = event.y // 50
        self.game.make_move(row, col)  # Llama a la función para hacer un movimiento en la lógica del juego
        self.draw_board()  # Actualiza la representación gráfica del tablero

    def update_board(self):
        # Actualiza la representación gráfica del tablero
        self.canvas.delete("all")
        self.draw_board()

    def quit_game(self):
        # Cierra el juego y la ventana de la interfaz gráfica
        self.window.destroy()
