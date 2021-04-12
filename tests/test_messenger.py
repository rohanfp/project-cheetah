from source.messenger import incoming, outgoing

import os
import re
import json
import pytest


@pytest.fixture
def mock_env_1(monkeypatch):
    monkeypatch.setenv("CHANNEL_NAME", "SQS")


@pytest.fixture
def mock_env_2(monkeypatch):
    monkeypatch.setenv("CHANNEL_NAME", "SNS")


class TestMessenger:
    def test_messenger_incoming(self, mock_env_1):
        event = json.load(open('tests/test_data/mock_incoming_messenger.json', 'r'))[0]
        context = {}
        incoming.translate_message(event, context)
        assert True


    def test_messenger_outgoing(self, mock_env_2):
        event = json.load(open('tests/test_data/mock_outgoing_messenger.json', 'r'))
        context = {}
        outgoing.translate_message(event, context)
        assert True
