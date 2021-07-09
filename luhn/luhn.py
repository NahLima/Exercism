class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if not self.card_num.isdigit():
            return False

        numbers = self.to_numbers()

        if len(numbers) <= 1:
            return False

        sum_numbers = sum([
            self.double(number) if pos % 2 != 0 else number
            for pos, number in enumerate(reversed(numbers))])

        return sum_numbers % 10 == 0

    def to_numbers(self):
        return list(map(int, self.card_num))

    def double(self, number):
        number *= 2

        if number > 9:
            number -= 9
            return number
        return number
