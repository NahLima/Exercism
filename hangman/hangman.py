# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.size = len(word)
        self.masked_word = ['_'] * self.size

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Game over") 
        if char not in self.word or char in self.masked_word: 
            self.remaining_guesses -= 1
        else:
            for letter in range(0, self.size):
                if char == self.word[letter]:
                    self.masked_word[letter] = char
        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return "".join(self.masked_word)

    def get_status(self):
        return self.status
