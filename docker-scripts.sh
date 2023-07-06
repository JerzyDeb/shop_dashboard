#!/bin/bash

apt-get update
apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 libjpeg-dev \
 libopenjp2-7-dev libffi-dev libpango1.0-dev libcairo2 \
 libharfbuzz0b libopenjp2-7-dev libsdl-pango-dev libxml2-dev libxslt-dev \
 libffi-dev libcairo2-dev
rm -rf /var/lib/apt/lists/*

