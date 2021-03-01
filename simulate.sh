#!/bin/bash
python source/generator.py 1000
python source/simulator.py 'data/scraper_status.json' 'data/cheetah_status_OFF.json' 'OFF'
echo "Delaying simulator by $1 seconds..."
sleep $1
python source/simulator.py 'data/scraper_status.json' 'data/cheetah_status_ON.json' 'ON'
python source/plot.py 'Grab'
