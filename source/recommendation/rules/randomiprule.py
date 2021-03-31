from .rule import Rule


from random import choices


class RandomIpRule(Rule):
    def handler(self, data=None):
        weights = [len(data['result']) - i for i in range(len(data['result']))]
        data['result'] = choices(data['result'], weights=weights, k=1)
        return super().handler(data)
