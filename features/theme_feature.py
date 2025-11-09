class ThemeManager:
    """Handles theme switching for the Tic Tac Toe UI."""

    THEMES = {
        "dark": {
            "bg": "#1b1b2f",
            "fg": "#EEEEEE",
            "accent": "#00ADB5",
            "button_bg": "#393E46",
            "button_fg": "#EEEEEE",
            "highlight": "#32E0C4",
            "x_color": "#FFD369",
            "o_color": "#FF2E63"
        },
        "light": {
            "bg": "#F4F4F4",
            "fg": "#222831",
            "accent": "#00ADB5",
            "button_bg": "#E0E0E0",
            "button_fg": "#222831",
            "highlight": "#00ADB5",
            "x_color": "#FF9800",
            "o_color": "#E91E63"
        },
        "retro": {
            "bg": "#2D2D2D",
            "fg": "#FFD700",
            "accent": "#FF9800",
            "button_bg": "#333333",
            "button_fg": "#FFD700",
            "highlight": "#00FF7F",
            "x_color": "#FFA500",
            "o_color": "#00FF7F"
        }
    }

    def __init__(self, game_instance):
        self.game = game_instance
        self.current_theme = "dark"

    def toggle_theme(self):
        """Cycle through available themes."""
        themes = list(self.THEMES.keys())
        current_index = themes.index(self.current_theme)
        next_theme = themes[(current_index + 1) % len(themes)]
        self.apply_theme(next_theme)

    def apply_theme(self, theme_name):
        """Apply a theme to all game widgets."""
        self.current_theme = theme_name
        theme = self.THEMES[theme_name]
        g = self.game

        # Root background
        g.root.configure(bg=theme["bg"])

        # Labels
        g.title_label.config(bg=theme["bg"], fg=theme["accent"])
        g.label.config(bg=theme["bg"], fg=theme["fg"])

        # Timer & Scoreboard labels
        if hasattr(g, "timer"):
            g.timer.timer_label.config(bg=theme["bg"], fg=theme["fg"])
            g.timer.move_label.config(bg=theme["bg"], fg=theme["fg"])
        if hasattr(g, "scoreboard"):
            g.scoreboard.frame.config(bg=theme["bg"])
            for widget in g.scoreboard.frame.winfo_children():
                widget.config(bg=theme["bg"], fg=theme["fg"])

        # Buttons (Grid)
        for row in g.buttons:
            for btn in row:
                btn.config(
                    bg=theme["button_bg"], fg=theme["button_fg"],
                    activebackground=theme["accent"], activeforeground=theme["bg"]
                )

        # Reset Button
        g.reset_button.config(bg=theme["accent"], fg=theme["bg"])

        # Footer
        g.footer_label.config(bg=theme["bg"], fg=theme["fg"])
