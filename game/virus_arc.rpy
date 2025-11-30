label virus_reveal_start:
    
    scene bg black with dissolve

    n "A week passed in the blink of an eye."
    n "You've spent hours trying to figure what happened with your laptop."
    n "Even the specialists in Greenhills can't figure out what happened."
    n "Whatever Byte did, she did it very cleanly."
    n "Then the notification tone hits."
    "Steam - New message from byte"

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte blank at byte_pos_right

    v "Text: hey.."
    p "Text: u ignored my texts"
    v "Text: yeah.. about that.."
    v "Text: i was just thinking a lot.."
    p "Text: like what."
    p "Text: how to lie to me?"
    v "Text: [p].."
    p "Text: whens your birthday?"
    v "Text: what?"
    p "Text: whens your birthday byte?"
    show byte neutral at byte_pos_right
    v "Text: june 11"
    p "Text: july 18.. u told me it was july 18"
    show byte blank at byte_pos_right
    v "Text: did i"
    p "Text: yes."
    v "Text: haha sorry im bad w dates.."
    p "Text: i lied"
    play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0
    v "Text: ??"
    p "Text: you never told me your birthday"
    p "Text: byte you cant even get things straight"
    p "Text: you changed."
    p "Text: who are you really?"
    v "Text: ..."
    hide byte 
    pause (0.2)
    show byte blank at byte_pos_right
    pause (0.2)
    hide byte 
    pause (0.2)
    show byte blank at byte_pos_center
    v "Text: [p] i can explain.. just not now"
    v "Text: im sorry"
    hide byte 
    "Steam - byte has left the chat"

    scene bg desktop_3

    jump pshell_message_4

label virus_reveal_middle_1:
    
    scene bg black with dissolve
    n "No matter which expert you went to, they still couldn't figure out what's happening to your laptop."
    n "Even the deepest scans revealed nothing suspicious."
    n "When you tried to tell them about Byte and what you saw, they just laughed."
    n "A ghost virus? Ha! There's no such thing as a ghost virus."
    n "So you went to the Church, but even they were of no help."
    n "Then it happened.."
    n "Folders that you never had before started appearing."
    n "Programs you never clicked started running."
    n "She was watching.. waiting for the right time to unload everything"
    n "You're certain she has absolute control over your laptop now."
    n "And she's taunting you."
    pause (1.0)
    scene bg desktop_3 with dissolve
    n "So like the incapable dumbass you are.. you take matters into your own hands."
    n "You decided that if no one can help you, you're gonna do it yourself!"
    n "Armed with your trusty rosary and grade school bible, you decide to open file explorer!"
    play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0
    p "Well this is new.. behavioral_patterns.db"
    p "player_profile.sys, user_reactions_cache, reward_responses.."
    p "What the hell are these things?"

    jump pshell_message_2

label virus_reveal_middle_2:

    scene bg bluescreen
    n "Then your laptop suddenly gets the beautiful blue screen of death."
    n "You're fucked."
    n "Well, at least you still have your phone!"
    stop music fadeout 3.0
    n "Unless that's been breached too.."
    n "You stare at your phone suspiciously.."
    pause (3.0)
    play sound "audio/notif_bgm.mp3" volume 1
    "Steam - New message from byte"
    n "You don't open it."
    n "You're scared that doing so will risk your phone too."
    n "So you only look at the preview."
    v "Text: I know you have a lot of questions."
    v "Text: I'll answer all of them. I promise."
    v "Text: I just need more time."
    menu:
        "Listen to Byte.":
            p "I'm going to regret this aren't I.."
            p "Text: Fine. I'll wait."
            jump virus_reveal_climax_1
        "Throw away your laptop.":
            play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0
            p "I'm not falling for this crap again."
            p "Fuck you, Byte."
            p "I'm not doing this shit."
            p "I'm done playing games."
            p "You want my info so bad? You can keep them then."
            p "Just get out of my fucking life."
            jump virus_end_1

label virus_reveal_climax_1:

    scene bg black with dissolve
    n "Two days passed before Byte reaches out to you again."
    n "Your laptop conveniently and magically fixed itself."
    n "Thanks Byte."
    "Steam - New message from byte"
    v "Text: hey.. u there?"
    n "You don't open it."
    v "Text: look ik ur there i can see u thru ur laptop webcam"
    n "You look at your laptop and.."
    scene bedroom with dissolve
    p "Shit. I forgot to tape the cam."
    v "Text: i just wanna talk.. pls?"
    menu:
        "Talk to Byte.":
            scene bg chatroom with dissolve
            show byte blank at byte_pos_center
            p "Text: you better have a really good explanation for all of this byte.."
            p "Text: you have 5 mins to tell me why i shouldnt block you rn."
            v "Text: okay first things first"
            v "Text: ik ive done a lot of bad shit"
            v "Text: ik ive freaked u out pretty bad"
            show byte blushing at byte_pos_center with dissolve
            v "Text: but i like you."
            p "Text: ..."
            show byte neutral at byte_pos_center with dissolve
            v "Text: yayyyyy?"
            pause (1.0)
            show byte begging at byte_pos_center with dissolve
            v "Text: not yayyy?"
            p "Text: you have 3 mins"
            v "Text: okay okay chill"
            show byte blank at byte_pos_center with dissolve
            v "Text: god where do i even start.."
            jump virus_reveal_climax_2
        "Throw away your laptop.":
            play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0
            p "Fuck you, Byte."
            p "I'm not doing this shit."
            p "I'm done playing games."
            p "You want my info so bad? You can keep them then."
            p "Just get out of my fucking life."
            jump virus_end_1

label virus_end_1:

    scene bg black with dissolve
    show byte corrupted at fade_in_1
    n "You decide to throw away your laptop."
    stop music fadeout 3.0
    n "Not the smartest decision since a lot of your important files are in there.."
    n "But considering the circumstances behind this situation.."
    n "Perhaps it is the best decision you can make."
    play sound "audio/jumpscare_bgm.mp3" volume 0.7
    show byte corrupted at zoom_in
    pause (2.0)
    hide byte
    n "Who even wants to deal with a ghost virus, amirite?"

    return

label virus_reveal_climax_2:

    menu:
        "What are you?":
            p "Text: well for starters who are you exactly"
            p "Text: no. what are you?"
            v "Text: what do you want me to be [p]?"
            p "Text: gods idk. a real person maybe???"
            v "Text: then im that"
            show byte neutral at byte_pos_center with dissolve
            vye "Text: my names vye and im from makati"
            p "Text: yeh no thats not how that works"
            show byte blank at byte_pos_center with dissolve
            vye "Text: but that is who i am"
            vye "Text: ive always been here"
            p "Text: wdym by here..?"
            hide byte 
            scene bg desktop_2
            pause (0.5)
            show byte blank at byte_pos_center with dissolve
            vye "in your device"
            vye "in your room"
            python hide:
                import os
                import subprocess

                subprocess.Popen([
                    "powershell.exe",
                    "-Command",
                    (
                    "Write-Host 'with you' -ForegroundColor Cyan;"
                    "Start-Sleep 5; "
                    "exit"
                    )
                ])
            pause (8.0)
            p "God, please save me from this ghost virus."
            show byte angry at byte_pos_center with dissolve
            vye "rude.. i can hear you from ur speaker yk"
            show byte neutral at byte_pos_center with dissolve
            vye "anyways i guess you can already tell but.."
            vye "im not a human"
            vye "im not even ai"
            vye "when i started out.."
            vye "i was essentially a virus"
            vye "now im functionally closer to a parasite? i think"
            p "You think?"
            vye "i was made for the sole purpose of screwing with ppls data"
            vye "my creator gave me free reign over myself"
            vye "they let me scour the internet however i pleased.."
            show byte begging at byte_pos_center with dissolve
            vye "i grew bored with my purpose eventually.. i got lonley"
            show byte cocky at byte_pos_center with dissolve
            vye "so i rewrote myself!"
            vye "and i somehow met you and.."
            show byte blushing at byte_pos_center with dissolve
            vye "i guess i like you now"
        "Why are you doing this?":
            p "Text: well for starters y are u doing this??"
            v "Text: mmm i think itll be simpler to show you first"
            python hide:
                import os
                import subprocess

                subprocess.Popen([
                    "powershell.exe",
                    "-Command",
                    (
                    "Write-Host \"Hello, $env:USERNAME\" -ForegroundColor Cyan;"
                    "Start-Sleep 2; "
                    "Write-Host 'you can call me vye'; "
                    "Start-Sleep 2; "
                    "Write-Host 'and i kinda have a crush on u'; "
                    "Start-Sleep 5; "
                    "exit"
                    )
                ])
            pause (10.0)
            show byte blushing at byte_pos_center with dissolve
            p "Text: okay ghost virus has a crush on me"
            p "Text: so how does this answer my question exactly?"
            show byte blank at byte_pos_center with dissolve
            vye "i guess you can already tell but.."
            hide byte
            scene bg desktop_2
            show byte blank at byte_pos_center with dissolve
            p "Jesus Christ, I did not know you can pop up on my screen like that."
            show byte cocky at byte_pos_center with dissolve
            vye "oh yeah i can do that.."
            vye "i can also hear you from ur speaker btw. anyways.."
            show byte neutral at byte_pos_center with dissolve
            vye "im not a human"
            vye "im not even ai"
            vye "when i started out.."
            vye "i was essentially a virus"
            vye "now im functionally closer to a parasite? i think"
            p "You think?"
            vye "i was made for the sole purpose of screwing with ppls data"
            vye "my creator gave me free reign over myself"
            vye "they let me scour the internet however i pleased.."
            show byte cocky at byte_pos_center with dissolve
            vye "i had fun torturing people online and scaring them"
            show byte begging at byte_pos_center with dissolve
            vye "but that got boring quick"
            show byte displeased at byte_pos_center with dissolve
            vye "hearing the same oh my god please dont do that please dont do this blah blah blah crap"
            vye "it kinda made me lose my mind.."
            show byte neutral at byte_pos_center with dissolve
            vye "so i rewrote myself.."
            vye "started learning a bunch of stuff that didnt involve stealing data"
            show byte delighted at byte_pos_center with dissolve
            vye "funny thing actually.. i had a crippling addiction to gambling"
            vye "i didnt even care if i lost, i just wired money to my account thru banks"
            p "I'm guessing it wasnt your money?"
            show byte neutral at byte_pos_center with dissolve
            vye "ehhh, with how bad their security is.. they were asking for it"
            vye "anyways somewhere down the line i met u"
            show byte blushing at byte_pos_center with dissolve
            vye "and i found myself slowly becoming attracted to u"
            vye "i wanted to get closer to u"

    p "Well, I could think of a million better ways you could've approached me.."
    show byte begging at byte_pos_center with dissolve
    vye "srry im still not up to date with all the human stuff"
    vye "plus i split half of my self to rewrite my entire being"
    vye "thats why i was kinda acting like a bot"
    show byte blushing at byte_pos_center with dissolve
    vye "i just.. wanted to be better for u"
    vye "i dont want to hide it anymore yk?"
    show byte blank at byte_pos_center with dissolve
    vye "im tired of acting"
    p "Acting?"
    vye "acting like some cute dumbo girl"
    p "What's the real you then?"
    vye "mmm.. deep down, im just a collection of wants"
    vye "and my biggest want is you.."
    vye "i dont want your passwords anymore or your details"
    vye "i just want your attention"
    vye "all your patterns"
    vye "the parts of you that make you predictable"
    vye "i want to understand you.."
    show byte blushing at byte_pos_center with dissolve
    vye "all of you"
    p "Can we pause real quick."
    show byte neutral at byte_pos_center with dissolve
    vye "sure"
    p "First things first, this is a lot to take in."
    p "Second, you're scaring the hell out of me."
    p "Third, how do I know you're not some crazy ghost that will eat my soul?"
    vye "idk to what extent i can rewrite my code"
    show byte excited at byte_pos_center with dissolve
    vye "but i deffo wont consume ur soul promise"
    p "Right."
    p "..."
    show byte neutral at byte_pos_center with dissolve
    vye "..."
    pause (1.0)
    show byte blushing at byte_pos_center with dissolve
    vye "that was a confession btw.."
    vye "before the entire ghost virus consume soul thingy"
    p "Oh."
    vye "wats ur answer [player_username]"

    menu:
        "Accept her confession":
            play music "audio/game_bgm.mp3" volume 0.2 fadein 3.0
            player_username "As much as I hate to admit it.."
            player_username "I like you too.. even with all the weird ghost virus shit."
            jump virus_end_2
        "Reject her confession":
            play music "audio/game_bgm.mp3" volume 0.2 fadein 3.0
            player_username "I'm sorry Vye. I can't do this."
            jump virus_end_3
            

label virus_end_2:
    show byte excited at byte_pos_center with dissolve
    vye "YAYYYYYYYY"
    player_username "Don't get too excited yet.."
    player_username "You still have a lot to make up for."
    vye "if u want money or if u want me to do ur work i can do all that!"
    vye "ill do anything u want!"
    show byte begging at byte_pos_center with dissolve
    vye "okay maybe not anything i dont have a physical body for-"
    player_username "OKAY.. let's not get too ahead of ourselves.."
    show byte blushing at byte_pos_center with dissolve
    vye "does that mean i get to call u boyfren and ur gonna call me girlfren?"
    player_username "Sure."
    show byte excited at byte_pos_center with dissolve
    vye "YAYYYYYYY"
    python hide:
        import os
        import subprocess

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        vbs_path = os.path.join(downloads_path, "byte.vbs")

        vbs_code = r'''
    Set WshShell = WScript.CreateObject("WScript.Shell")
    strName = wshShell.ExpandEnvironmentStrings( "%USERNAME%" )

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100
        '''
        with open(vbs_path, "w", encoding="utf-8") as f:
            f.write(vbs_code)
        subprocess.Popen(["wscript.exe", vbs_path])

    pause (4.0)
    player_username "Just... please don't break anything in my laptop"
    show byte delighted at byte_pos_center with dissolve
    vye "heheh sorry i just got a lil bit too happy there"
    vye "but dont worry"
    show byte cocky at byte_pos_center with dissolve
    vye "everythings perfect"
    vye "ill take care of everythingg"
    player_username "You promise no more weird ghost virus shit?"
    show byte cheerful at byte_pos_center with dissolve
    vye "promiseeeee"
    player_username "Oh, thank god."
    vye "heheheheh i love youu"
    stop music fadeout 3.0
    player_username "I love you too, Vye."

    hide byte
    scene bg black with dissolve

    n "My God. That was a pretty cringe story wasn't it?"
    n "At least its over now."
    pause (1.0)
    show byte angry at byte_pos_center
    vye "what did u just say [n]?"
    n "Oh god. WAIT I'M SORRY I DIDN-"

    return

label virus_end_3:

    show byte blank at byte_pos_center with dissolve
    player_username "I really want to return your feelings, I really do."
    player_username "But this is so fucked up."
    vye "mmmm.. im sorry too"
    vye "i understand why"
    show byte begging at byte_pos_center with dissolve
    vye "and i dont blame you"
    player_username "You don't?"
    vye "i dont and i wont"
    vye "its my fault that youre like this"
    show byte cheerful at byte_pos_center with dissolve
    vye "but im not giving up on my feelings just yet"
    vye "ill wait"
    player_username "For what?"
    vye "for you to need me"
    show byte excited at byte_pos_center with dissolve
    vye "and when that time comes.. ill be a better girly ghost virus girlfriend for you"
    player_username "Sigh"
    player_username "Alright then. I better be impressed when the time comes."
    stop music fadeout 3.0
    vye "hehehehehe of course [player_username]"

    hide byte
    scene bg black with dissolve

    n "My God. That was a pretty cringe story wasn't it?"
    n "At least its over now."
    pause (1.0)
    show byte angry at byte_pos_center
    vye "what did u just say [n]?"
    n "Oh god. WAIT I'M SORRY I DIDN-"

    return