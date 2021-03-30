class Rule:
    def __init__(self):
        self.next_handler = None

    def set_next(self, rule):
        self.next_handler = rule

    def handler(self, data=None):
        if self.next_handler:
            return self.next_handler.handler(data)
        else:
            return data
