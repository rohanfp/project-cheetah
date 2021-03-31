from ..translator.translatorsfactory import TranslatorsFactory

import os


def translate_message(event, context):
    # Universal message format translator to keep cheetah aws service agnostic
    translator = TranslatorsFactory().create_translator(channel_name=os.getenv("CHANNEL_NAME"))
    translated_message = translator.translate(event)
    outgoing_messenger(**translated_message)
    return translated_message


def outgoing_messenger(*args, **kwargs):
    # Outgoing message forwarder
    pass