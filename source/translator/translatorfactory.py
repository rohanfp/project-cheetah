from .translators import *


class TranslatorFactory:
    @staticmethod
    def create_translator(channel_name):
        module_name = f'{channel_name.lower()}translator'
        class_name = f'{channel_name.title()}Translator'
        return getattr(globals()[module_name], class_name)(channel_name)
