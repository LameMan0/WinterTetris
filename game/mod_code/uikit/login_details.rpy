screen login_details():
    style_prefix "login_details"

    vbox:
        text "{user}" size 200 xalign 0.5
        null height 20
        text turnell_username() xalign 0.5
        null height 40
        textbutton "{login} Login" action Start() xalign 0.5

style login_details_text:
    font _wm_font_lexend.regular size 48

style login_details_button_text:
    font _wm_font_lexend.light size 32