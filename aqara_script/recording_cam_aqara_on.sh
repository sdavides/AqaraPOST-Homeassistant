#!/bin/bash

killall -9 ffmpeg

ffmpeg -i "rtsp://192.168.1.4:8554/720p" -acodec copy -vcodec copy /media/modem_$(date +"%d-%m-%Y_%H-%M-%S").mp4