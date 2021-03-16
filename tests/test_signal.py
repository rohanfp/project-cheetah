from source.signal.signalsfactory import SignalsFactory

import os
import json
import pytest


@pytest.fixture
def _mock_env(monkeypatch):
    """Mock environment."""
    monkeypatch.setenv('DATABASE', './tests/test_data/mock_cheetah_status.json')


def test_init_signal(_mock_env):
    json.dump({}, open(os.getenv('DATABASE'), 'w'))
    mock_scraper_status = 'INIT,deliveroo,189.254.241.21'.split(',')
    init_signal = SignalsFactory().create_signal(*mock_scraper_status)
    init_signal.perform()
    mock_cheetah_status = json.load(open(os.getenv('DATABASE'), 'r'))
    assert 'deliveroo' in mock_cheetah_status
    assert 'queue' in mock_cheetah_status['deliveroo']
    assert 'queueWeights' in mock_cheetah_status['deliveroo']


def test_start_signal(_mock_env):
    mock_scraper_status = 'START,deliveroo,189.254.241.21'.split(',')
    end_signal = SignalsFactory().create_signal(*mock_scraper_status)
    end_signal.perform()
    mock_cheetah_status = json.load(open(os.getenv('DATABASE'), 'r'))
    assert 'deliveroo' in mock_cheetah_status
    assert 'scraperFeed' in mock_cheetah_status['deliveroo']
    assert '189.254.241.21' in mock_cheetah_status['deliveroo']['scraperFeed']
    assert 'startTime' in mock_cheetah_status['deliveroo']['scraperFeed']['189.254.241.21']


def test_end_signal(_mock_env):
    mock_scraper_status = 'END,deliveroo,189.254.241.21'.split(',')
    end_signal = SignalsFactory().create_signal(*mock_scraper_status)
    end_signal.perform()
    mock_cheetah_status = json.load(open(os.getenv('DATABASE'), 'r'))
    assert 'deliveroo' in mock_cheetah_status
    assert 'scraperFeed' in mock_cheetah_status['deliveroo']
    assert '189.254.241.21' in mock_cheetah_status['deliveroo']['scraperFeed']
    assert 'endTime' in mock_cheetah_status['deliveroo']['scraperFeed']['189.254.241.21']
    assert 'count' in mock_cheetah_status['deliveroo']['scraperFeed']['189.254.241.21']
