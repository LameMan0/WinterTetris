screen power_options(return_action=None):
    style_prefix "power_options"

    button action Quit(confirm=False):
        at power_option_transform
        add _wm_power_button.shutdown

    button action Function(renpy.quit, True):
        at power_option_transform
        add _wm_power_button.restart

    if return_action is not None:
        button action return_action:
            at power_option_transform
            add _wm_power_button.arrow_left

style power_options_button is button

style power_options_button:
    padding (20, 20)
    size_group "power_options_button"
    hover_background RoundedFrame("#fff4", radius=10.0)

init python in _wm_power_button:
    from store import Text, VBox

    def iconbutton(icon, t):
        return VBox(
            Text(icon, size=64, color="#fff", xalign=0.5, yalign=0.1), 
            Text(t, size=24, color="#fff", xalign=0.5, yalign=0.9), 
            xysize=(120, 120)
        )

    shutdown = iconbutton("{power}", "{lexend=light}Shutdown{/lexend}")
    restart = iconbutton("{restart}", "{lexend=light}Restart{/lexend}")
    arrow_left = iconbutton("{arrow_left}", "{lexend=light}Return{/lexend}")

transform power_option_transform:
    alpha 0.6

    on idle:
        easein_quad 0.25 alpha 0.6
    on hover:
        easein_quad 0.25 alpha 1.0