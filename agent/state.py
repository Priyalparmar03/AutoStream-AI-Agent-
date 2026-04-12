# class AgentState:
#     def __init__(self):
#         self.name = None
#         self.email = None
#         self.platform = None
#         self.intent = None


class AgentState:
    def __init__(self):
        self.user_input = ""
        self.intent = ""
        self.response = ""
        self.name = None
        self.email = None
        self.platform = None