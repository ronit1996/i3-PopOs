#!/usr/bin/env bash

# Terminate already running bar instances
# If all your bars have ipc enabled, you can use 
polybar-msg cmd quit
# Otherwise you can use the nuclear option:
killall -q polybar

# Launch bar1 and bar2
 polybar -r center  2>&1 | tee -a /tmp/polybar2.log & disown
 polybar -r date  2>&1 | tee -a /tmp/polybar3.log & disown
 polybar -r right  2>&1 | tee -a /tmp/polybar4.log & disown
 polybar -r bottom  2>&1 | tee -a /tmp/polybar5.log & disown
 polybar -r top-weather  2>&1 | tee -a /tmp/polybar6.log & disown
 polybar -r time  2>&1 | tee -a /tmp/polybar7.log & disown
 # polybar -r window-bar  2>&1 | tee -a /tmp/polybar8.log & disown
echo "Bars launched..."
