#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
Author: Piotr Miller
e-mail: nwg.piotr@gmail.com
Website: http://nwg.pl
Project: https://github.com/purpleleaf/pmt2e
License: GPL3

Credits: mreithub at https://unix.stackexchange.com/a/67398 (and comments below!)

Dependencies: 'jgmenu' 'pulseaudio' 'pulseaudio-alsa'

This script creates jgmenu to switch audio output with the pa-switch-output helper script
"""

import os
import subprocess


def main():
    # get sink numbers
    sinks = subprocess.check_output("pactl list short sinks", shell=True).decode("utf-8").splitlines()

    # get output descriptions
    names = subprocess.check_output("pacmd list-sinks | grep device.description | awk -F '=' '{print $2}'",
                                    shell=True).decode("utf-8").splitlines()
    outputs = []

    # Tuples ("sink_number", "output_description")
    for output in range(len(sinks)):
        output = sinks[output].split()[0], names[output].strip()[1:-1]
        outputs.append(output)

    # Create jgmenu script
    jgmenu = []
    jgmenu.append("#!/bin/sh\n")
    jgmenu.append("config_file=$(mktemp)")
    jgmenu.append("menu_file=$(mktemp)")
    jgmenu.append("trap \"rm -f ${config_file} ${menu_file}\" EXIT\n")
    jgmenu.append("cat << 'EOF' >${config_file}")
    jgmenu.append("stay_alive           = 0")
    jgmenu.append("tint2_look           = 1")
    jgmenu.append("menu_width           = 40")
    jgmenu.append("menu_border          = 1")
    jgmenu.append("item_height          = 20")
    jgmenu.append("font                 = Sans 10")
    jgmenu.append("icon_size            = 0")
    jgmenu.append("color_norm_fg        = #eeeeee 100")
    jgmenu.append("color_sel_fg         = #eeeeee 100")
    jgmenu.append("EOF\n")
    jgmenu.append("cat <<'EOF' >${menu_file}")

    # Use previously saved tuples (sink_number, output_description) to create jgmenu entries
    for output in outputs:
        jgmenu.append(output[1] + ", " + "/usr/lib/pmt2e/pa-switch-output " + output[0])

    jgmenu.append("EOF\n")
    jgmenu.append("jgmenu --config-file=${config_file} --csv-file=${menu_file}")

    # Exit if jgmenu not installed
    try:
        subprocess.check_output("which jgmenu", shell=True)
    except subprocess.CalledProcessError:
        os.system("notify-send 'Install jgmenu package, run jgmenu init'")
        exit(0)

    # Save jgmenu script
    pmt2e_dir = os.getenv("HOME") + "/.config/pmt2e"
    if not os.path.isdir(pmt2e_dir):
        os.makedirs(pmt2e_dir)

    with open(pmt2e_dir + '/pulseaudio-menu', 'w') as f:
        for item in jgmenu:
            f.write("%s\n" % item)

    # Make executable
    os.system("chmod u+x " + pmt2e_dir + "/pulseaudio-menu")

    # Execute jgmenu script
    os.system(pmt2e_dir + "/pulseaudio-menu &")


if __name__ == "__main__":
    main()
