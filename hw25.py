import string

class Alphabet:
    def __init__(self,lang,letters):
        self.lang = lang
        self.letters = letters

    def alph(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En',string.ascii_uppercase)
        self.__letters_num = 26

    def is_en_letter(self, letter):
        if letter in string.ascii_uppercase:
            return True
        else:
            return False

    def letters_num(self):
        print(self.__letters_num)

    @staticmethod
    def example():
        print('Hello, world!')

if __name__ == '__main__':
    ex = EngAlphabet()
    ex.alph()
    ex.letters_num()
    print(ex.is_en_letter('F'))
    print(ex.is_en_letter('Щ'))
    EngAlphabet.example()