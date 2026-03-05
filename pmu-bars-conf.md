### 1. Waybar
Waybar uses Real-Time (RT) signals to wake up custom modules. `pmt2e` natively sends `RTMIN+8` when an update finishes. 

Add this module to your `~/.config/waybar/config`:

```json
"custom/updates": {
    "exec": "pmt2e -c -f",
    "interval": 3600,
    "on-click": "pmt2e -u -f",
    "on-click-right": "pmt2e -m -f",
    "signal": 8,
    "tooltip": false
}
```
*Note: Make sure to add `"custom/updates"` to your `modules-left`, `modules-center`, or `modules-right` array.*

---

### 2. Polybar
Polybar requires IPC (Inter-Process Communication) to be enabled so the script can send the `polybar-msg cmd restart` command.

Add this module to your `~/.config/polybar/config.ini`:

```ini
[module/updates]
type = custom/script
exec = pmt2e -c -t
interval = 3600
click-left = pmt2e -u -t
click-right = pmt2e -m -t
```
**Important:** Ensure your main bar configuration has IPC enabled so the refresh command works:
```ini
[bar/mybar]
enable-ipc = true
```

---

### 3. sfwbar (Wayland)
`sfwbar` is a highly flexible floating window bar for Wayland. It uses triggers to listen for RT signals. `pmt2e` natively sends `RTMIN+4` for sfwbar.

Add this button to your layout in `~/.config/sfwbar/sfwbar.config`:

```ini
layout {
  button {
    value = Exec("pmt2e -c -f")
    trigger = "realtime4"
    action[LeftClick] = Exec("pmt2e -u -f")
    action[RightClick] = Exec("pmt2e -m -f")
  }
}
```

---

### 4. tint2
`tint2` listens for the standard `SIGUSR1` signal to refresh all of its executor plugins. `pmt2e` sends this automatically. 

Add an executor to your `~/.config/tint2/tint2rc` (adjust the executor number to fit your setup):

```ini
#-------------------------------------
# Executor 1
execp = new
execp_command = pmt2e -c -t
execp_interval = 3600
execp_has_icon = 0
button = new
button_lclick_command = pmt2e -u -t
button_rclick_command = pmt2e -m -t
```
