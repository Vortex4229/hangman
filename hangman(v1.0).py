import random
import tkinter as tk


class gameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x700")
        self.root.title("Hangman")
        self.root.resizable(False, False)

        self.file = open("words.txt", "r")
        data = self.file.read()
        self.words = data.split("\n")

        self.win = False
        self.lose = False
        self.word_lines = None
        self.guesses = None
        self.word = None
        self.false_guess = None

        self.modeQuestion = None
        self.easy = None
        self.medium = None
        self.hard = None
        self.guesses_label = None
        self.letters = None
        self.question = None
        self.guess = None
        self.guess_button = None
        self.character_count = None
        self.return_button = None
        self.false_guesses = []
        self.false_guess_message = None
        self.win_label = None
        self.word_label = None
        self.guesses_left = None
        self.lose_label = None
        self.custom_or_random = None
        self.custom = None
        self.random = None

        self.title = tk.Label(self.root, text="Hangman", font=("Helvetica", 50))
        self.onePlayer = tk.Button(self.root, text="Play", font=("Helvetica", 40), borderwidth=4, relief="raised", command=self.modeSelect)
        self.version = tk.Label(self.root, text="v1.0", font=("Helvetica", 20))

        self.title.place(x=500, y=50, anchor=tk.N)
        self.onePlayer.place(x=500, y=200, anchor=tk.N)
        self.version.place(x=950, y=650, anchor=tk.N)

        self.root.mainloop()

    def modeSelect(self):
        self.onePlayer.destroy()
        self.title.destroy()
        self.version.destroy()

        self.modeQuestion = tk.Label(self.root, text="Select a mode:", font=("Helvetica", 50))
        self.easy = tk.Button(self.root, text="Easy", font=("Helvetica", 40), borderwidth=4, relief="raised", command=self.easy_set)
        self.medium = tk.Button(self.root, text="Medium", font=("Helvetica", 40), borderwidth=4, relief="raised", command=self.medium_set)
        self.hard = tk.Button(self.root, text="Hard", font=("Helvetica", 40), borderwidth=4, relief="raised", command=self.hard_set)

        self.modeQuestion.place(x=500, y=50, anchor=tk.N)
        self.easy.place(x=500, y=200, anchor=tk.N)
        self.medium.place(x=500, y=350, anchor=tk.N)
        self.hard.place(x=500, y=500, anchor=tk.N)

    def easy_set(self):
        self.modeQuestion.destroy()
        self.easy.destroy()
        self.medium.destroy()
        self.hard.destroy()

        self.word = random.choice(self.words)
        self.guesses = 10

        self.game()

    def medium_set(self):
        self.modeQuestion.destroy()
        self.easy.destroy()
        self.medium.destroy()
        self.hard.destroy()

        self.word = random.choice(self.words)
        self.guesses = 7

        self.game()

    def hard_set(self):
        self.modeQuestion.destroy()
        self.easy.destroy()
        self.medium.destroy()
        self.hard.destroy()

        self.word = random.choice(self.words)
        self.guesses = 5

        self.game()

    def game(self):
        self.word_lines = "_ " * len(self.word)

        self.guesses_label = tk.Label(self.root, text="Guesses left: " + str(self.guesses), font=("Helvetica", 20))
        self.letters = tk.Label(self.root, text=self.word_lines, font=("Helvetica", 50))
        self.question = tk.Label(self.root, text="Guess a letter, or guess the word:", font=("Helvetica", 20))
        self.guess = tk.Entry(self.root, font=("Helvetica", 20))
        self.guess_button = tk.Button(self.root, text="Guess", font=("Helvetica", 20), borderwidth=4, relief="raised", command=self.guess_check)
        self.character_count = tk.Label(self.root, text="Number of characters: " + str(len(self.word)), font=("Helvetica", 20))
        self.return_button = tk.Button(self.root, text="Return to Menu", font=("Helvetica", 20), borderwidth=4, relief="raised", command=self.return_to_menu)

        self.guesses_label.place(x=500, y=50, anchor=tk.N)
        self.question.place(x=500, y=150, anchor=tk.N)
        self.guess.place(x=500, y=200, anchor=tk.N)
        self.guess_button.place(x=500, y=250, anchor=tk.N)
        self.letters.place(x=500, y=350, anchor=tk.N)
        self.character_count.place(x=500, y=500, anchor=tk.N)
        self.return_button.place(x=150, y=600, anchor=tk.N)

    def guess_check(self):
        if len(self.guess.get()) == 1:
            if self.guess.get() in self.word:
                self.word_lines = self.word_lines.split(" ")
                for i in range(len(self.word)):
                    if self.word[i] == self.guess.get():
                        self.word_lines[i] = self.guess.get()
                self.word_lines = " ".join(self.word_lines)
                self.letters.config(text=self.word_lines)
                if self.word_lines.replace(" ", "") == self.word:
                    self.win_page()
            elif self.guess.get() in self.false_guesses:
                self.false_guess_message = tk.Label(self.root, text="You already guessed that letter!", font=("Helvetica", 20))
                self.false_guess_message.place(x=750, y=610, anchor=tk.N)
                self.root.after(2000, self.false_guess_message.destroy)
            else:
                self.guesses -= 1
                self.guesses_label.config(text="Guesses left: " + str(self.guesses))
                self.false_guesses.append(self.guess.get())
                if self.guesses == 0:
                    self.lose_page()
        elif len(self.guess.get()) > 1:
            if self.guess.get() == self.word:
                self.win_page()
            else:
                self.guesses -= 1
                self.guesses_label.config(text="Guesses left: " + str(self.guesses))
                if self.guesses == 0:
                    self.lose_page()
        else:
            return

    def win_page(self):
        self.win = True

        self.guesses_label.destroy()
        self.letters.destroy()
        self.question.destroy()
        self.guess.destroy()
        self.guess_button.destroy()
        self.character_count.destroy()
        self.return_button.destroy()

        self.win_label = tk.Label(self.root, text="You win!", font=("Helvetica", 50))
        self.word_label = tk.Label(self.root, text="The word was: " + self.word, font=("Helvetica", 25))
        self.guesses_left = tk.Label(self.root, text="Guesses left: " + str(self.guesses), font=("Helvetica", 25))
        self.return_button = tk.Button(self.root, text="Return to Menu", font=("Helvetica", 40), borderwidth=4, relief="raised", command=self.return_to_menu)

        self.win_label.place(x=500, y=50, anchor=tk.N)
        self.word_label.place(x=500, y=200, anchor=tk.N)
        self.guesses_left.place(x=500, y=300, anchor=tk.N)
        self.return_button.place(x=500, y=500, anchor=tk.N)

    def lose_page(self):
        self.lose = True

        self.guesses_label.destroy()
        self.letters.destroy()
        self.question.destroy()
        self.guess.destroy()
        self.guess_button.destroy()
        self.character_count.destroy()
        self.return_button.destroy()

        self.lose_label = tk.Label(self.root, text="You lose!", font=("Helvetica", 50))
        self.word_label = tk.Label(self.root, text="The word was: " + self.word, font=("Helvetica", 25))
        self.return_button = tk.Button(self.root, text="Return to Menu", font=("Helvetica", 40), borderwidth=4, relief="raised", command=self.return_to_menu)

        self.lose_label.place(x=500, y=50, anchor=tk.N)
        self.word_label.place(x=500, y=200, anchor=tk.N)
        self.return_button.place(x=500, y=500, anchor=tk.N)

    def return_to_menu(self):
        if self.win:
            self.win_label.destroy()
            self.word_label.destroy()
            self.guesses_left.destroy()
            self.return_button.destroy()
        elif self.lose and not self.win:
            self.lose_label.destroy()
            self.word_label.destroy()
            self.return_button.destroy()
        else:
            self.guesses_label.destroy()
            self.letters.destroy()
            self.question.destroy()
            self.guess.destroy()
            self.guess_button.destroy()
            self.character_count.destroy()
            self.return_button.destroy()

        # variables
        self.win = False
        self.lose = False
        self.word_lines = None
        self.guesses = None
        self.word = None

        self.title = tk.Label(self.root, text="Hangman", font=("Helvetica", 50))
        self.onePlayer = tk.Button(self.root, text="Play", font=("Helvetica", 40), borderwidth=4, relief="raised", command=self.modeSelect)
        self.version = tk.Label(self.root, text="v1.0", font=("Helvetica", 20))

        self.title.place(x=500, y=50, anchor=tk.N)
        self.onePlayer.place(x=500, y=200, anchor=tk.N)
        self.version.place(x=950, y=650, anchor=tk.N)


gameGUI()
