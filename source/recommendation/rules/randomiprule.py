from .rule import Rule

from random import choice


class RandomIpRule(Rule):
    def handler(self, data=None):
        data['result'] = choice(data['result'])
        super().handler(data)
