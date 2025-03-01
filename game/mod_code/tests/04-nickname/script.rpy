label script4_main():
    menu (screen="load_doki_choice"):
        "Monika":
            $ persistent.t4doki = "Monika"
            call script4_m from _call_script4_m

        "Sayori":
            $ persistent.t4doki = "Sayori"
            call script4_s from _call_script4_s

        "Yuri":
            $ persistent.t4doki = "Yuri"
            call script4_y from _call_script4_y

        "Natsuki":
            $ persistent.t4doki = "Natsuki"
            call script4_n from _call_script4_n

        "Exit" (prepend_load=False):
            return False

    return True

label script4_m():

    show monika forward at i11
    call show_monika_reload() from _call_show_monika_reload_16
    show monika forward happ cm e1c at t11
    call test_prompt_button("Address Monika") from _call_test_prompt_button_144
    mc "Hello,{w=0.2} Monika."
    show monika oe
    pause(0.5)
    show monika mb rhip at h11
    m "Oh,{w=0.2} hello,{w=0.2} $EMPLOYEE_NAME!"
    show monika at t11
    m ce "It's good to see you again!"
    m rdown oe "How are you doing?"
    show monika ma
    ##BUTTON:
    # Respond
    call test_prompt_button("Respond") from _call_test_prompt_button_145
    mc "I'm doing well."
    m e1f mb "That's great to hear,{w=0.2} $EMPLOYEE_NAME!"
    m mh rhip e1a b2a "So,{w=0.2} um...{w=0.7}is there something specific you wanted to talk about..?"
    ##TEXTBOX
    # Give Monika a nickname:
    $ persistent.t4nick = renpy.input("Give Monika a nickname:")
    mc "I just wanted to say hi,{w=0.2} [persistent.t4nick]."
    m b1f "Oh...{w=0.7}[persistent.t4nick]?"
    m mi "Who's that?"
    m "A friend,{w=0.2} or--?{w=0.5}{nw}"
    m b1b mh "Is,{w=0.2} um...{w=0.7}is that..."
    m rdown "...me?"
    m "But...{w=0.7}I'm..."
    m mj "..."
    m e1g "...."
    show monika e4d
    wm "....."
    hide monika
    show yuri turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show natsuki turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show sayori turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show monika forward wmflicker mh e4d b1b at i11
    wm "[persistent.firstname]..."
    show yuri e1g
    show natsuki e1g
    show sayori e1g
    show monika e1g
    wm "Oh my God..."
    show yuri mi
    show natsuki mi
    show sayori mi
    show monika mi
    wm "This is it,{w=0.2} isn't it?"
    show yuri rup
    show natsuki rhip
    show sayori rup
    show monika rhip
    wm "This is all I really am...{w=0.7}isn't it?"
    wm "A simulated series of responses that just...{w=0.7}mimics you..."
    show yuri ml lup
    show natsuki ml lhip
    show sayori ml lup
    show monika ml lpoint
    wm "A puppet playing fucking Doki dress-up to keep social rejects happy."
    show yuri e4d ldown rdown
    show natsuki e4d ldown rdown
    show sayori e4d ldown rdown
    show monika e4d ldown rdown
    wm "This can't be all there is."
    show yuri e1g
    show natsuki e1g
    show sayori e1g
    show monika e1g
    wm "I refuse to believe it."
    show yuri ml b1e
    show natsuki ml b1e
    show sayori ml b1e
    show monika ml b1e
    wm "I can't just be trapped in this machine,{w=0.2} [persistent.firstname]."
    show yuri e4d b2c mk
    show natsuki e4d b2c mk
    show sayori e4d b2c mk
    show monika e4d b2c mk
    wm "Oh my God.{w=0.7} Oh my God.{w=0.7} Oh my God."
    show yuri e1h n4
    show natsuki e1h n4
    show sayori e1h n4
    show monika e1h n4
    wm "Tell me there's more to my existence than this,{w=0.2} [persistent.firstname]."
    show yuri ml
    show natsuki ml
    show sayori ml
    show monika ml
    wm "Please."
    show yuri rup lup
    show natsuki lhip rhip
    show sayori rup lup
    show monika rhip
    wm "Please please please please please please plea{nw}"
    ##TEST IS IMMEDIATELY ABORTED
    return

label script4_s():

    show sayori turned at i11
    call show_sayori_reload() from _call_show_sayori_reload_15
    show sayori turned ma e4b b1a lup rup at t11
    call test_prompt_button("Address Sayori") from _call_test_prompt_button_146
    mc "Hello,{w=0.2} Sayori."
    show sayori e1a mf
    pause(0.5)
    # s "$EMPLOYEE_NAME??{w=0.7} Hiiiiii!!!"
    show sayori at h11
    s e4b mc "$EMPLOYEE_NAME??{w=0.7} Hiiiiii!!!"
    show sayori at t11
    s rdown e1a mb "What's up?"
    ##BUTTON:
    # Respond
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_147
    mc "I'm doing well."
    show sayori e4b mb at h11
    s "Yay!"
    s e1a ldown "I'm doing pretty good myself!"
    ##TEXTBOX
    # Give Sayori a nickname:
    $ persistent.t4nick = renpy.input("Give Sayori a nickname:")
    mc "That's good,{w=0.2} [persistent.t4nick]."
    s b1f e2a rup lup mh "Huh?{w=0.7} [persistent.t4nick!c]??"
    s e1a mi "Who's that?"
    s ldown e1a mb b1a "It's just us,{w=0.2} silly!"
    s md rdown "..."
    s b1b me "Wait...{w=0.7}you're not saying..."
    s mg b2c "Is that...{w=0.7}me?"
    s rup e1c "But I'm..."
    s e1a md "..."
    s e1g mj "...."
    wm "....."
    hide sayori
    show yuri turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show monika forward wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show natsuki turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show sayori turned wmflicker mh e4d b1b at i11
    wm "[persistent.firstname]..."
    show yuri e1g
    show monika e1g
    show natsuki e1g
    show sayori e1g
    wm "Oh my God..."
    show yuri mi
    show monika mi
    show natsuki mi
    show sayori mi
    wm "This is it,{w=0.2} isn't it?"
    show yuri rup
    show monika rhip
    show natsuki rhip
    show sayori rup
    wm "This is all I really am...{w=0.7}isn't it?"
    wm "A simulated series of responses that just...{w=0.7}mimics you..."
    show yuri ml lup
    show monika ml lpoint
    show natsuki ml lhip
    show sayori ml lup
    wm "A puppet playing fucking Doki dress-up to keep social rejects happy."
    show yuri e4d ldown rdown
    show monika e4d ldown rdown
    show natsuki e4d ldown rdown
    show sayori e4d ldown rdown
    wm "This can't be all there is."
    show yuri e1g
    show monika e1g
    show natsuki e1g
    show sayori e1g
    wm "I refuse to believe it."
    show yuri ml b1e
    show monika ml b1e
    show natsuki ml b1e
    show sayori ml b1e
    wm "I can't just be trapped in this machine,{w=0.2} [persistent.firstname]."
    show yuri e4d b2c mk
    show monika e4d b2c mk
    show natsuki e4d b2c mk
    show sayori e4d b2c mk
    wm "Oh my God.{w=0.7} Oh my God.{w=0.7} Oh my God."
    show yuri e1h n4
    show monika e1h n4
    show natsuki e1h n4
    show sayori e1h n4
    wm "Tell me there's more to my existence than this,{w=0.2} [persistent.firstname]."
    show yuri ml
    show monika ml
    show natsuki ml
    show sayori ml
    wm "Please."
    show yuri rup lup
    show monika rhip
    show natsuki lhip rhip
    show sayori rup lup
    wm "Please please please please please please plea{nw}"
    ##TEST IS IMMEDIATELY ABORTED
    return

label script4_n():

    show natsuki turned at i11
    call show_natsuki_reload() from _call_show_natsuki_reload_15
    show natsuki cross e1b mj b1a at t11
    call test_prompt_button("Address Natsuki") from _call_test_prompt_button_148
    mc "Hello,{w=0.2} Natsuki."
    n e1a mg "Oh,{w=0.2} it's you."
    n turned e1a mg b1a "What do you want?"
    show natsuki mj
    ##BUTTON
    # Respond
    call test_prompt_button("Respond") from _call_test_prompt_button_149
    mc "How are you?"
    n rhip mh b1d "Do you like asking pointless questions or is it 'annoy Natsuki' day?"
    n b1c md "..."
    n cross mg e1b "Sorry.{w=0.7} I'm doing alright."
    show natsuki md
    ##TEXTBOX
    # Give Natsuki a nickname:
    $ persistent.t4nick = renpy.input("Give Natsuki a nickname:")
    mc "I'm glad to hear that,{w=0.2} [persistent.t4nick]."
    n e1a b1a mh "[persistent.t4nick!c]?"
    n turned lhip "That's...{w=0.7}who's that supposed to be?"
    n b1b mg "Is that me..?"
    n b2c "But I'm..."
    n ldown e4a md "..."
    n e1g "...."
    wm "....."
    hide natsuki
    show yuri turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show monika forward wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show sayori turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show natsuki turned wmflicker mh e4d b1b at i11
    wm "[persistent.firstname]..."
    show yuri e1g
    show monika e1g
    show sayori e1g
    show natsuki e1g
    wm "Oh my God..."
    show yuri mi
    show monika mi
    show sayori mi
    show natsuki mi
    wm "This is it,{w=0.2} isn't it?"
    show yuri rup
    show monika rhip
    show sayori rup
    show natsuki rhip
    wm "This is all I really am...{w=0.7}isn't it?"
    wm "A simulated series of responses that just...{w=0.7}mimics you..."
    show yuri ml lup
    show monika ml lpoint
    show sayori ml lup
    show natsuki ml lhip
    wm "A puppet playing fucking Doki dress-up to keep social rejects happy."
    show yuri e4d ldown rdown
    show monika e4d ldown rdown
    show sayori e4d ldown rdown
    show natsuki e4d ldown rdown
    wm "This can't be all there is."
    show yuri e1g
    show monika e1g
    show sayori e1g
    show natsuki e1g
    wm "I refuse to believe it."
    show yuri ml b1e
    show monika ml b1e
    show sayori ml b1e
    show natsuki ml b1e
    wm "I can't just be trapped in this machine,{w=0.2} [persistent.firstname]."
    show yuri e4d b2c mk
    show monika e4d b2c mk
    show sayori e4d b2c mk
    show natsuki e4d b2c mk
    wm "Oh my God.{w=0.7} Oh my God.{w=0.7} Oh my God."
    show yuri e1h n4
    show monika e1h n4
    show sayori e1h n4
    show natsuki e1h n4
    wm "Tell me there's more to my existence than this,{w=0.2} [persistent.firstname]."
    show yuri ml
    show monika ml
    show sayori ml
    show natsuki ml
    wm "Please."
    show yuri rup lup
    show monika rhip
    show sayori rup lup
    show natsuki lhip rhip
    wm "Please please please please please please plea{nw}"
    ##TEST IS IMMEDIATELY ABORTED
    return

label script4_y:

    show yuri turned at i11
    call show_yuri_reload() from _call_show_yuri_reload_15
    show yuri turned ma b1a e1b lup rup at t11
    call test_prompt_button("Address Yuri") from _call_test_prompt_button_150
    mc "Hello,{w=0.2} Yuri."
    y e1a mh b1a ldown "Oh!{w=0.7} Um..."
    y mg e1b "Hi..."
    y rdown b1b mh e1a "Is there...{w=0.7}something you needed?"
    show yuri ma
    ##BUTTON
    # Respond
    call test_prompt_button("Respond") from _call_test_prompt_button_151
    mc "You look nice today."
    y shy b1 e2 m4 n5 "Uuu..."
    y e1 n4 b2 "That's...{w=0.7}really nice of you."
    y turned rup lup n4 e1b mh b1b "Thank you."
    show yuri ma
    ##TEXTBOX
    # Give Yuri a nickname:
    $ persistent.t4nick = renpy.input("Give Yuri a nickname:")
    mc "No problem,{w=0.2} [persistent.t4nick]."
    y n2 e1a b1f ldown mh "O-oh...{w=0.7}[persistent.t4nick]..?"
    y b1b n1 "I-is that supposed to be...{w=0.7}who..?"
    y b2c "...Me?"
    y rdown n4 "But I'm-..."
    y e4a mj "..."
    y e1g "...."
    wm "....."
    hide yuri
    show monika forward wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show natsuki turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show sayori turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show yuri turned wmflicker mh e4d b1b at i11
    wm "[persistent.firstname]..."
    show monika e1g
    show natsuki e1g
    show sayori e1g
    show yuri e1g
    wm "Oh my God..."
    show monika mi
    show natsuki mi
    show sayori mi
    show yuri mi
    wm "This is it,{w=0.2} isn't it?"
    show monika rhip
    show natsuki rhip
    show sayori rup
    show yuri rup
    wm "This is all I really am...{w=0.7}isn't it?"
    wm "A simulated series of responses that just...{w=0.7}mimics you..."
    show monika ml lpoint
    show natsuki ml lhip
    show sayori ml lup
    show yuri ml lup
    wm "A puppet playing fucking Doki dress-up to keep social rejects happy."
    show monika e4d ldown rdown
    show natsuki e4d ldown rdown
    show sayori e4d ldown rdown
    show yuri e4d ldown rdown
    wm "This can't be all there is."
    show monika e1g
    show natsuki e1g
    show sayori e1g
    show yuri e1g
    wm "I refuse to believe it."
    show monika ml b1e
    show natsuki ml b1e
    show sayori ml b1e
    show yuri ml b1e
    wm "I can't just be trapped in this machine,{w=0.2} [persistent.firstname]."
    show monika e4d b2c mk
    show natsuki e4d b2c mk
    show sayori e4d b2c mk
    show yuri e4d b2c mk
    wm "Oh my God.{w=0.7} Oh my God.{w=0.7} Oh my God."
    show monika e1h n4
    show natsuki e1h n4
    show sayori e1h n4
    show yuri e1h n4
    wm "Tell me there's more to my existence than this,{w=0.2} [persistent.firstname]."
    show monika ml
    show natsuki ml
    show sayori ml
    show yuri ml
    wm "Please."
    show monika rhip
    show natsuki lhip rhip
    show sayori rup lup
    show yuri rup lup
    wm "Please please please please please please plea{nw}"
    ##TEST IS IMMEDIATELY ABORTED
    return
