#!/bin/bash

sudo ./PythonRTC.py >/dev/time
val=`cat /dev/time`
date -s "$val"
