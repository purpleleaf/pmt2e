#!/bin/sh

# Set desired level with a yad dialog box

# Dependencies: `alsa-utils`, `acpilight` or `light-git`, `yad`
# Arguments: [bri] | [vol]

if [[ $1 == bri* ]]; then

    # Prefer the `light` package, use `xbacklight` if `light` not found
    if [[ $(which light) == *"/light"* ]]; then
        lvl=$(light -G)
    else
        lvl=$(xbacklight -get)
    fi

    lvl=$(echo ${lvl} | awk '{ printf"%0.0f\n", $1 }')

    yad --scale --value ${lvl} --print-partial --mouse --no-buttons \
    --undecorated --skip-taskbar --sticky --close-on-unfocus --height 400 --vertical --on-top --class="yad_slider" 2> /dev/null | \
    while read BRI; do
        if [[ $(which light) == *"/light"* ]]; then
            light -S $BRI 2>&1 >/dev/null
        else
            xbacklight -set "$BRI" 2>&1 >/dev/null
        fi
    done &

elif [[ $1 == vol* ]]; then
    lvl=$(amixer sget Master | grep 'Mono:' | awk -F'[][]' '{ print $2 }')
    lvl=${lvl::-1}
    yad --scale --value ${lvl} --print-partial --mouse --no-buttons \
    --undecorated --skip-taskbar --sticky --close-on-unfocus --height 400 --vertical --on-top --class="yad_slider" | \
    while read VOL; do
      amixer sset 'Master' "$VOL%" 2>&1 >/dev/null
    done &
else
    echo "Allowed arguments: vol | bri"
fi



