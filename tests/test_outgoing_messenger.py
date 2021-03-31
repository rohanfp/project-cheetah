from source.outgoingmessenger.messenger import translate_message

import os
import re
import json
import pytest


@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv("CHANNEL_NAME", "SNS")


class TestOutgoingMessenger:
    def test_translate_message(self, mock_env):
        event = json.load(open('tests/test_data/mock_outgoing_messenger_data.json', 'r'))
        context = {}
        translate_message(event, context)
        assert True
