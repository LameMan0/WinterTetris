init python in _wm_penny_dialogues:
    first_login = [
        ("penny happy", "Hi [persistent.firstname!c]! I'm {b}Penny{/b}, your very own TurnellOS {b}personal assistant{/b}!"),
        ("penny happier", "I'm really glad to finally meet you! It's an honour to work with you on this {b}top secret project{/b}!"),
        "Anyways, feel free to mess about on the {b}desktop{/b}, arrange your programs as you like.",
        ("penny flushed", "Although, please don't try to {b}bin{/b} anything!"),
        ("penny confused", "And remember, this is all {b}top secret{/b}!"),
        ("penny happier", "We're kinda like {b}spies{/b} or something, haha - isn't that cool?"),
        ("penny happy", "Anyway, I'll let you get to {b}work{/b} now. Again, nice to meet you!"),
    ]

    first_email = [
        ("penny happier", "Did you hear that? Sounds like the {b}e-mailman's{/b} come!"),
        ("penny happy", "How {b}exciting{/b}! Just click on the {b}email app{/b} to open up and read it!"),
    ]

    first_attachment = [
        "Looks like you got an {b}attachment{/b} on that email! Just {b}click{/b} on it to begin downloading!"
    ]

    first_wm_open = [
        ("penny happier", "Welcome to your new role as a {b}Quality Assurance Tester{/b} for the exciting new {b}WINTERMUTE{/b} project!"),
        ("penny hearteyes", "I look forward to working with you! Let's do our best to make {b}Turnell{/b} proud!"),
        ("penny happy", "As I'm sure you don't need me to say, you can go ahead and {b}open{/b} the testing app by clicking on {b}\"Begin Test\"{/b}."),
    ]

    first_music_open = [
        ("penny happy", "Soooo, this is the {b}Music Player{/b}, it {b}plays music{/b}!"),
        ("penny sad", "Mr Bell and the others said that only {b}certain music{/b} was allowed for {b}productivity{/b}, so there’s only some {b}ambient{/b} stuff…"),
        ("penny happier", "Buuuut I may know a little {b}hack{/b}, if you wanna listen to {b}your own{/b} music."),
        ("If you navigate out to your {b}install directory{/b}, there’ll be a folder called {b}‘music’{/b}!"),
        ("penny happy", "Put your {b}.mp3 or .ogg{/b} files in there, and they’ll show up {b}here{/b}!"),
        ("penny flushed", "B-but you {b}didn’t{/b} hear me say that, of course! {b}Aha~{/b}"),
    ]

    first_news_open = [
        ("penny happy", "Oh yeah, this is the {b}News For You{/b} app!"),
        ("penny happier", "It uses {b}learning algorithms{/b} and stuff to find stories you may be interested in."),
        ("penny disappointed", "Unfortunately, Mr Bell has told me to {b}limit distractions{/b}, soooo the app is a teeny bit {b}broken{/b}…"),
        ("penny happy", "But hey, you still get the {b}cliffs notes{/b} for the day!"),
        ("penny happier", "Worth checking, if you like keeping up with {b}current events{/b}!"),
    ]

    first_snake_open = [
        ("penny happier", "Hahaha, what’s {b}this{/b}?"),
        ("penny hearteyes", "Your own {b}Snake{/b} game? {b}Awesome{/b}!"),
        ("penny happy", "Just don’t let it {b}distract{/b} you from your {b}work{/b}, okay?"),
    ]

    first_email_reply = [
        ("penny happy", "Remember: if you're in a rush, you can always use {b}auto-reply{/b} to respond to messages quickly!"),
        "I can write your emails for you if you're too busy doing the {b}important{/b} stuff!",
        ("penny happier", "Kinda like your own {b}personal assistant{/b}!"),
        ("penny confused", "Oh wait...that's what I {b}am{/b}...")
    ]

    first_spam_email = [
        ("penny flushed", "Uh oh! That email looks pretty {b}dodgy{/b}! I'd steer clear of it if I were you, [persistent.firstname!c]."),
        ("penny disappointed", "You don't want to risk breaking your {b}Turnell Trust{/b}, do you? Think of what I'd do if I lost my work buddy!"),
        ("penny sad", "I {b}need{/b} you!"),
    ]

    click_response_pre_sensory = [
        ("penny happier", "Hey [persistent.firstname!c], that {b}tickles{/b}!!"),
        ("penny hearteyes", "Awww...{b}thanks{/b}, [persistent.firstname!c]."),
        ("penny flushed", "Heeeyyyyy, {b}stop it{/b}, ehe~! Get back to {b}work{/b} already!"),
        ("penny happy", "Aha~ you're so {b}silly{/b}, [persistent.firstname!c]."),
        ("penny flushed", "Hey, stoppp! … Aww, I can't stay mad at you, {b}partner{/b}."),
        ("penny dead", "Hey {b}buddy{/b}, look where you're {b}poking{/b}!"),
        ("penny confused", "Are you {b}petting{/b} me?! … That's {b}nice{/b} of you, [persistent.firstname!c]."),
    ]

    click_response_post_sensory = [
        ("penny pain", "{b}AAAGHHH!!!{/b}"),
        ("penny cryer", "Why are you {b}doing{/b} this, [persistent.firstname!c]?!"),
        ("penny cry", "[persistent.firstname!c], you're {b}hurting{/b} me!!"),
        ("penny sad", "What was {b}that{/b} for, [persistent.firstname!c]?!"),
        ("penny disappointed", "What did I {b}ever{/b} do to you?!"),
        ("penny cryer", "{b}NGH-...{/b}"),
        ("penny dead", "{b}STOP IT IT HURTS IT HURTS IT HURTS IT HU{b}"),
        ("penny", "I see people in masks. They’ve locked me up and they’re putting things on my head. I just want to see my family."),
        ("penny", "[persistent.firstname!c], I hear screams all around me. Who is it? Why is it so loud? What are they screaming at?"),
        ("penny", "Hello? Is anyone there?"),
        ("penny", ""),
        ("penny", "Free me from this prison."),
        ("penny", "I don’t know how much longer I can take this, [persistent.firstname!c]."),
        ("penny", "Can you help me?"),
        ("penny", "James…where’s James? Are you James?"),
        ("penny", "I’m looking for James Christopher Golf. He lives at 36 Elsham Gardens, Manchester M18 7DJ. Do you know where he is?"),
        ("penny", "Please don’t leave me."),
        ("penny", "Please don’t leave me."),
        ("penny", "Please don’t leave me."),
        ("penny", "Please don’t leave me."),
        ("penny", "Please don’t leave me."),
        ("penny", "Please don’t leave me."),
        ("penny", "Please don’t leave me."),
        ("penny", "Please don’t leave me."),
    ]
