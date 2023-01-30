from model.Member import Member


class FundMember(Member):

    def __init__(self, name, grad_year, major):
        super().__init__(name, grad_year, major)
        self.excel_workbooks = []

    def get_major(self):
        super().get_major()

    def get_name(self):
        super().get_name()

    def get_graduation_year(self):
        super().get_graduation_year()

    def add_slide_deck(self, workbook):
        self.excel_workbooks.append(workbook)

    def get_slide_deck(self):
        return self.excel_workbooks
