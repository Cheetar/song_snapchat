#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn song_snapchat.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 3
