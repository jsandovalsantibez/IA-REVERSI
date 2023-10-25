#Integrantes#
#Diego Pizarro   19.639.215-7  nrc:6909
#Diego Troncoso  20.462.209-8  nrc:6908
#Matías Riveros  20.676.480-5  nrc:6908
#Jorge Sandoval  20.214.231-1  nrc:6908

import tkinter as tk
from board import Board
from gui import ReversiGUI
from gameLogic import ReversiGame


def choose_board_size():
    # Función para mostrar un diálogo y elegir el tamaño del tablero
    dialog = tk.Tk()
    dialog.title("Elegir Tamaño de Tablero")

    label = tk.Label(dialog, text="Elige el tamaño del tablero:")
    label.pack()

    def set_board_size(size):
        dialog.destroy()
        if size == 10:
            dificil()  # Llama a la función "dificil" cuando el tamaño es 10x10
        else:
            start_game(size)

    button_6x6 = tk.Button(dialog, text="6x6", command=lambda: set_board_size(6))
    button_6x6.pack()

    button_8x8 = tk.Button(dialog, text="8x8", command=lambda: set_board_size(8))
    button_8x8.pack()

    button_10x10 = tk.Button(dialog, text="10x10", command=lambda: set_board_size(10))
    button_10x10.pack()

    dialog.mainloop()

def start_game(board_size):
    # Inicia el juego con el tamaño de tablero especificado
    board = Board(board_size)
    game = ReversiGame(board)
    game.initialize_game()

    gui = ReversiGUI(board, game)

def dificil():
    # Función para iniciar el juego en modo "dificil" (10x10)
    board_size = 10
    board = Board(board_size)
    game = ReversiGame(board)
    game.initialize_game()
    gui = ReversiGUI(board, game)

if __name__ == "__main__":
    choose_board_size()
