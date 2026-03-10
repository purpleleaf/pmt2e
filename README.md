# Poor  Man Tint2 Executors

A set of scripts to use as tint2 executors.

Forked from [t2ec](https://github.com/nwg-piotr), pmt2e is written with these purposes:

  * substitution of zenity with yad

  * add use of font glyphs beside text and icons output (requires a [Nerd Font](https://www.nerdfonts.com/) of your  choice)

  * remove  the use of a single  scripts to invoke all the others
; this choice in my opinion simplifies  the use of the scripts reducing the  number of options

  * porting python scripts to shell scripts

  * use OpenMeteo instead of OpenWeatherMaps

  * use separate name for exery tint2 executor instead of grouping all executors under  a single script calling  them (work in progress).

Many scripts show no changes related to the t2ec ones, excluding font glyphs, others are more  deeply modified and/or rewritten. Many other code snippets taken from other projects are used and credits are reported in every script description.

## PMU (Poor Man Updater)

`pmu` is a posix compliant update manager designed for lightweight Desktop Environment, intended for use as an **executor** or **custom module** for panels and bars.

---

### Features
* **Native support** for `tint2`, `Waybar`, `Polybar`, and `sfwbar`.
* **Checks system repositories** (Pacman) and AUR (via helpers).
* **Flatpack support**
* **Distro Agnostic:** While optimized for Arch Linux, it provides a robust override system to any other distribution via custom commands. It should work on BSD also.
* **Flexible UI Output:**
    * **Text:** Simple strings for classic bars.
    * **Glyphs:** Nerd Font support for minimalist setups.
    * **Icons:** Absolute path output for panel executors (like tint2).
* **Interactive Management:** Built-in `jgmenu` and `yad` integration for listing packages and launching upgrades without touching the terminal manually.

---

### Requirements
To use all features of the script, ensure the following are installed:
* **System:** `sh` (POSIX compliant shell) and `pgrep`.
* **Arch Linux:** `pacman-contrib` (provides the `checkupdates` binary).
* **GUI Elements:** 
    * **yad:** For the desktop notification window and the package list.
    * **jgmenu:** For the interactive right-click or status menu.
* **Fonts:**
    * **Nerd Fonts:** Required if you use the Glyph output (`-f`).

---

### Installation
Ensure the script is in your `$PATH` (e.g., `/usr/bin/pmu`) and has execution permissions:
`chmod +x /usr/bin/pmu`

### Configuration
The script creates a configuration file at `~/.config/pmt2e/pmu.conf` on its first run. 
* **Terminals:** It auto-detects common terminals, but you can force your preferred one (e.g., `terminal=kitty`).
* **AUR:** If you use an AUR helper like `yay` or `paru`, set `arch_use_helper=true`.
* **Customization:** If you are on a non-Arch system, you can define your own commands in this file.

### Integration with Status Bars

**For tint2 (Icon mode):**
Set the executor command to `pmu -c [-i|-f|-t]` to return the appropriate package status [icon|text]. Assignto left or right click the command menu with pmu -m [-i|-f|t].

**For Waybar (Text or Glyph mode):**
Configure a custom module with the command `pmu -c -t` and a click action like `pmu -m [-i|-f|t]` for command menu.

**For Polybar (Text or Glyph mode):**
Use a `custom/script` module with `exec = pmu -c -f` and assign `click-left = pmu -m  -m [-i|-f|t]` for command menu.

**For sfwbar (Icon or Glyph mode):**
In your sfwbar config, use configure an `exec` module with Command = "pmu -c -i" and Action[LeftClick] = "pmu -m -i" .

---

### Usage Summary

#### Choose one Output Format:
* **-i (Icon):** Returns the path to a status icon.
* **-t (Text):** Returns a simple string (e.g., `Upd: 12`).
* **-f (Glyph):** Returns a Nerd Font icon (e.g., `󱆢`).

#### Choose one Action:
* **-c:** **Check** (Primary command for bars).
* **-n:** **Notify** (Shows a list of pending updates in a window).
* **-u:** **Upgrade** (Opens terminal and starts the system upgrade).
* **-m:** **Menu** (Opens the interactive jgmenu).
* **-p:** **Toggle Flatpak** (Enables or disables Flatpak checks).
* **-e:** **Empty Cache** (Runs the package manager's cleaning utility).

---

### Overriding Commands (e.g. Debian/Ubuntu)
If you are not using Arch Linux, you can make the script work by setting these variables in `~/.config/pmt2e/pmu.conf`:

* **check_cmd:** `'apt list --upgradable 2>/dev/null | grep -c /'`
* **upgrade_cmd:** `'sudo apt update && sudo apt upgrade'`
* **clean_cmd:** `'sudo apt autoremove && sudo apt clean'`


##  Poor Man Weather - pmw

pmw is an executor displaying an icon corresponding to  the current weather  in tint2. If invoked with the -n switch, through a mouse click  on the icon (setted in tint2 preferences), it display a notification showing current weather and the forecast for the next hours.
Wheater data are provided by open-meteo.com,  and can be queried without restriction until to 10.000 call/day.

pmw  settings are provided by yad, that is called at first run and can be recalled  through a jgmenu with the command:

`pmw -m`

The yad settings windows let you choose your preferred  measure units, the weather forecast location, if you want light or dark themed icon or  font glyphs as executor output and if you prefer coloured or dark themed icons for notifications.
Fonts glyphs require some adjustment in tint2 settings (notably  may be necessary set an adequate horizontal padding).

If you want you can also have  only text as output instead of icons, running this command:

`pwm -t`

An help message is displayed using the command:

pmw -h

Dependencies: curl, jq, yad, awk, dunst.

##  volume-icon

volume-icon display an icon  as tint2 executor showing current volume level.  Command can be linked in executor to mouse event  to raise or low volume level and to toggle mute.

Usage: volume-icon [ -h | -n | -m | -m ] [ -i | -f | -t ]

  -h, Show this help message and exit.
  -s, set volume to the number passed as argument.
  -u, raise volume.
  -d, lower volume.
  -m, toggle mute.

  -i, output an icon path to Tint2.
  -f, output a font glyph instead of icon.
  -t, output text instead of icon.
Only one option for both the two option group must be provided.
If -s is selected an integer number (0-100) must be provided.
If -h is selected no other option is required.

Dependencies: alsa-utils dunst.

##  battery-icon

battery-icon display an icon  as tint2 executor showing current battery level.  Command can be linked to mouse event in executor, to show a notification. If battery level goes under 5% an alert sound is played.

Usage: battery-icon [ -h | -n | -m | -t | -f | -i ]

  -h, Show this help message and exit.
  -n, Show notification.
  -m, Show jgmenu.
  -t, show only text as tint2 executor output.
  -f, show a font gyph as tint2 executor output.
  -i, show an icon as tint2 executor output.
If multiple arguments are provided, only the first one will considered

Dependencies: acpi ogg123 (vorbis-tools) dunst.

## yad-box  volume-icon

A slider changing the volume level, nothing more, nothing less.

## createjgmenu

A simple utility to create jgmenu. Used in  other pmt2e scripts and useful if you want attach your own menus to the pmt2e icons.

```bash
Usage: /home/max/.local/bin/createjgmenu -c config_file | -m menu_file | -h | list of command to feed jgmenu

  -h Show this help message and exit.
  -c config_file, use config_file to set jgmenu configuration.
  -m menu_file, use menu_file to fill jgmenu.

If -m is provided any other eventual argument passed to build the menu will be ignored.
Menu items must be passed in the form "Menu name,/command/to/execute.
```
You could directly use jgmenu --vsimple, but in my opinion createjgmenu is more intuitive , if  executed without config file produce an already integrated tint2 menu and menu items  can be passed to command line in a simpler way.

Dependencies: jgmenu.






