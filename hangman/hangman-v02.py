# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.letters = set(word)
        self.guessed_letters = []
        self.word = word

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Game over")
        if char not in self.letters or char in self.guessed_letters:
            self.remaining_guesses -= 1
        else:
            if char in self.letters:
                self.guessed_letters.append(char)

        if len(self.letters) == len(self.guessed_letters):
            self.status = STATUS_WIN
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_status(self):
        return self.status

    def get_masked_word(self):
        masked_word = []
        for letter in self.word:
            if letter in self.guessed_letters:
                masked_word.append(letter)
            else:
                masked_word.append("_")
        return "".join(masked_word)
