import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe 🎮")
        self.root.geometry("340x400")
        self.root.configure(bg="#1b1b2f")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # --- Title & status label ---
        self.title_label = tk.Label(
            root, text="Tic Tac Toe", font=("Poppins", 20, "bold"),
            fg="#00ADB5", bg="#1b1b2f"
        )
        self.title_label.pack(pady=(10, 0))

        self.label = tk.Label(
            root, text=f"Player {self.current_player}'s Turn",
            font=("Poppins", 14, "bold"), fg="#EEEEEE", bg="#1b1b2f"
        )
        self.label.pack(pady=(5, 15))

        # --- Main frame ---
        self.frame = tk.Frame(root, bg="#1b1b2f")
        self.frame.pack()

        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.frame, text="", font=("Poppins", 22, "bold"),
                    width=5, height=2, bg="#393E46", fg="#EEEEEE",
                    activebackground="#00ADB5", activeforeground="#222831",
                    bd=0, relief="flat",
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                btn.grid(row=row, column=col, padx=5, pady=5)
                # Add hover effect
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#00ADB5"))
                btn.bind("<Leave>", lambda e, b=btn:
                         b.config(bg="#393E46") if b["state"] == "normal" and b["text"] == "" else None)
                self.buttons[row][col] = btn

        # --- Restart button ---
        self.reset_button = tk.Button(
            root, text="Restart Game", font=("Poppins", 12, "bold"),
            bg="#00ADB5", fg="#1b1b2f", relief="flat",
            width=15, height=1, command=self.reset_board
        )
        self.reset_button.pack(pady=15)

        # --- Footer ---
        tk.Label(root, text="Made with ❤️ by Sourabh",
                 font=("Poppins", 9), fg="#555", bg="#1b1b2f").pack(pady=(0, 5))

    # --- Button Click Logic ---
    def on_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = self.current_player
            button["fg"] = "#FFD369" if self.current_player == "X" else "#FF2E63"
            if self.check_winner():
                self.highlight_winner()
                self.show_popup(f"🏆 Player {self.current_player} Wins!")
            elif self.is_draw():
                self.show_popup("😐 It's a Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Player {self.current_player}'s Turn")

    # --- Winner Check ---
    def check_winner(self):
        b = self.buttons
        for i in range(3):
            if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] != "":
                self.winning_cells = [(i, 0), (i, 1), (i, 2)]
                return True
            if b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] != "":
                self.winning_cells = [(0, i), (1, i), (2, i)]
                return True
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != "":
            self.winning_cells = [(0, 0), (1, 1), (2, 2)]
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != "":
            self.winning_cells = [(0, 2), (1, 1), (2, 0)]
            return True
        return False

    def is_draw(self):
        return all(button["text"] != "" for row in self.buttons for button in row)

    # --- UI Enhancements ---
    def highlight_winner(self):
        for (r, c) in self.winning_cells:
            self.buttons[r][c].config(bg="#32E0C4", fg="#222831")
        self.disable_buttons()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def reset_board(self):
        self.current_player = "X"
        self.label.config(text=f"Player {self.current_player}'s Turn")
        for row in self.buttons:
            for button in row:
                button.config(text="", state="normal", bg="#393E46", fg="#EEEEEE")

    # --- Custom Popup Window ---
    def show_popup(self, message):
        popup = tk.Toplevel(self.root)
        popup.title("Game Over")
        popup.geometry("250x150")
        popup.configure(bg="#1b1b2f")
        popup.resizable(False, False)
        tk.Label(popup, text=message, font=("Poppins", 14, "bold"),
                 fg="#00ADB5", bg="#1b1b2f").pack(pady=20)
        tk.Button(popup, text="Play Again", bg="#00ADB5", fg="#1b1b2f",
                  font=("Poppins", 11, "bold"), width=12, relief="flat",
                  command=lambda: [self.reset_board(), popup.destroy()]).pack(pady=10)
        popup.transient(self.root)
        popup.grab_set()
        popup.wait_window()

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
