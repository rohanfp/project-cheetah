from source.signal.signalsfactory import SignalsFactory

import os
import re
import json
import pytest
import boto3
from boto3.dynamodb.conditions import Key
from moto import mock_dynamodb2


@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv('AWS_PROFILE', 'dev')
    monkeypatch.setenv('AWS_DEFAULT_REGION', 'ap-southeast-1')


@pytest.fixture(scope="class")
def mock_dynamodb():
    mock = mock_dynamodb2()
    mock.start()
    dynamodb = boto3.resource("dynamodb")
    dynamodb.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "scraper_type",
                "AttributeType": "S"
            },
            {
                "AttributeName": "ip_address",
                "AttributeType": "S"
            }
        ],
        TableName="ip-level-status",
        KeySchema=[
            {
                "KeyType": "HASH",
                "AttributeName": "scraper_type"
            },
            {
                "KeyType": "RANGE",
                "AttributeName": "ip_address"
            }
        ],
        BillingMode="PAY_PER_REQUEST"
    )
    dynamodb.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "scraper_type",
                "AttributeType": "S"
            },
            {
                "AttributeName": "service_name",
                "AttributeType": "S"
            }
        ],
        TableName="service-level-status",
        KeySchema=[
            {
                "KeyType": "HASH",
                "AttributeName": "scraper_type"
            },
            {
                "KeyType": "RANGE",
                "AttributeName": "service_name"
            }
        ],
        BillingMode="PAY_PER_REQUEST"
    )
    yield dynamodb
    mock.stop()


class TestSignal:
    def test_init_signal(self, mock_dynamodb, mock_env):
        signal_data = json.load(open('tests/test_data/mock_signal_data_init.json', 'r'))
        signal = SignalsFactory().create_signal(signal_name='INIT')
        signal.perform(**signal_data)
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ip-level-status')
        status_data = table.query(
            KeyConditionExpression=(Key('scraper_type').eq('A') & Key('ip_address').eq('127.0.0.1'))
        )
        assert bool(status_data)


    def test_start_signal(self, mock_dynamodb, mock_env):
        signal_data = json.load(open('tests/test_data/mock_signal_data_start.json', 'r'))
        signal = SignalsFactory().create_signal(signal_name='START')
        signal.perform(**signal_data)
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ip-level-status')
        ip_level_status_data = table.query(
            KeyConditionExpression=Key('scraper_type').eq('A') & Key('ip_address').eq('127.0.0.1')
        )['Items'][0]
        table = dynamodb.Table('service-level-status')
        service_level_status_data = table.query(
            KeyConditionExpression=Key('scraper_type').eq('A') & Key('service_name').eq('grab')
        )['Items'][0]
        assert 'grab' in ip_level_status_data['to_restrict_list']
        assert re.match(r'\d+\.\d+', service_level_status_data['latest_start_timestamp'])


    def test_end_signal(self, mock_dynamodb, mock_env):
        signal_data = json.load(open('tests/test_data/mock_signal_data_end.json', 'r'))
        signal = SignalsFactory().create_signal(signal_name='END')
        signal.perform(**signal_data)
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('service-level-status')
        service_level_status_data = table.query(
            KeyConditionExpression=Key('scraper_type').eq('A') & Key('service_name').eq('grab')
        )['Items'][0]
        assert re.match(r'\d+\.\d+', service_level_status_data['latest_end_timestamp'])
