#!/bin/sh

# This script displays battery icon according to the charge level and charging state

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/purpleleaf/pmt2e
# Icon by @edskeye

# Dependencies: `wireless_tools`
# Arguments: [-N] ("Wi-Fi: " instead of icon) | [-M'custom name']

name="none"

wifi=$(iwgetid | awk -F '"' '{ print $2 }')
if [[ ! -z "$wifi" ]]; then
    name="$wifi"
fi

if [[ $1 == -N* ]]; then
    echo "Wi-Fi: $name"
elif [[ $1 == -M* ]]; then
    echo -e "$(echo $1 | cut -c3-) \n$name"
else
    echo /usr/share/pmt2e/icons/network.svg
    echo ${name}
fi

