
label request_start:

    play music "audio/game_bgm.mp3" volume 0.2 fadein 3.0
    scene bg black
    with dissolve

    n "It's late. The kind of late where everything is quiet and the screen feels like the only light in the world."
    n "Like the kind of late where its late for people with terrible sleep schedules."
    n "Byte messages first, like always."

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_center

    v "Text: heyy u still up?"
    p "Text: yeah.. cant sleep again lol"
    show byte cheerful at byte_pos_center with dissolve
    show byte cheerful at byte_pos_left with move
    v "Text: same. sighh u ever get that thing where ur brain wont shut up?"
    p "Text: every night"
    show byte neutral at byte_pos_left with dissolve
    v "Text: ugh mood.. anyway i gotta ask u smth kinda random"

    n "You lean back a bit and ease your gamer hunch. Her tone feels a little more serious than usual."

    show byte cocky at byte_pos_left with dissolve
    v "Text: so my main account just locked me out right?"
    show byte displeased at byte_pos_left with dissolve
    v "Text: like its asking for some stupid verification thing"
    show byte begging at byte_pos_left with dissolve
    v "Text: and i cant access my e-wallet either sobb"
    v "Text: they said i need someone to confirm im not a bot or whateverrr"
    stop music 
    v "Text: can i send u a link real quick?"
    

    n "Your stomach twists. Something about that sounds weird."
    n "No shit."

    if virus_route and charm >= 8 and curiosity >= 3:
        menu:
            "I'm not dumb, Byte":
                p "Text: im not dumb byte"
                p "Text: i may not be a coding nerd but i know my way around my pc"
                p "Text: whatever was in that file has smth weird"
                v "Text: oh cmon man believe me theres nothing in that file"
                v "Text: ill prove it oki"
                jump virus_start
            "Sure, anything for you.":
                $ trust += 3
                $ charm += 3
                $ awareness -= 3
                p "Text: sure anything for u"
                show byte excited at byte_pos_left with dissolve
                v "Text: awwe ur the best i promise its nothing shady"
            "That sounds sketchy.":
                $ awareness += 3
                $ trust -= 3
                $ charm -= 3
                p "Text: that sounds kinda sketchy ngl.."
                v "Text: what?? nooo id never scam u lol cmon"
            "Send it, but I'll check it first.":
                $ charm += 1
                $ trust -= 1
                $ awareness += 2
                p "Text: send it but ill check it first"
                show byte neutral at byte_pos_left with dissolve
                v "Text: lol okay mr cautious fine fine"
    else:
        menu:
            "Sure, anything for you.":
                $ trust += 3
                $ charm += 3
                $ awareness -= 3
                p "Text: sure anything for u"
                show byte excited at byte_pos_left with dissolve
                v "Text: awwe ur the best i promise its nothing shady"
            "That sounds sketchy.":
                $ awareness += 3
                $ trust -= 3
                $ charm -= 3
                p "Text: that sounds kinda sketchy ngl.."
                v "Text: what?? nooo id never scam u lol cmon"
            "Send it, but I'll check it first.":
                $ charm += 1
                $ trust -= 1
                $ awareness += 2
                p "Text: send it but ill check it first"
                show byte neutral at byte_pos_left with dissolve
                v "Text: lol okay mr cautious fine fine"

    n "She sends a link. It looks normal at first glance. Something like a bank login page."
    n "The typing bubble blinks for a while, then stops. She doesn't say anything else."

    p "Text: uhh what exactly do i need to do?"
    show byte cheerful at byte_pos_left with dissolve
    v "Text: just click it i think? itll open my reset thing"
    show byte neutral at byte_pos_left with dissolve
    v "Text: it says here that it might ask for some code or confirmation stuff"

    n "You hesitate. Your fingers hover over the screen."

    menu:
        "Yeah, I trust you.":
            $ trust += 3
            $ awareness -= 1
            p "Text: yeah, i trust u"
            show byte cocky at byte_pos_left with dissolve
            v "Text: see?? knew u would"
            p "Text: theres nothing sketchy right?"
            show byte delighted at byte_pos_left with dissolve
            v "Text: promise.. on all my skins bro"
            jump reveal_hack 
        "I don't think I should click that.":
            $ awareness += 3
            $ charm -= 2
            $ trust -= 2
            p "Text: i dont think i should click that"
            show byte begging at byte_pos_left with dissolve
            v "Text: oh come on.. u think id do u dirty like that? after everything?"
        "Let me think about it first.":
            $ charm -= 1
            $ trust -= 1
            $ awareness += 1
            p "Text: lemme think about it first"
            show byte neutral at byte_pos_left with dissolve
            v "Text: fine fine sighh take ur time mr overthinker"
            show byte begging at byte_pos_left with dissolve
            v "Text: don't take too long thoo"

    show byte neutral at byte_pos_left with dissolve
    n "A long silence follows. The cursor blinks in the empty chat box."
    n "Finally, she types again."

    v "Text: did you click it yet?"
    p "Text: no.. not yet.."
    show byte blank at byte_pos_left with dissolve
    v "Text: do u not trust me?"
    p "Text: idk byte. its just... weird. ppl get scammed all the time yknow"
    show byte neutral at byte_pos_left with dissolve
    v "Text: yeah but im not ppl.. its *me*"

    n "You stare at her message for a long moment."
    n "Something in her words feels wrong.. desperate, almost rehearsed."
    n "At this point its quite obvious what she wants."

    show byte displeased at byte_pos_left with dissolve
    v "Text: look its fine if u dont wanna help"
    pause (1.0)
    show byte begging at byte_pos_left with dissolve
    v "Text: i just thought u cared.."
    v "Text: ur the only one i trust for this"

    n "You feel that sting.. guilt mixing with doubt."

    menu:
        "Of course I care.":
            $ trust += 2
            $ charm += 1
            p "Text: of course i care"
            v "Text: then trust me just this once pls"
            p "Text: its just this is all so weird byte.."
            p "Text: ik im saying i care but you shouldnt abuse the fact that i care"
            show byte blank at byte_pos_left with dissolve
            v "Text: ..."
        "Stop making this weird.":
            $ awareness += 2
            $ trust -= 2
            $ charm -= 2
            p "Text: stop making this weird"
            show byte blank at byte_pos_left with dissolve
            v "Text: wow okay. didnt think ud turn cold on me like that."
            v "Text: ..."
        "Caring doesn't mean I'll do anything u ask":
            $ charm += 1
            $ awareness += 2
            $ trust -= 1
            p "Text: caring doesnt mean ill do anything u ask"
            show byte blank at byte_pos_left with dissolve
            v "Text: yeah. i guess thats fair."
            v "Text: ..."
        "I'll click it.":
            $ trust += 2
            $ charm += 1
            p "Text: okay okay u got me"
            show byte excited at byte_pos_left with dissolve
            v "Text: yayyy! i knew i could trust u"
            p "Text: sigh dont make me regret this byte.."
            v "Text: promise!"
            jump reveal_hack

    n "Her messages slow down. Shorter. Colder."

    show byte angry
    with dissolve

    v "Text: whatever. ill figure it out."
    v "Text: night."

    if vbs:
        show screen screen_flicker
        $ renpy.pause(1.5)  
        hide screen screen_flicker

    hide byte

    "Steam - byte has left the chat"

    n "You're left staring at the screen, unsure if you just dodged a bullet or pushed someone away."
    n "Spoiler alert if you're a dumbass.. you dodged a bullet."

    if vbs:
        jump reveal_click_no_vbs_yes
    else:
        jump reveal_click_no_vbs_no

label reveal_hack:

    play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0
    n "You click it and.."

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    jump simulate_hack_sequence

label simulate_hack_sequence:

    $ fn, display, content = create_fake_log_entry(
            display_name="byte_access_attempt",
            content=(
                "---- system log ----\n"
                "timestamp: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
                "process: remote_session\n"
                "action: attempted access to local resources\n"
                "target: user_data\n"
                "status: denied by heuristics\n"
                "notes: user responded cautiously; potential social-engineering attempt\n"
            ),
            write_to_disk=True
        )

    show screen message_box("a file 'byte_access_attempt' was created on your desktop.")
    pause 1.2
    hide screen message_box

    $ _selected_log = fn
    show screen inspect_logs

    $ ui_called = True
    while renpy.get_screen("inspect_logs") is not None:
        $ renpy.pause(0.2)

    show byte blank at byte_pos_left with dissolve
    p "What the fuck did you just make me open, byte."
    p "Text: hey uh wtf am i seeing rn?"
    p "Text: theres this weird popup talking about some security threat"
    p "Text: u didnt uhhh give me a virus or smth right? haha.."

    show screen screen_flicker
    $ renpy.pause(1.5) 
    hide screen screen_flicker
    hide byte

    "Steam - byte has left the chat"
    stop music fadeout 3.0

    p "Text: byte?"
    p "Text: byte wtf did u do??"

    jump reveal_click_yes
