from source.cheetah import cheetah

import os
import json
import pytest
import time


@pytest.fixture
def _mock_env(monkeypatch):
    """Mock environment."""
    monkeypatch.setenv('DATABASE', './tests/test_data/mock_cheetah_status.json')


def test_cheetah(_mock_env):
    json.dump({}, open(os.getenv('DATABASE'), 'w'))
    mock_scraper_status = [
        'INIT,deliveroo,189.254.241.21',
        'START,deliveroo,189.254.241.21',
        'END,deliveroo,189.254.241.21'
    ]
    response = {}
    for i in range(len(mock_scraper_status)):
        signal_name, service_name, ip_address = mock_scraper_status[i].split(',')
        response[signal_name] = cheetah(signal_name, service_name, ip_address)
    assert 'recommended_ip_address' in response['END']['data']
