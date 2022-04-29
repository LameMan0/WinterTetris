screen dock():
    style_prefix "dock"

    if _wm_manager.open_apps:
        frame at dock_animation:
            has hbox:
                spacing 10

            for app in _wm_manager.open_apps:
                use dock_app_icon(app)

transform dock_animation:
    yoffset 15
    ypos 1.0

    on show:
        ease_cubic 0.5 yoffset -15 yanchor 1.0

    on hide:
        ease_cubic 0.5 yoffset 15 yanchor 0.0 

style dock_frame:
    xalign 0.5 yalign 0.99
    ysize 120
    background RoundedFrame(Solid("#fff5"), radius=20.0, outline_width=1.5, outline_color="#fff8")
    padding (10, 10)

screen dock_app_icon(app):
    button action Function(app.raise_window):
        padding (10, 10)
        add app.icon fit "contain"