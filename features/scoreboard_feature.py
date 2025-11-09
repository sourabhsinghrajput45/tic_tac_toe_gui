import tkinter as tk

class Scoreboard:
    """Handles tracking and displaying player scores."""

    def __init__(self, parent_frame):
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0

        # Frame for scoreboard
        self.frame = tk.Frame(parent_frame, bg="#1b1b2f")
        self.frame.pack(pady=(0, 5))

        # Labels for scores
        self.x_label = tk.Label(self.frame, text="X Wins: 0", font=("Poppins", 11, "bold"),
                                fg="#FFD369", bg="#1b1b2f", width=10)
        self.o_label = tk.Label(self.frame, text="O Wins: 0", font=("Poppins", 11, "bold"),
                                fg="#FF2E63", bg="#1b1b2f", width=10)
        self.draw_label = tk.Label(self.frame, text="Draws: 0", font=("Poppins", 11, "bold"),
                                   fg="#00ADB5", bg="#1b1b2f", width=10)

        self.x_label.grid(row=0, column=0, padx=3)
        self.o_label.grid(row=0, column=1, padx=3)
        self.draw_label.grid(row=0, column=2, padx=3)

        # Reset button
        self.reset_button = tk.Button(
            self.frame, text="Reset Scores", font=("Poppins", 9, "bold"),
            bg="#00ADB5", fg="#1b1b2f", relief="flat", width=12, height=1,
            command=self.reset_scores
        )
        self.reset_button.grid(row=1, column=0, columnspan=3, pady=(5, 0))

    def update_score(self, winner):
        """Update scoreboard based on winner."""
        if winner == "X":
            self.x_wins += 1
        elif winner == "O":
            self.o_wins += 1
        elif winner == "draw":
            self.draws += 1
        self.refresh_labels()

    def reset_scores(self):
        """Reset all scores to 0."""
        self.x_wins = self.o_wins = self.draws = 0
        self.refresh_labels()

    def refresh_labels(self):
        """Update label text to reflect current scores."""
        self.x_label.config(text=f"X Wins: {self.x_wins}")
        self.o_label.config(text=f"O Wins: {self.o_wins}")
        self.draw_label.config(text=f"Draws: {self.draws}")
