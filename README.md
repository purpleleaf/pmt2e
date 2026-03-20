# 🛠️ pmt2e - Poor Man Tint2 Executors

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![AUR version](https://img.shields.io/aur/version/pmt2e-git)](https://aur.archlinux.org/packages/pmt2e-git)

**pmt2e** is a set of POSIX-compliant scripts designed to extend the functionality of `tint2`, `Waybar`, `sfwbar`, and other lightweight panels. Born as a fork and a deep rewrite of [t2ec](https://github.com/nwg-piotr/t2ec), it has evolved into a project that prioritizes readability, stability, and system efficiency.

---

## 💡 Why pmt2e?

The idea behind pmt2e stems from a simple observation: a modern desktop environment shouldn't devour 1.4 GB of RAM just to stay on when it's possible to have a complete, elegant, and functional desktop using merely 100 MB.

I wanted to create a tool that was, first and foremost, **universal**. For this reason, I chose the **POSIX** standard (`#!/bin/sh`): the code must be able to run anywhere, not only on Linux but potentially on BSD systems as well, without depending on "bashisms" or the specifics of a single shell. 

The code is written in a linear and vertical way because I believe software must be **readable and educational**. Anyone should be able to open a script and understand what is happening on their PC without being an engineer. Too often, we are forced to use disproportionate tools: network managers designed for devices with dozens of Ethernet ports when we only use Wi-Fi, audio servers for music professionals when we just want to listen to Spotify, or weather applets that take up 200 MB of memory just to tell us if it's raining.

pmt2e is the minimalist answer to all this: essential, transparent, and lightweight tools. Currently, the project is optimized for **Openbox**, but with an eye to the future: it will be adapted for Wayland environments (such as `labwc` or `waybox`) as soon as all the necessary components are mature.

---

## 📦 Main Components

| Script | Full Name | Description |
| :--- | :--- | :--- |
| **`pmupdater`** | Poor Man Updater | Update Manager for Pacman, AUR, and Flatpak. |
| **`pmweather`** | Poor Man Weather | Weather based on OpenMeteo (no API keys). |
| **`pmbattery`** | Poor Man Battery | Battery monitor with audio alarms and notifications. |
| **`pmvolume`** | Poor Man Volume | Audio volume manager with YAD slider. |
| **`pmbrightness`**| Poor Man Brightness | Smooth backlight control. |
| **`pmnetwork`** | Poor Man Network | Wi-Fi/Eth network monitoring and management. |
| **`pmdesktop`** | Poor Man Desktop | Utility for session and desktop management. |

---

## 🚀 Installation

### Arch Linux (AUR)
The fastest method is using an AUR Helper:
```bash
yay -S pmt2e-git
```

### Other Distributions / BSD (Manual)
```bash
git clone [https://github.com/purpleleaf/pmt2e.git](https://github.com/purpleleaf/pmt2e.git)
cd pmt2e
sudo cp -r usr/bin/* /usr/bin/
sudo cp -r usr/share/pmt2e /usr/share/
```

### Dependencies
For the proper functioning of all components, ensure you have the following installed:
- `sh` (POSIX Shell)
- `yad` (for all graphical interfaces)
- `jgmenu` (for context menus)
- `curl` & `jq` (for weather data and updates)
- `Nerd Fonts` (for graphical output via glyph `-f`)

---

## 🛠️ Integration in tint2

To use a script as an executor, add these lines to your `tint2rc` (or use the Settings GUI):

```bash
# Example for Volume control
execp = pmvolume -i
left_click = pmvolume -m
```

For detailed instructions and to learn about the dependencies for each script, check the [pmt2e Wiki](https://github.com/purpleleaf/pmt2e/wiki).

---

## 💳 Credits
Inspired by the original work of **nwg-piotr** ([t2ec](https://github.com/nwg-piotr/t2ec)). Completely rewritten, converted to POSIX Shell, and optimized by **purpleleaf**.
