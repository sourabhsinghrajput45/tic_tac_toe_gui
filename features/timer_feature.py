import tkinter as tk
import time

class GameTimer:
    """Handles game timer and move counter logic."""
    
    def __init__(self, parent_frame):
        self.start_time = None
        self.running = False
        self.move_count = 0
        
        # Create labels
        self.timer_label = tk.Label(
            parent_frame, text="Time: 00:00", font=("Poppins", 12),
            fg="#EEEEEE", bg="#1b1b2f"
        )
        self.timer_label.pack(pady=(0, 2))

        self.move_label = tk.Label(
            parent_frame, text="Moves: 0", font=("Poppins", 12),
            fg="#EEEEEE", bg="#1b1b2f"
        )
        self.move_label.pack(pady=(0, 10))

    def start(self, root):
        """Start or restart the timer."""
        self.start_time = time.time()
        self.running = True
        self.update_timer(root)

    def update_timer(self, root):
        """Update the timer every second."""
        if self.running:
            elapsed = int(time.time() - self.start_time)
            minutes, seconds = divmod(elapsed, 60)
            self.timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
            root.after(1000, lambda: self.update_timer(root))

    def stop(self):
        """Pause the timer."""
        self.running = False

    def reset(self):
        """Reset timer and moves."""
        self.running = False
        self.start_time = None
        self.move_count = 0
        self.timer_label.config(text="Time: 00:00")
        self.move_label.config(text="Moves: 0")

    def increment_move(self):
        """Increment move count and update label."""
        self.move_count += 1
        self.move_label.config(text=f"Moves: {self.move_count}")
