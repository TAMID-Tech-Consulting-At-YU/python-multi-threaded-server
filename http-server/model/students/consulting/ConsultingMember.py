from model.Member import Member


class ConsultingMember(Member):

    def __init__(self, name, grad_year, major):
        super().__init__(name, grad_year, major)
        self.slide_decks = []

    def get_major(self):
        super().get_major()

    def get_name(self):
        super().get_name()

    def get_graduation_year(self):
        super().get_graduation_year()

    def add_slide_deck(self, slide_deck):
        self.slide_decks.append(slide_deck)

    def get_slide_deck(self):
        return self.slide_decks
