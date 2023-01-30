from model.Member import Member


class TechMember(Member):

    def __init__(self, name, grad_year, major):
        super().__init__(name, grad_year, major)
        self.tech_tools = []

    def get_major(self):
        super().get_major()

    def get_name(self):
        super().get_name()

    def get_graduation_year(self):
        super().get_graduation_year()

    def add_tech_tool(self, tool):
        self.tech_tools.append(tool)

    def get_tech_tools(self):
        return self.tech_tools
