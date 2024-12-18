#!/bin/bash

killall ffmpeg

ffmpeg -i "rtsp://192.168.1.4:8554/720p" -acodec copy -vcodec copy /media/cameraG3_$(date +"%d-%m-%Y_%H-%M-%S").mp4
