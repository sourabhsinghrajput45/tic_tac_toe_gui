import tkinter as tk
from tkinter import messagebox
from features.timer_feature import GameTimer
from features.scoreboard_feature import Scoreboard
from features.theme_feature import ThemeManager


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe 🎮")

        # ✅ Make window full screen
        self.root.attributes("-fullscreen", True)

        # (Optional) If you prefer a maximized but resizable window instead of true full screen:
        # self.root.state('zoomed')

        self.root.configure(bg="#1b1b2f")

        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # --- Title ---
        self.title_label = tk.Label(
            root, text="Tic Tac Toe", font=("Poppins", 26, "bold"),
            fg="#00ADB5", bg="#1b1b2f"
        )
        self.title_label.pack(pady=(15, 0))

        # --- Player Turn Label ---
        self.label = tk.Label(
            root, text=f"Player {self.current_player}'s Turn",
            font=("Poppins", 14, "bold"), fg="#EEEEEE", bg="#1b1b2f"
        )
        self.label.pack(pady=(5, 10))

        # --- Timer + Move Counter ---
        self.timer = GameTimer(root)
        self.timer.start(root)

        # --- Scoreboard ---
        self.scoreboard = Scoreboard(root)

        # --- Game Board Frame ---
        self.frame = tk.Frame(root, bg="#1b1b2f")
        self.frame.pack(pady=20)

        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.frame, text="", font=("Poppins", 24, "bold"),
                    width=6, height=2, bg="#393E46", fg="#EEEEEE",
                    activebackground="#00ADB5", activeforeground="#222831",
                    bd=0, relief="flat",
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                btn.grid(row=row, column=col, padx=10, pady=10)
                # Add hover effect
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#00ADB5"))
                btn.bind("<Leave>", lambda e, b=btn:
                         b.config(bg="#393E46") if b["state"] == "normal" and b["text"] == "" else None)
                self.buttons[row][col] = btn

        # --- Restart Button ---
        self.reset_button = tk.Button(
            root, text="Restart Game", font=("Poppins", 13, "bold"),
            bg="#00ADB5", fg="#1b1b2f", relief="flat",
            width=18, height=2, command=self.reset_board
        )
        self.reset_button.pack(pady=20)

        # --- Theme Button ---
        self.theme_button = tk.Button(
            root, text="Change Theme 🎨", font=("Poppins", 12, "bold"),
            bg="#00ADB5", fg="#1b1b2f", relief="flat",
            width=15, height=1, command=self.toggle_theme
        )
        self.theme_button.pack(pady=(0, 10))

        # --- Footer ---
        self.footer_label = tk.Label(
            root, text="Made with ❤️ by Sourabh",
            font=("Poppins", 10), fg="#888", bg="#1b1b2f"
        )
        self.footer_label.pack(pady=(10, 10))

        # --- Theme Manager ---
        self.theme_manager = ThemeManager(self)
        self.theme_manager.apply_theme("dark")

        # --- Add Esc key to exit fullscreen ---
        self.root.bind("<Escape>", self.exit_fullscreen)

    # --- Exit fullscreen when pressing Esc ---
    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)

    # --- Button Click Logic ---
    def on_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            self.timer.increment_move()

            button["text"] = self.current_player
            button["fg"] = "#FFD369" if self.current_player == "X" else "#FF2E63"

            if self.check_winner():
                self.timer.stop()
                self.highlight_winner()
                self.scoreboard.update_score(self.current_player)
                self.show_popup(f"🏆 Player {self.current_player} Wins!")

            elif self.is_draw():
                self.timer.stop()
                self.scoreboard.update_score("draw")
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
        self.timer.reset()
        self.timer.start(self.root)

    def toggle_theme(self):
        self.theme_manager.toggle_theme()

    def show_popup(self, message):
        popup = tk.Toplevel(self.root)
        popup.title("Game Over")
        popup.geometry("300x180")
        popup.configure(bg="#1b1b2f")
        popup.resizable(False, False)
        tk.Label(popup, text=message, font=("Poppins", 15, "bold"),
                 fg="#00ADB5", bg="#1b1b2f").pack(pady=25)
        tk.Button(popup, text="Play Again", bg="#00ADB5", fg="#1b1b2f",
                  font=("Poppins", 12, "bold"), width=14, relief="flat",
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
