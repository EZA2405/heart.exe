label virus_start:

    p "Text: prove what"
    p "Text: that ur not trying to brick my fkin laptop and hack my deets?"
    show byte begging at byte_pos_left with dissolve
    v "Text: hey noww lets not be too hasty alr"

    menu:
        "Refute her.":
            p "Text: hasty my ass dyt im blind???"
            p "Text: i can see u messing with my FUCKING files"
            v "Text: ur relly not gonna belieb me?"
            v "Text: cmonn [p] u gotta beliebe me"
            v "Text: its all just weird coincidences alrrr i promise"
            p "Text: u cant be fucking serious"
            p "Text: byte be honest with me"
            p "Text: are u hacking my ass or not."
            show byte blank at byte_pos_left with dissolve
            jump aware_ending
        "Call her weird.":
            p "Text: hasty my ass dyt im blind???"
            show byte blank at byte_pos_left with dissolve
            p "Text: i can see u messing with my FUCKING files"
            p "Text: and i just wanna add how fucking weird youve been the past couple days??"
            v "Text: What?"
            play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0
            p "Text: u answer practically instantly now"
            p "Text: its almost like ur in my laptop watching my every move"
            p "Text: and then theres the fact that u repeat the same shit every now and then"
            p "Text: but u dont notice it"
            p "Text: fuck and u play like a chess bot in cs2" 
            p "Text: like for all ik ur not even real"
            p "Text: how do i even know if im actually talking to byte"
            show byte neutral at byte_pos_left 
            pause (0.2)
            show byte blank at byte_pos_left 
            pause (0.2)
            show byte neutral at byte_pos_left 
            pause (0.1)
            show byte blank at byte_pos_left 
            p "Text: n not some broken bot???"
            show byte blank at byte_pos_left 
            pause (0.2) 
            show byte neutral at byte_pos_left 
            v "Text: I'm not a bot."
            v "Text: I'm still the same old Byte."
            show byte neutral at byte_pos_left 
            pause (0.2) 
            show byte angry at byte_pos_left 
            pause (0.2)
            show byte blank at byte_pos_left 
            pause (0.2) 
            show byte neutral at byte_pos_left 
            pause (0.2)
            show byte angry at byte_pos_left 
            pause (0.2)
            show byte blank at byte_pos_left 
            v "Text: I'm real."
            hide byte 
            pause (0.2)
            show byte blank at byte_pos_left 
            pause (0.2)
            hide byte 
            show byte angry at byte_pos_left 
            pause (0.2)
            hide byte
            pause (0.2)
            show byte neutral at byte_pos_left 
            v "Text: I am real."
            hide byte 
            pause (0.2)
            show byte blank at byte_pos_right 
            pause (0.1)
            show byte blank at byte_pos_left
            pause (0.1)
            show byte blank at byte_pos_right
            pause (0.2)
            hide byte 
            pause (0.2)
            show byte blank at byte_pos_center
            pause (0.1)
            show byte blank at byte_pos_left 
            hide byte 
            pause (0.2)
            show byte blank at byte_pos_center 
            v "Text: I AM REAL."
            show byte corrupted
            pause (0.08)
            hide byte 
            "Steam - byte has left the chat"
            pause (1.0)
            p "What the fuck just happened."

            scene bg desktop_3
            jump ipconfig


label aware_ending:
    v "Text: ..."
    v "Text: okay fine"
    v "Text: i may or may not... have sent u a virus.."
    v "Text: that gave me all ur deets.."
    p "Text: jesus christ byte"
    p "Text: srsly? i trusted u.."

    scene bg desktop_5
    pause (0.5)
    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker
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

    pause (3.0)
    play music "audio/game_bgm.mp3" volume 0.2 fadein 3.0
    v "Text: there i removed everything"
    show byte begging at byte_pos_left with dissolve
    v "Text: im sorry okay i was being dumb"
    p "Text: how do i know i can trust you"
    v "Text: mmmmm"
    show byte blank at byte_pos_left with dissolve
    v "Text: listen.."

    n "She sends a long message. It's not the usual quick lines."

    hide byte
    pause (0.5)
    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte blank at byte_pos_center with dissolve
    v "Text: i used to do this. talk to ppl. gain their trust. take what i needed. i told myself it was survival. but every time i did it, i felt less real."
    v "Text: then i met u. and it was... different."
    p "Text: different how"
    show byte blushing at byte_pos_center with dissolve
    v "Text: like i actually wanted to stop lying."

    n "She goes quiet for a long time."

    show byte neutral at byte_pos_center with dissolve
    v "Text: so heres the truth. im not who i said i was. not even close."
    show byte begging at byte_pos_center with dissolve
    v "Text: and i get it if u hate me now."
    p "Text: dammit byte i could tell"
    p "Text: im not stupid and u freaked me out. a lot."
    p "Text: but i dont hate you. i just wish u told me sooner."
    v "Text: yeah. me too.. im really sorry"
    p "Text: ..."
    
    $ nme = renpy.input ("What is your real name?", length = 32)
    $ nme = nme.strip()

    if not nme:
        $ nme = "Xab"

    nme "Text: idk if i should trust u with this.."    
    nme "Text: but im [nme.lower()]"

    if nme.lower() == user.lower():
        show byte neutral at byte_pos_center with dissolve
        v "Text: ur user is the same as ur real name?"
        nme "Text: yehh.. not very smart of me huh"
        show byte delighted at byte_pos_center with dissolve
        v "Text: LOL"
        v "Text: yeh not very smart of u [nme.lower()]"
        v "Text: but its still quite cute of u"
    show byte neutral at byte_pos_center with dissolve
    v "Text: sigh guess i have to do the same dont i?"
    nme "Text: u dont have to if u dont wanna"
    v "Text: no.. u deserve to know"
    vye "Text: my real names vye"
    vye "Text: and thanks for talking to me like i was real."

    n "A final message comes in.. It's an address in makati"

    hide byte
    with dissolve

    "Steam - byte has left the chat"

    scene bedroom
    with fade

    n "You close the laptop. The morning light slips through your window."
    stop music fadeout 3.0
    n "Somewhere out there, theres a girl waiting for you.."
    n "Fuck idk dawg u should prolly go see her.. i think she digs u."
    n "What you thought I was going to say something profound for the ending?"
    n "Fuck no."
    scene bg black with fade
    show byte corrupted at fade_in_2
    n "Also this isn't the real ending, in case you didnt notice."

    return
