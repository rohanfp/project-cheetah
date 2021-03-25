from .signals import *


class SignalsFactory:
    @staticmethod
    def create_signal(signal_name):
        module_name = f'{signal_name.lower()}signal'
        class_name = f'{signal_name.title()}Signal'
        return getattr(globals()[module_name], class_name)(signal_name)
