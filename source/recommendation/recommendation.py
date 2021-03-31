from .rules import *


class Recommendation:
    def __init__(self):
        self.rule_names = ['UnusedIpRule', 'RecentlyUsedIpRule', 'RandomIpRule']
        self.engine = None


    def create_engine(self):
        for rule_name in self.rule_names:
            module_name = rule_name.lower()
            class_name = rule_name
            next_rule = getattr(globals()[module_name], class_name)()
            if not self.engine:
                self.engine = next_rule
            else:
                rule.set_next(next_rule)
            rule = next_rule
