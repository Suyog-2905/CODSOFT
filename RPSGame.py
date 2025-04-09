import random
import tkinter as tk

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("300x300")
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label = tk.Label(self.window, text="User Score: 0")
        self.user_score_label.pack(pady=10)
        self.computer_score_label = tk.Label(self.window, text="Computer Score: 0")
        self.computer_score_label.pack(pady=10)
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack(pady=10)
        self.rock_button = tk.Button(self.window, text="Rock", command=self.rock)
        self.rock_button.pack(pady=5)
        self.paper_button = tk.Button(self.window, text="Paper", command=self.paper)
        self.paper_button.pack(pady=5)
        self.scissors_button = tk.Button(self.window, text="Scissors", command=self.scissors)
        self.scissors_button.pack(pady=5)
        self.reset_button = tk.Button(self.window, text="Play Again", command=self.reset)
        self.reset_button.pack(pady=10)

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        if (user_choice == "rock" and computer_choice == "scissors") or \
           (user_choice == "scissors" and computer_choice == "paper") or \
           (user_choice == "paper" and computer_choice == "rock"):
            return "User"
        return "Computer"

    def rock(self):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner("rock", computer_choice)
        self.update_score(winner)
        self.result_label.config(text=f"Computer chose {computer_choice}. {self.get_result_text(winner)}")
        self.check_game_over()

    def paper(self):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner("paper", computer_choice)
        self.update_score(winner)
        self.result_label.config(text=f"Computer chose {computer_choice}. {self.get_result_text(winner)}")
        self.check_game_over()

    def scissors(self):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner("scissors", computer_choice)
        self.update_score(winner)
        self.result_label.config(text=f"Computer chose {computer_choice}. {self.get_result_text(winner)}")
        self.check_game_over()

    def update_score(self, winner):
        if winner == "User":
            self.user_score += 1
            self.user_score_label.config(text=f"User Score: {self.user_score}")
        elif winner == "Computer":
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def get_result_text(self, winner):
        if winner == "Tie":
            return "It's a tie!"
        elif winner == "User":
            return "User wins this round!"
        else:
            return "Computer wins this round!"

    def check_game_over(self):
        if self.user_score == 3:
            self.result_label.config(text="User wins the game!")
            self.play_again()
        elif self.computer_score == 3:
            self.result_label.config(text="Computer wins the game!")
            self.play_again()

    def play_again(self):
        self.rock_button.config(state="disabled")
        self.paper_button.config(state="disabled")
        self.scissors_button.config(state="disabled")
        play_again_button = tk.Button(self.window, text="Play Again", command=self.reset)
        play_again_button.pack(pady=10)

    def reset(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="User Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")
        self.result_label.config(text="")
        self.rock_button.config(state="normal")
        self.paper_button.config(state="normal")
        self.scissors_button.config(state="normal")
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Button) and widget['text'] == 'Play Again':
                widget.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
