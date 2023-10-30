#!/bin/sh

if [[ ! -d ~/.config/pmt2e ]]; then
    mkdir -p ~/.config/pmt2e
fi

if [[ $1 == --bbswitch ]]; then
    if [[ ! -f ~/.config/pmt2e/menu-bbswitch.sh ]]; then
        cp /usr/lib/pmt2e/menu-template.sh ~/.config/pmt2e/menu-bbswitch.sh
    fi
    exec ~/.config/pmt2e/menu-bbswitch.sh
fi

if [[ $1 == --brightness ]]; then
    if [[ ! -f ~/.config/pmt2e/menu-brightness.sh ]]; then
        cp /usr/lib/pmt2e/menu-template.sh ~/.config/pmt2e/menu-brightness.sh
    fi
    exec ~/.config/pmt2e/menu-brightness.sh
fi

if [[ $1 == --brightness ]]; then
    if [[ ! -f ~/.config/pmt2e/menu-brightness.sh ]]; then
        cp /usr/lib/pmt2e/menu-template.sh ~/.config/pmt2e/menu-brightness.sh
    fi
    exec ~/.config/pmt2e/menu-brightness.sh
fi

if [[ $1 == --lbrightness ]]; then
    if [[ ! -f ~/.config/pmt2e/menu-lbrightness.sh ]]; then
        cp /usr/lib/pmt2e/menu-template.sh ~/.config/pmt2e/menu-lbrightness.sh
    fi
    exec ~/.config/pmt2e/menu-lbrightness.sh
fi

if [[ $1 == --volume ]]; then
    if [[ ! -f ~/.config/pmt2e/menu-volume.sh ]]; then
        cp /usr/lib/pmt2e/menu-template.sh ~/.config/pmt2e/menu-volume.sh
    fi
    exec ~/.config/pmt2e/menu-volume.sh
fi

if [[ $1 == --wifi ]]; then
    if [[ ! -f ~/.config/pmt2e/menu-wifi.sh ]]; then
        cp /usr/lib/pmt2e/menu-template.sh ~/.config/pmt2e/menu-wifi.sh
    fi
    exec ~/.config/pmt2e/menu-wifi.sh
fi

if [[ $1 == --weather ]]; then
    if [[ ! -f ~/.config/pmt2e/menu-weather.sh ]]; then
        cp /usr/lib/pmt2e/menu-template.sh ~/.config/pmt2e/menu-weather.sh
    fi
    exec ~/.config/pmt2e/menu-weather.sh
fi

if [[ $1 == --battery ]]; then
    if [[ ! -f ~/.config/pmt2e/menu-battery.sh ]]; then
        cp /usr/lib/pmt2e/menu-template.sh ~/.config/pmt2e/menu-battery.sh
    fi
    exec ~/.config/pmt2e/menu-battery.sh
fi
