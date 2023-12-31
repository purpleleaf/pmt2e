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






