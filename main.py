from tic_tac_toe import TicTacToe
import tkinter as tk

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
