# import json
# import pytest
# from source.cheetah import read_file, write_file, record_ip_status

# def mock_json_load(*args, **kwargs):
#     file_path = "mock_" + args[0].split("/")[-1]
#     file_data = json.load(open('tests/test_data/mock_status.json', 'r'))
#     return file_data


# def mock_json_dump(*args, **kwargs):
#     file_path = "mock_" + args[0].split("/")[-1]
#     file_data = json.load(open('tests/test_data/mock_status.json', 'r'))
#     return file_data


# def test_record_ip_status():
#     file_path = 'tests/test_data/mock_status.json'
#     mock_ip_address = "1.1.1.1"
#     mock_competitor_name = "Mockcompetitor"
#     record_ip_status(mock_ip_address, mock_competitor_name, file_path)
#     file_data = read_file(file_path)
#     assert mock_ip_address in file_data['IP']
#     assert mock_competitor_name in file_data

