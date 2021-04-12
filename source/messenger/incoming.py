from ..translator.translatorsfactory import TranslatorsFactory

import os


def translate_message(event, context):
    # Universal message format translator to keep cheetah aws service agnostic
    translator = TranslatorsFactory().create_translator(channel_name=os.getenv("CHANNEL_NAME"))
    translated_message = translator.translate(event)
    incoming_messenger(**translated_message)
    return translated_message


def incoming_messenger(signal_name, ip_address, scraper_type, service_name=None, time=None):
    # Incoming message forwarder
    pass
