#!/bin/bash
virtualenv .
source bin/activate
pip install -r requirements.txt
buildout bootstrap
sudo npm i grunt-cli -g
