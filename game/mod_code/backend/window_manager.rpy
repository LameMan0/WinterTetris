init -5 python in _wm_manager:
    zorders = [ ]
    positions = { }
    position_serial = 100

    def get_zorder(screen_id):
        if screen_id in zorders:
            return zorders.index(screen_id) + 1

        zorders.append(screen_id)
        return len(zorders)

    def update_zorders():
        for screen_id in zorders:
            screen = renpy.get_screen(screen_id)
            if screen is None:
                continue

            renpy.change_zorder(screen.layer, screen.tag, get_zorder(screen_id))

        renpy.restart_interaction()

    def get_position(screen_id):
        global position_serial

        if screen_id in positions:
            return positions[screen_id]

        new_pos = (position_serial, position_serial)

        position_serial += 100
        positions[screen_id] = new_pos

        return new_pos

    class Application(object):
        def __init__(self, name, screen_id):
            self.name = name
            self.screen_id = screen_id

        def raise_window(self, *args, **kwargs):
            if self.screen_id in zorders:
                zorders.remove(self.screen_id)

            zorders.append(self.screen_id)
            update_zorders()

        def change_position(self, drags, drops):
            d = drags[0]
            x, y = d.x, d.y
            positions[self.screen_id] = (x, y)

        def open(self, *args, **kwargs):
            renpy.show_screen(self.screen_id, _zorder=get_zorder(self.screen_id), *args, **kwargs)

        def close(self):
            renpy.hide_screen(self.screen_id)
            if self.screen_id in zorders:
                zorders.remove(self.screen_id)

screen program_header(title, close_action=NullAction()):
    style_prefix "header"

    frame:
        text "[title]" xalign 0.5
        imagebutton:
            idle RoundedFrame(Solid("#FF3D00"), xysize=(22, 22)).set_radius(11.0)
            hover RoundedFrame(Solid("#ff5926"), xysize=(22, 22)).set_radius(11.0)
            action close_action xalign 1.0 yalign 0.5 xoffset -10

style header_text is empty
style header_frame is empty
style header_image_button is button

style header_text:
    font _wm_font_ubuntu.medium
    size 20
    yalign 0.5

style header_frame:
    background "#505050"
    xfill True ysize 40

screen program_base(app, **props):
    drag at [ window_animation ]:
        pos _wm_manager.get_position(app.screen_id)
        activated app.raise_window
        dragged app.change_position
        draggable True

        vbox properties props:
            at RoundedWindows(radius=10.0, outline_width=3.0, outline_color="#828282")
            use program_header(app.name, Function(app.close))

            transclude

