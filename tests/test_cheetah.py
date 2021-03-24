from source.cheetah import translate_message

import json
import pytest


@pytest.fixture
def mock_env_1(monkeypatch):
    monkeypatch.setenv("CHANNEL_NAME", "SQS")


@pytest.fixture
def mock_env_2(monkeypatch):
    monkeypatch.setenv("CHANNEL_NAME", "SNS")


class TestTranslateMessage:
    def test_translator_sqs(self, mock_env_1):
        event_0 = json.load(open('tests/test_data/mock_event_data_sqs.json', 'r'))[0]
        event_1 = json.load(open('tests/test_data/mock_event_data_sqs.json', 'r'))[1]
        context = {}
        translated_message_0 = translate_message(event_0, context)
        translated_message_1 = translate_message(event_1, context)
        assert set(translated_message_0) == {"signal_name", "ip_address", "scraper_type", "service_name", "time"}
        assert set(translated_message_1) == {"signal_name", "ip_address", "scraper_type", "service_name", "time"}

    def test_translator_sns(self, mock_env_2):
        event = json.load(open('tests/test_data/mock_event_data_sns.json', 'r'))
        context = {}
        translated_message = translate_message(event, context)
        assert set(translated_message) == {"signal_name", "ip_address", "scraper_type", "service_name", "time"}
