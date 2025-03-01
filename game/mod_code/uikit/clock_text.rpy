# Text clock on the corner of the login and desktop screen.

image wm_clock_colon:
    Text("{lexend=regular}:{/lexend}", size=48)
    0.5
    Null()
    0.5
    repeat

init python in _wm_clock_text:
    from store import (
        DynamicDisplayable,
        Text,
        wm_game_time
    )

    def __format_time():
        now = wm_game_time.now()
        fmt_time = now.strftime("{lexend=regular}%I:%M{/lexend}")
        return fmt_time + " " + now.strftime("{lexend=light}%p{/lexend}").lower()

    def __format_date():
        now = wm_game_time.now()
        return now.strftime("{lexend=regular}%A{/lexend}{lexend=light}, %d %B, %Y{/lexend}")

    class ClockText(object):
        def __init__(self, func, size):
            self.text = Text("", size=size)
            self.func = func

        def __call__(self, st, at):
            self.text.set_text(self.func())
            return self.text, 0.0

    def __get_text_displayable(st, at, func, size):
        return Text(func(), size=size), 0.0

    time_display = DynamicDisplayable(ClockText(__format_time, 48))
    date_display = DynamicDisplayable(ClockText(__format_date, 36))

screen wm_clock_text():
    vbox:
        add _wm_clock_text.time_display xalign 1.0
        add _wm_clock_text.date_display

screen wm_clock_text_left():
    vbox:
        add _wm_clock_text.time_display
        add _wm_clock_text.date_display

screen wm_clock_text_centered():
    vbox:
        add _wm_clock_text.time_display xalign 0.5
        add _wm_clock_text.date_display xalign 0.5
