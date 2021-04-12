from source.translator.translatorsfactory import TranslatorsFactory

import json
import pytest


class TestTranslator:
    def test_translator_sqs(self):
        translator = TranslatorsFactory().create_translator(channel_name="sqs")
        message_0 = json.load(open('tests/test_data/mock_translator_data_sqs.json', 'r'))[0]
        message_1 = json.load(open('tests/test_data/mock_translator_data_sqs.json', 'r'))[1]
        translated_message_0 = translator.translate(message_0)
        translated_message_1 = translator.translate(message_1)
        assert set(translated_message_0) == {"signal_name", "ip_address", "scraper_type", "service_name", "time"}
        assert set(translated_message_1) == {"signal_name", "ip_address", "scraper_type", "service_name", "time"}

    def test_translator_sns(self):
        translator = TranslatorsFactory().create_translator(channel_name="sns")
        message = json.load(open('tests/test_data/mock_translator_data_sns.json', 'r'))
        translated_message = translator.translate(message)
        assert set(translated_message) == {"signal_name", "ip_address", "scraper_type", "service_name", "time"}
