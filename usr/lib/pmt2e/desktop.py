#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

This script uses `wmctrl` to switch desktops, or just prints path to the icon corresponding to currently active desktop,
followed by the desktop number as text.

Author: Piotr Miller
e-mail: nwg.piotr@gmail.com
Website: http://nwg.pl
Project: https://github.com/purpleleaf/pmt2e
License: GPL3

Arguments [next] | [prev] | [<number>] | [-menu] [-N]

[next] - switch to next desktop
[prev] - switch to previous desktop
[number] - switch to desktop of number given

"""

import sys
import subprocess
import os


def main():
    output = subprocess.check_output("wmctrl -d", shell=True)
    desktops = output.splitlines()
    textual = False
    glyph = False
    current = current_desktop(desktops)
    last = len(desktops) - 1

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i].upper() == "NEXT":
                next_desktop(current, last)
            elif sys.argv[i].upper() == "PREV" or sys.argv[1].upper() == "PREVIOUS":
                previous_desktop(current, last)
            elif sys.argv[i].upper() == "-N":
                textual = True
            elif sys.argv[i].upper() == "MENU":
                create_menu(last + 1)
            elif sys.argv[i].upper() == "-F":
                glyph = True
            else:
                try:
                    d = int(sys.argv[i])
                    select_desktop(d - 1, last)
                except ValueError:
                    print("Argument not allowed. Should be: desktop.py [next] | [prev] | [<number>] | [menu] [-N]")

    if textual:
        print("Desktop: " + str(current_desktop(desktops) + 1))
    else:
        if glyph:
            print(str("󰍺 <span font-size=\"xx-small\">" + str(current_desktop(desktops) + 1) + "</span>"))
        else:
            print(str("/usr/share/pmt2e/icons/desktop.svg"))
            print(str(current_desktop(desktops) + 1))

def current_desktop(desktops):
    for d in range(len(desktops)):
        if str(desktops[d]).find("*") > -1:
            return d


def next_desktop(current, last):
    n = current + 1 if current + 1 <= last else 0
    subprocess.call(["wmctrl", "-s", str(n)])


def previous_desktop(current, last):
    n = current - 1 if current - 1 >= 0 else last
    subprocess.call(["wmctrl", "-s", str(n)])


def select_desktop(which, last):
    if 0 <= which <= last:
        subprocess.call(["wmctrl", "-s", str(which)])
    else:
        print("You only have desktops 1-" + str(last + 1))


def create_menu(d_number):
    try:
        subprocess.check_output("which jgmenu", shell=True)
    except subprocess.CalledProcessError:
        print("\nInstall jgmenu package, run `jgmenu init`\n")
        return

    # Just in case user had more or less desktops than 4, let's create a relevant template at the 1st run
    pmt2e_dir = os.getenv("HOME") + "/.config/pmt2e"
    if not os.path.isdir(pmt2e_dir):
        os.makedirs(pmt2e_dir)

    if not os.path.isfile(pmt2e_dir + "/menu-desktop.sh"):
        content = ['#!/bin/sh',
                   '',
                   'config_file=$(mktemp)',
                   'menu_file=$(mktemp)',
                   'trap "rm -f ${config_file} ${menu_file}" EXIT',
                   '',
                   'cat <<\'EOF\' >${config_file}',
                   'stay_alive          = 0',
                   'tint2_look          = 1',
                   'position_mode		= ipc',
                   'menu_width          = 40',
                   'menu_border         = 0',
                   'item_height         = 20',
                   'font                = Sans 10',
                   'icon_size           = 0',
                   'color_norm_fg       = #eeeeee 100',
                   'color_sel_fg        = #eeeeee 100',
                   'EOF',
                   '',
                   'cat <<\'EOF\' >${menu_file}']

        for i in range(1, d_number + 1):
            content.append("desktop " + str(i) + ", pmt2e --desktop " + str(i))

        content.append('EOF')
        content.append('')
        content.append('jgmenu --config-file=${config_file} --csv-file=${menu_file}')

        with open(pmt2e_dir + '/menu-desktop.sh', 'w') as menu_file:
            for row in content:
                menu_file.write('%s\n' % row)

        os.system('chmod +x ' + pmt2e_dir + "/menu-desktop.sh")

    subprocess.call([pmt2e_dir + '/menu-desktop.sh'], shell=True)


if __name__ == "__main__":
    main()
