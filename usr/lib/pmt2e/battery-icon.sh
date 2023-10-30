#!/bin/sh

# This script displays battery icon according to the charge level and charging state

# Author: Piotr Miller <nwg.piotr@gmail.com>
# Author: purpleleaf <max@ganoia.eu>
# Website: http://nwg.pl
# Project: https://github.com/purpleleaf/pmt2e
# License: GPL3

# Dependencies: `acpi`
# argument: [-l] - append textual volume level

bat=$(acpi -b)

if [[ $bat ]]; then
    state=$(echo ${bat} | awk '{print $3}')

    if [[ "$state" = "Not" ]]; then
        level=$(echo ${bat} | awk '{print $5}')
        level=${level::-1}

    else
        level=$(echo ${bat} | awk '{print $4}')
        if [[ "$state" == *"Unknown"* ]]; then
            level=${level::-1}
        else
            if [[ "$level" == "100%" ]]; then
              level=${level::-1}
            else
              level=${level::-2}
            fi
        fi
    fi
fi

show_icon(){
if [[ "$bat" == *"until"* ]]; then
	if [[ "$level" -ge "95" ]]; then
		echo /usr/share/pmt2e/icons/bat-full-charging.svg
	elif [[ "$level" -ge "75" ]]; then
		echo /usr/share/pmt2e/icons/bat-threefourth-charging.svg
	elif [[ "$level" -ge "35" ]]; then
		echo /usr/share/pmt2e/icons/bat-half-charging.svg
	elif [[ "$level" -ge "15" ]]; then
		echo /usr/share/pmt2e/icons/bat-quarter-charging.svg
	else
		echo /usr/share/pmt2e/icons/bat-empty-charging.svg
	fi
else
	if [[ "$level" -ge "95" ]]; then
		echo /usr/share/pmt2e/icons/bat-full.svg
	elif [[ "$level" -ge "75" ]]; then
		echo /usr/share/pmt2e/icons/bat-threefourth.svg
	elif [[ "$level" -ge "35" ]]; then
		echo /usr/share/pmt2e/icons/bat-half.svg
	elif [[ "$level" -ge "15" ]]; then
		echo /usr/share/pmt2e/icons/bat-quarter.svg
	else
		if [[ "$level" -le "5" ]]; then
			ogg123 -q /usr/share/sounds/freedesktop/stereo/bell.oga
			dunstify -t 5000 -h string:x-dunst-stack-tag:battery -u critical "$bat"
		fi
		echo /usr/share/pmt2e/icons/bat-empty.svg
	fi
fi
if [[ $2 == "-l" ]]; then
	echo ${level}%
fi
}

show_glyphs(){
if [[ "$bat" == *"until"* ]] || [[ "$bat" == *"Not charging"* ]] || [[ "$bat" == *"Full"* ]] ; then
	if [[ "$level" -eq "100" ]]; then
		echo "󰂅"
	elif [[ "$level" -ge "90" ]]; then
		echo "󰂋"
	elif [[ "$level" -ge "80" ]]; then
		echo "󰂊"
	elif [[ "$level" -ge "70" ]]; then
		echo "󰢞"
	elif [[ "$level" -ge "60" ]]; then
		echo "󰂉"
	elif [[ "$level" -ge "50" ]]; then
		echo "󰢝"
	elif [[ "$level" -ge "40" ]]; then
		echo "󰂈"
	elif [[ "$level" -ge "30" ]]; then
		echo "󰂇"
	elif [[ "$level" -ge "20" ]]; then
		echo "󰂆"
	elif [[ "$level" -ge "10" ]]; then
		echo "󰢜"
	else
		echo "󰢟"
	fi
else
	if [[ "$level" -eq "100" ]]; then
		echo "󰁹"
	elif [[ "$level" -ge "90" ]]; then
		echo "󰂂"
	elif [[ "$level" -ge "80" ]]; then
		echo "󰂁"
	elif [[ "$level" -ge "70" ]]; then
		echo "󰂀"
	elif [[ "$level" -ge "60" ]]; then
		echo "󰁿"
	elif [[ "$level" -ge "50" ]]; then
		echo "󰁾"
	elif [[ "$level" -ge "40" ]]; then
		echo "󰁽"
	elif [[ "$level" -ge "30" ]]; then
		echo "󰁼"
	elif [[ "$level" -ge "20" ]]; then
		echo "󰁻"
	elif [[ "$level" -ge "10" ]]; then
		echo "󰁺"
	else
		if [[ "$level" -le "5" ]]; then
			ogg123 -q /usr/share/sounds/freedesktop/stereo/bell.oga
			dunstify -t 5000 -h string:x-dunst-stack-tag:battery -u critical "$bat"
		fi
		echo "󰂎"
	fi
fi
}

if [[ $1 == -N* ]]; then
	echo "Bat: ${level}%"
elif  [[ $1 == "-n"* ]]; then
	if [[ "$level" -le "5" ]]; then
		if [[ "$bat" == *"until"* ]]; then
			dunstify -t 2500 -h string:x-dunst-stack-tag:battery -u normal "$bat"
			exit
		fi
	else
		dunstify -t 2500 -h string:x-dunst-stack-tag:battery -u normal "$bat"
		exit
	fi
elif  [[ $1 == "-F"* ]]; then
	show_glyphs
else
	show_icon
fi
