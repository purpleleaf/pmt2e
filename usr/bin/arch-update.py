#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/purpleleaf/pmt2e
# License: GPL3

# Credits: RaphaelRochet/arch-update
# https://github.com/RaphaelRochet/arch-update
# Icon by @edskeye

Arguments [-C<aur_helper>] | [-U<aur_helper> <terminal>] | [menu] | -[O] [-N] | [-M<custom_name>]

[-C<aur_helper>] - check updates
[-U<terminal>,<aur_helper>] - update systerm with provided AUR helper and terminal 
[-O] - show pending updates as notification
[-N] - name instead of icon
[menu] - show context jgmenu

Dependencies: `pacman-contrib`
Optional: `pacaur` | `trizen` | `yay`, `jgmenu`
"""

import sys
import os
import subprocess


def main():
    name = None
    helper_name, terminal_name, helper_cmd, updates = "", "", "", ""
    do_check, do_update, do_notify = False, False, False

    tmp_file = os.getenv("HOME") + "/.arch-updates"

    check_command = 'sh -c "checkupdates > ' + tmp_file

    aur_check_commands = {'pacaur': 'pacaur check -q',
                          'trizen': 'trizen -Qqu -a',
                          'yay': 'yay -Qqu -a'}
    font_icon = False

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):

            if sys.argv[i].upper() == '-O':
                do_check = False
                do_update = False
                do_notify = True
                break

            elif sys.argv[1].upper() == "MENU":
                show_menu()
                break

            if sys.argv[i].upper().startswith('-C'):
                try:
                    helper_cmd = aur_check_commands[sys.argv[i][2::]]
                except KeyError:
                    helper_cmd = ""
                    pass
                if helper_cmd:
                    check_command += " && " + helper_cmd
                check_command += ' >> ' + tmp_file + '"'
                do_check = True
                do_update = False
                do_notify = False

            if sys.argv[i].upper().startswith('-U'):
                tools = sys.argv[i][2::].split(":")
                terminal_name = tools[0]
                try:
                    helper_name = tools[1]
                except IndexError:
                    helper_name = "sudo pacman"
                do_check = False
                do_update = True
                do_notify = False

            if sys.argv[i].upper() == '-N':
                name = "Upd:"

            if sys.argv[i].upper().startswith('-M'):
                name = sys.argv[i][2::]

            if sys.argv[i].upper() == '-F':
                font_icon = True

            if sys.argv[i] == '-h' or sys.argv[i] == '--help':
                print("\npmt2e --update -C[aur_helper] | -U<terminal>[:aur_helper] | [-O] [-N] | [-M<custom_name>]\n")
                print("-C[aur_helper] - (C)heck updates with pacman and optionally AUR helper")
                print(" example: pmt2e --update -Ctrizen")
                print(" Check 'Show icon' and set 'Continous output' to 2 in Tint2 settings\n")
                print("-U<terminal>[:aur_helper] - (U)pdate in <terminal> with pacman or AUR helper")
                print(" example: pmt2e --update -Uxfce4-terminal:trizen\n")
                print("-O - display saved pending updates as n(O)tification")
                print("-N - print (N)ame instead of icon")
                print("-M<custom_name> - print custom na(M)e instead of icon\n")
                print("-F - show icon as font glyphs (requires a Nerd font of your choice)")
                print(" Uncheck 'Show icon' and set 'Continous output' to 1 in Tint2 settings\n")

    if do_check:
        if name is not None:
            os.system("echo Checking...")
        elif font_icon:
            os.system("echo 󰂪")
        else:
            os.system("echo /usr/share/pmt2e/icons/refresh.svg")
            os.system("echo ''")

        subprocess.call(check_command, shell=True)
        updates = open(tmp_file, 'r').read().rstrip()
        num_upd = len(updates.splitlines())

        if name is not None:
            if num_upd > 0:
                print(name + " " + str(num_upd))
            else:
                print("Up-to-date")
        elif font_icon:
            if num_upd > 0:
                print('󱆢')
            else:
                print("󰕥")
        else:
            if num_upd > 0:
                os.system("echo /usr/share/pmt2e/icons/arch-icon-notify.svg")
                os.system("echo ''")
            else:
                os.system("echo /usr/share/pmt2e/icons/arch-icon.svg")
                os.system("echo ''")

    if do_update:
        command = terminal_name + ' -e \'sh -c \"' + helper_name + ' -Syu; echo Press enter to exit; read; killall -SIGUSR1 tint2\"\''
        subprocess.call(command, shell=True)

    if do_notify:
        updates = open(tmp_file, 'r').read().rstrip()
        notify(updates)


def notify(updates):
    subprocess.call(
        ['notify-send', "Pending updates:", "--icon=/usr/share/pmt2e/icons/arch-update48.svg", "--expire-time=5000", updates])


def show_menu():
    try:
        subprocess.check_output("which jgmenu", shell=True)
    except subprocess.CalledProcessError:
        print("\nInstall jgmenu package, run `jgmenu init`\n")
        return

    pmt2e_dir = os.getenv("HOME") + "/.config/pmt2e"
    if not os.path.isdir(pmt2e_dir):
        os.makedirs(pmt2e_dir)
    if not os.path.isfile(pmt2e_dir + "/menu-update"):
        subprocess.call(["cp /usr/lib/pmt2e/menu-update "+ pmt2e_dir + "/menu-update"], shell=True)
    subprocess.call([pmt2e_dir + '/menu-update'], shell=True)


if __name__ == "__main__":
    main()
