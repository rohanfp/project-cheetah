#!/bin/bash
mkdir data
python source/generator.py 'data/scraper_status.json' 5000
python source/simulator.py 'data/scraper_status.json' 'data/cheetah_status.json'

