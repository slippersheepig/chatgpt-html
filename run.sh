#!/bin/bash
Xvfb $DISPLAY -screen $DISPLAY 640x480x8 &
gunicorn -b 0.0.0.0:80 main:server --timeout 200 --worker-class gevent
