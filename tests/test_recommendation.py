from source.signal.signalsfactory import SignalsFactory

import os
import re
import json
import pytest
from source.recommendation.rules.unusediprule import UnusedIpRule
from source.recommendation.rules.recentlyusediprule import RecentlyUsedIpRule
from source.recommendation.rules.randomiprule import RandomIpRule
from source.recommendation.recommendation import Recommendation


class TestRecommendation:
    def test_unused_ip_rule(self):
        data = json.load(open('tests/test_data/mock_recommendation_data_unused.json', 'r'))
        unused_ip_rule = UnusedIpRule()
        data = unused_ip_rule.handler(data)
        assert set(data['result']) == set(['192.128.0.0', '127.0.0.0'])


    def test_recently_used_ip_rule(self):
        data = json.load(open('tests/test_data/mock_recommendation_data_recently.json', 'r'))
        recently_used_ip_rule = RecentlyUsedIpRule()
        data = recently_used_ip_rule.handler(data)
        assert data['result'] == ['192.128.0.0', '127.0.0.0']

    
    def test_recently_used_ip_rule(self):
        data = json.load(open('tests/test_data/mock_recommendation_data_random.json', 'r'))
        random_ip_rule = RandomIpRule()
        data = random_ip_rule.handler(data)
        assert len(data['result']) == 1


    def test_receommendation_engine(self):
        data = json.load(open('tests/test_data/mock_recommendation_data_unused.json', 'r'))
        recommendation = Recommendation()
        recommendation.create_engine()
        data = recommendation.engine.handler(data)
        assert len(data['result']) == 1
