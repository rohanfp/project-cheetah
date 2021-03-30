from .rules import *


class Recommendation:
    def __init__(self):
        self.rule_names = ['UnusedIpRule', 'RecentlyUsedIpRule', 'RandomIpRule'].reverse()
        self.engine = None

    def create_engine(self):
        for rule_name in self.rule_names:
            next_rule = None
            module_name = rule_name.lower()
            class_name = rule_name
            rule = getattr(globals()[module_name], class_name)
            self.engine = rule.next_handler(next_rule)
            next_rule = rule
