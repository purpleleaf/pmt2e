#!/bin/bash

# This script display an appropriate volume icon according to the volume level

# Authors: 
# Piotr Miller nwg.piotr@gmail.com
# Max Franco purpleleaf@ganoia.eu
# License: GPL3

# Dependencies: `alsa-utils`
# arguments: [up] | [down] | [toggle] | [<level>] [-N]

# Check volume for Lefth/Right audio channel or Mono Channel
control="Master"
output=`amixer sget $control`
levels=`echo "$output" | grep -o -e '\[[[:digit:]]*%\]'`
num=`echo "$levels" | wc -l`
sum=`echo "$levels 0" | tr '[%]\n' '  + ' | xargs expr`
vol=`expr $sum / $num`

function is_mute {
    amixer get Master | grep '%' | grep -oE '[^ ]+$' | grep off > /dev/null
}

function send_notification {
    notify-send.sh -i $2 -t 1000 -h string:x-dunst-stack-tag:volume -u normal "$1%" -h int:value:$1
}

function get_icon {
if [[ "$(amixer get Master | grep '%' | grep -oE '[^ ]+$')" == *"[on]"* ]]; then
        if [[ ${vol} -ge 90 ]]; then
            icon="/usr/share/pmt2e/icons/vol-full.svg"
        elif [[ ${vol} -ge 40 ]]; then
            icon="/usr/share/pmt2e/icons/vol-medium.svg"
        elif [[ ${vol} -ge 10 ]]; then
            icon="/usr/share/pmt2e/icons/vol-low.svg"
        else
            icon="/usr/share/pmt2e/icons/vol-lowest.svg"
fi
else
	icon="/usr/share/pmt2e/icons/vol-muted.svg"
fi
echo ${icon}
}

function get_glyph {
if [[ "$(amixer get Master | grep '%' | grep -oE '[^ ]+$')" == *"[on]"* ]]; then
	if [[ ${vol} -ge 66 ]]; then
		glyph="󰕾"
	elif [[ ${vol} -ge 33 ]]; then
		glyph="󰖀"
	else
		glyph="󰕿"
	fi
else
	glyph="󰖁"
fi
echo ${glyph}
}

if [[ $1 == *"-F"* ]] || [[ $2 == *"-F"* ]]; then
	get_glyph
else
	get_icon
fi

volicon=$(get_icon)

case $1$2 in
	*-N*)
    echo "Vol: ${vol}%"
	;;
	*up*)
	# Set the volume on (if it was muted)   
	if is_mute ; then
    amixer sset Master toggle -q
    fi
    amixer sset Master 5%+ -q
    send_notification ${vol} ${volicon}
	;;
	*down*)
	if is_mute ; then
     amixer -D default set Master on > /dev/null
    fi
    amixer sset Master 5%- -q
    send_notification ${vol} ${volicon}
	;;
	*toggle*)
	if is_mute ; then
    	amixer sset Master toggle -q
		notifyicon=$(get_icon)
    	send_notification ${vol} ${notifyicon}
    else
    	amixer sset Master toggle -q
		notify-send.sh -i "/usr/share/pmt2e/icons/vol-muted.svg" -t 1000 -h string:x-dunst-stack-tag:volume -u normal "Muted"
	fi
	;;
	*)
    # If none of above, check if argument is a valid int, set volume if so
    if [[ $(($1)) == $1 ]] && [[ "$1" -ge 0 ]] && [[ "$1" -le 100 ]]; then
        amixer set Master "$1"% -q
    fi
	;;
esac
