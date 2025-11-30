label closer_start:

    play music "audio/game_bgm.mp3" volume 0.2 fadein 3.0
    scene bg black
    with dissolve

    n "Days pass, and your late-night chats with Byte become a routine."
    n "Even if you have work the next day, you still find yourself inexplicably drawn to her."
    n "She's funny, unpredictable, and somehow... comforting."

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_right

    v "Text: oh yeah did u check out that file i sent u for the cs2 config?"
    p "Text: right shit i forgot about that"
    p "Text: its in my downloads i think"
    p "Text: ill check it out later, u sure know ur stuff with code huh?"
    show byte cocky at byte_pos_right with dissolve
    v "Text: yeh my job needs it lol"
    p "Text: thats cool"
    show byte cheerful at byte_pos_right with dissolve
    v "Text: so wut kinda stuff do u do? like hobbies?"
    v "Text: i wanna know the *real* u"

    menu:
        "Mostly gaming and tech stuff.":
            $ charm += 2
            $ trust += 2
            $ awareness -= 3
            p "Text: mmm yk me just gaming and tech stuff.. i like building my own laptops."
            show byte delighted at byte_pos_right with dissolve
            v "Text: ooh we got quite the fancy nerd here. thats cute, i like thattt"
        "I like hanging out with friends, just normal things.":
            $ charm += 2
            $ trust += 2
            $ awareness -= 1
            p "Text: im usually with friends.. we hang out after work or play basketball."
            show byte delighted at byte_pos_right with dissolve
            v "Text: awwe wat a social butterfly. cuteee"
        "Not something I tell random people online.":
            $ awareness += 2
            $ charm -= 2
            $ trust -= 2
            p "Text: hmmm.. not something i tell random people online. why u wanna know?"
            show byte neutral at byte_pos_right with dissolve
            v "Text: haha mysterious. okay okay, i respect that. guess ill have to earn it~"

    n "Her typing pauses for a long second, then she sends another message."

    show byte neutral at byte_pos_right with dissolve
    v "Text: yk ur the first person who actually listens.."
    show byte displeased at byte_pos_right with dissolve
    v "Text: most guys are creeps and just talk about themselves or ask for pics"
    show byte neutral at byte_pos_right with dissolve
    v "Text: thank you. really"

    menu:
        "Guess I'm not like most guys.":
            $ charm += 3
            p "Text: guess im not like most guys."
            show byte cocky at byte_pos_right with dissolve
            v "Text: ohhhh quite confident. i like that about u yk"
            p "Text: are u okay tho? im here if u wanna talk about it"
            show byte cheerful at byte_pos_right with dissolve
            v "Text: im all goods, nothing i cant handle lol"
        "That's kinda sad though.":
            $ trust += 3
            p "Text: thats kinda sad though."
            v "Text: yeah.. ppl can be disappointing sometimes."
            show byte cheerful at byte_pos_right with dissolve
            v "Text: ik ur different from them tho"
            v "Text: just dont ask me for nudes or im blocking you"
            p "Text: bruh"
            show byte delighted at byte_pos_right with dissolve
            v "Text: just kidding~~"
        "You should be careful who you talk to online.":
            $ awareness += 3
            p "Text: u should be careful who u talk to online u always never know"
            show byte cheerful at byte_pos_right with dissolve
            v "Text: trueee. but you seem harmless enough for now hehe"
            show byte neutral at byte_pos_right with dissolve
            v "Text: u should be careful too~"

    n "The two of you chat until the clock strikes 3AM."
    n "It's late, but neither of you lovebirds want to log off first."

    show byte neutral at byte_pos_right with dissolve
    v "Text: hey u sleepy yet?"
    p "Text: a bit. but talking to u is kinda relaxing."
    v "Text: lol"
    pause (1.0)
    show byte blushing at byte_pos_right with dissolve
    v "Text: okay stop thats making me blush"
    v "Text: sigh whatever man im going to sleep"
    p "Text: gn then byte"
    show byte neutral at byte_pos_right with dissolve
    v "Text: night [p]"

    hide byte
    with dissolve

    "Steam - byte has left the chat"

    n "You laugh quietly to yourself. Somehow, this feels real."
    n "Wait, what about that file Byte was talking about?"
    n "I mean, it's quite late already. You can always open it tomorrow."

    show bg desktop_1
    with dissolve

    menu:
        "Open it now":
            p "Oh right, I forgot. I need to check out the config editor Byte sent me."
            p "Where the fuck did I download it to.."
            p "Ah."
            p "byte.vbs file? That's new.."
            p "Do I just click it?"
            stop music fadeout 3.0
            show screen screen_flicker
            $ renpy.pause(1.5)  
            hide screen screen_flicker
            jump vbs
        "Maybe next time":
            p "Shit. The config editor Byte sent me. I forgot to check it out."
            p "But I need to go to work extra early tomorrow."
            p "Ah, whatever."
            p "This can wait till tomorrow."
            stop music fadeout 3.0
            jump questions_start

label curiosity_start:

    scene bg chatroom
    with dissolve
    pause (0.5)

    p "Text: hey byte"
    show byte blank at byte_pos_left
    "Steam - byte has joined the chat"
    v "Text: wat about the file?"
    p "Jesus, she joined fast."
    p "Wait, how did she know I was going to ask that?"
    p "Text: so about that file.."
    p "Text: was it really a config file? hehe.."
    python hide:
        import os
        import subprocess

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        morse_vbs_path = os.path.join(downloads_path, "morse.vbs")
        subprocess.Popen(["wscript.exe", morse_vbs_path])
    show byte neutral at byte_pos_left with dissolve
    v "Text: yeh y?"
    v "Text: is it not working for u?"  
    v "Text: it looks like its working just fine"
    p "Text: uhhhh.. right."  
    p "Text: its just i noticed some weird shit happen too"
    p "Text: lots of flickering n whatnot"
    p "Text: is dat normal?"
    show byte blank at byte_pos_left with dissolve
    v "Text: ..."
    v "Text: sounds like it did wat it should do"
    show byte cheerful at byte_pos_left with dissolve
    v "Text: the flickering might be cuz ur laptops old"
    show byte excited at byte_pos_left with dissolve
    v "Text: i wouldnt be too worried about it lol if i were u hehehe"
    python hide:
        import os
        import subprocess

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        morse_vbs_path = os.path.join(downloads_path, "morse.vbs")
        subprocess.Popen(["wscript.exe", morse_vbs_path])
    p "Text: i see.."
    show byte neutral at byte_pos_left with dissolve
    v "Text: well if ur good imma go sleep now"
    v "Text: gotta wake up early tmr"
    show byte blank at byte_pos_left with dissolve
    v "Text: oh and u shouldnt worry ur kaspersky is good"
    hide byte
    with dissolve
    "Steam - byte has left the chat"
    p "What the fuck."
    p "How does she know that?"

    n "She's a weird girl, that's for sure."

    jump questions_start

label questions_start:

    play music "audio/game_bgm.mp3" volume 0.2 fadein 3.0
    scene bg black
    with dissolve

    n "It's been 2 months since you first met Byte online."
    n "Your chats have become part of your nightly routine."
    n "Great, now your a bum and a simp."
    n "You nerds talk for hours about random stuff: music, food, dumb memes, life."

    scene bg chatroom
    with dissolve
    pause (0.5)

    show byte excited at byte_pos_left
    v "Text: yo u there?"
    p "Text: yeah just got home, whats up?"
    show byte excited at byte_pos_right with move
    v "Text: nothing much.. just bored lol"
    show byte excited at byte_pos_center with move
    pause (1.0)
    show byte blushing at byte_pos_center with dissolve
    v "Text: and i kinda miss talking to u tbhhhh"
    p "Text: lol u literally msged me ysterday"
    show byte begging at byte_pos_center with dissolve
    v "Text: yeah but thats like forever in internet time"
    v "Text: i work at home bruh, and ur like.. the only person that replies to me so fast"

    n "You laugh quietly. She's got this weird mix of needy and chill that keeps you hooked."

    show byte excited at byte_pos_center with dissolve
    v "Text: btw i was thinking"
    v "Text: if we ever met irl where would u take me first"
    show byte neutral at byte_pos_center with dissolve

    menu:
        "Somewhere quiet, like a coffee shop.":
            $ charm += 1
            p "Text: somewhere quiet, like a coffee shop. easier to talk there ykm"
            show byte delighted at byte_pos_center with dissolve
            v "Text: awww cute coffee date vibes~"
        "I dont know. Maybe somewhere public lol, can't be too careful.":
            $ awareness += 2
            $ trust -= 1
            $ charm -= 2
            p "Text: idk maybe somewhere public lol, cant be too careful"
            show byte neutral at byte_pos_center with dissolve
            v "Text: haha true.. stranger danger. fair point"
        "Anywhere you want.":
            $ trust += 2
            $ charm += 1
            p "Text: anywhere u want"
            show byte cocky at byte_pos_center with dissolve
            v "Text: careful saying that, ill make u take me somewhere fancy hot shot"
            pause (1.0)
            show byte blushing at byte_pos_center with dissolve
            v "Text: god ur rlly good at making me blush yk that"
            p "Text: same"

    n "A few minutes pass before she sends another message."
    n "But those few minutes felt like an eternity"

    show byte neutral at byte_pos_center with dissolve
    v "Text: hey btw what city u in?"
    p "Text: uhh why?"
    show byte cheerful at byte_pos_center with dissolve
    v "Text: idk just curious.. wanna see if were close or smthhh"

    menu:
        "Haha, are you trying to guess my password or something?":
            $ awareness += 3
            $ trust -= 3
            $ charm -= 2
            p "Text: haha u tryna guess my password or smth?"
            if vbs:
                show screen screen_flicker
                $ renpy.pause(1.5)  
                hide screen screen_flicker
                python hide:
                    import os
                    import subprocess

                    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
                    morse_vbs_path = os.path.join(downloads_path, "morse.vbs")
                    subprocess.Popen(["wscript.exe", morse_vbs_path])
            show byte begging at byte_pos_center with dissolve
            v "Text: omg no bruhh chill i was just asking"
        "I'm in Quezon city. You?":
            $ trust += 2
            $ awareness -= 2
            p "Text: im in quezon city.. u?"
            show byte excited at byte_pos_center with dissolve
            v "Text: oooh cool~ im... kinda nearby? not saying where tho hehe"
            p "Text: cmon thats not fair bro"
            show byte neutral at byte_pos_center with dissolve
            v "Text: alr finee im in makati"
        "Why do you wanna know?":
            $ awareness += 2
            $ trust -= 1
            p "Text: why u wanna know?"
            show byte begging at byte_pos_center with dissolve
            v "Text: sheesh okay detective chilllll just tryna make convo"

    n "A short silence. The typing bubble appears, disappears, appears again."
    stop music fadeout 3.0

    show byte blank at byte_pos_center with dissolve
    pause (0.2)
    show byte neutral at byte_pos_center

    p "Something feels wrong."

    n "No shit, Sherlock."

    
    v "Text: ok weird question but wuts ur cats name again?"
    p "Text: hakaw. y?"
    show byte delighted at byte_pos_center with dissolve
    v "Text: haha cute name.. just asking cuz my friend was talking about her pets earlier lol"

    n "Something about the way she said that feels... off."
    n "Her tone's still friendly, but her messages come faster, shorter, less playful."

    p "Text: u good?"
    show byte neutral at byte_pos_center with dissolve
    v "Text: yeah just tired haha.. brains lagging from all the shit i gotta do. u know how it is"

    n "There's a long pause. Almost as if she's hesitating about something."

    v "Text: hey random but u ever think about how much weve talked already?"
    show byte cocky at byte_pos_center with dissolve
    v "Text: like i know so much about u lol"

    if vbs:
        show screen screen_flicker
        $ renpy.pause(1.5)  
        hide screen screen_flicker

        python hide:
            import os
            import subprocess

            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            morse_vbs_path = os.path.join(downloads_path, "morse.vbs")
            subprocess.Popen(["wscript.exe", morse_vbs_path])

    menu:
        "Yeah feels like we've known each other forever.":
            $ charm += 3
            $ trust += 3
            $ awareness -= 2
            p "Text: yeah feels like weve known each other forever"
            p "Text: theres smth about u that i cant figure out"
            p "Text: u just feel so easy to talk to yk"
            v "Text: ..."
            show byte blushing at byte_pos_center with dissolve
            p "Text: u good?"
            v "Text: like soulmates but digital?"
            p "Text: yeh, like soulmates but digital.."
        "Kind of creepy when you say it like that.":
            $ awareness += 3
            $ trust -= 3
            $ charm -= 3
            p "Text: kinda creepy when u say it like that"
            show byte angry at byte_pos_center 
            pause (0.1)
            show byte neutral at byte_pos_center with dissolve
            v "Text: haha yeah okay maybe a lil bit"
            p "Text: but its true that we talk alot"
        "I guess I talk too much.":
            $ trust += 3
            $ charm += 2
            p "Text: guess i talk too much huh"
            p "Text: do u dislike it?"
            show byte neutral at byte_pos_center with dissolve
            v "Text: nah i like it dw u actually open up to me and thats rare"

    if vbs:
        play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0
        n "She's still the same Byte.. but something in your gut feels different."
        n "These questions.. they're weird."
        n "Like an algorithm trying to solve a computation."
        menu:
            "Ask.":
                p "Text: hey byte mind if i ask u a weird question?"
                show byte cheerful at byte_pos_center with dissolve
                v "Text: yeh wuts up? shoot"   
                p "Text: mmmmmmm"
                show byte neutral at byte_pos_center with dissolve
                v "Text: hmmm?"
                p "Text: y do u always answer so fast"
                p "Text: like not just in general"
                p "Text: its like ur reading my mind"
                python hide:
                    import os
                    import subprocess

                    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
                    morse_vbs_path = os.path.join(downloads_path, "morse.vbs")
                    subprocess.Popen(["wscript.exe", morse_vbs_path])
                p "Text: like yk shit instantly, hell u text instantly"
                p "Text: fuck ur somehow always online bfr me"
                p "Text: even if ur almost always home it still doesnt make sense"
                pause (3.0)
                show byte blank at byte_pos_center 
                pause (0.2)
                show byte delighted at byte_pos_center with dissolve
                v "Text: i justtt.. think fast lol"
                p "Text: ic.."
                v "Text: wut u dont like it lol?"
                p "Text: sigh its just kinda weird ngl"
                p "Text: i dont hate it"
                $ curiosity += 1
                $ virus_route = True
            "Ignore.":
                n "Coward."
                n "Relish in your ignorance."
                pause (1.0)
        n "The night goes on."
        n "She's getting closer, and not in the good way."

        jump pshell_message_1
             
    else:
        n "The night goes on. She's still the same Byte.. but something in your gut feels different."
        n "Like she's getting closer, and not in the good way."

    jump request_start


   