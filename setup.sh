#!/usr/bin/env bash

# Add Python repository
add-apt-repository -y ppa:jonathonf/python-3.6
# Install Python 3
apt-get update && apt-get install -y python3.6 python3-pip python3-venv
python3.6 -m venv env --without-pip

# Install Coind
pip3 install coind