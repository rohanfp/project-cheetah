from source.signal.signalsfactory import SignalsFactory

import os
import re
import json
import pytest


@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv('DATABASE', './tests/test_data/database.json')


class TestSignal:
    def test_database(self, mock_env):
        database = {
            'ip_level_status': {},
            'service_level_status': {}
        }
        json.dump(database, open(os.getenv('DATABASE'), 'w'), indent=4)
        assert True


    def test_init_signal(self, mock_env):
        signal_data = json.load(open('tests/test_data/mock_signal_data_init.json', 'r'))
        signal = SignalsFactory().create_signal(signal_name='INIT')
        signal.perform(**signal_data)
        database = json.load(open(os.getenv('DATABASE', 'r')))['ip_level_status']
        assert 'A' in database
        assert '127.0.0.1' in database['A']


    def test_start_signal(self, mock_env):
        signal_data = json.load(open('tests/test_data/mock_signal_data_start.json', 'r'))
        signal = SignalsFactory().create_signal(signal_name='START')
        signal.perform(**signal_data)
        database = json.load(open(os.getenv('DATABASE', 'r')))['service_level_status']
        assert '127.0.0.1' in database['A']['grab']
        assert 'start_timestamp' in database['A']['grab']['127.0.0.1']
        assert re.match(r"\d+\.\d+", database['A']['grab']['127.0.0.1']['start_timestamp'])


    def test_end_signal(self, mock_env):
        signal_data = json.load(open('tests/test_data/mock_signal_data_end.json', 'r'))
        signal = SignalsFactory().create_signal(signal_name='END')
        signal.perform(**signal_data)
        database = json.load(open(os.getenv('DATABASE', 'r')))['service_level_status']
        assert re.match(r"\d+\.\d+", database['A']['grab']['127.0.0.1']['end_timestamp'])
        assert database['A']['grab']['127.0.0.1']['execution_count'] == 1
