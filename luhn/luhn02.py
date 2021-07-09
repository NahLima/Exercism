class Luhn:
    def __init__(self, card_num):
        nums = []  # lista vazia

        for n in card_num:  # confirma se é um número
            if n.isdigit():
                nums.append(int(n))
            elif n != ' ':
                self.n_valid = False
                return

        if len(nums) < 2:
            self.n_valid = False
            return

        num_sum = 0
# pega a partir do segundo número da esquerda para a direita e faz o calculo
        for item in nums[-2::-2]:
            item *= 2
            if item > 9:
                item -= 9
            num_sum += item

        for item in nums[-1::-2]:  # pega os outros numeros
            num_sum += item

        if not num_sum % 10:  # pega os numeros e divide por 10
            self.n_valid = True
        else:
            self.n_valid = False

    def valid(self):
        return self.n_valid
