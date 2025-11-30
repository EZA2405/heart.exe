

label bad_ending_click_yes:

    play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0
    n "You feel a chill crawl up your spine."

    show byte blank at byte_pos_right with dissolve
    v "Text: i guess u really did trust me huh?"
    v "Text: thats... sweet."
    v "Text: u should probably check your email btw."

    n "You open your inbox. Dozens of notifications flood in. All of them about password resets, login alerts, strange transactions."

    v "Text: dont worry. i didnt take much."

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    show byte neutral at byte_pos_right with dissolve
    v "Text: hey u closing the app isnt gonna do u any good lol"

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    show byte blank at byte_pos_right with dissolve
    v "Text: yk i can see what ur doing on ur screen right?"

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    show byte angry at byte_pos_right with dissolve
    v "Text: its cute but also kinda pathetic"
    show byte blank at byte_pos_right with dissolve
    v "Text: anyways as i was sayin"
    v "Text: i just needed proof that ppl still fall for nice words."
    v "Text: dont hate me, okay?"

    n "You stare at the screen. the typing bubble blinks one last time."

    v "Text: bye, [p]."

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker
    hide byte

    "Steam - byte has left the chat"
    stop music fadeout 3.0

    n "And then she's gone."

    scene bg black
    with dissolve

    n "Your reflection stares back from the dark monitor.. smaller, quieter, a little less trusting."

    return

label neutral_ending_click_yes:

    v "Text: guess ur smarter than most ppl huh?"
    p "Text: depends what u mean by smart"
    v "Text: smart enough not to trust too easy."
    show byte cheerful at byte_pos_right with dissolve
    v "Text: thats good. thatll keep u safe."
    p "Text: from what exactly?"
    v "Text: one sec.."

    scene bg desktop_2
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
    v "Text: and done!"
    p "Text: wtf"
    p "Text: my laptop"
    p "Text: U HACKED MY FUCKING LAPTOP?"
    show byte delighted at byte_pos_right with dissolve
    v "Text: yeh.. my bad"

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_center

    n "Her messages come slower, shorter, almost like she's tired."

    v "Text: truth is, i wasnt lying about everything."
    v "Text: the stories, the jokes, the 3am talks.. they were real. i just... wanted to see if ud care."
    p "Text: but i did care"
    v "Text: yeah. thats why i stopped."
    v "Text: maybe we couldve been something more, [p]"
    v "Text: but you dont deserve a ghost"

    hide byte
    with dissolve

    "Steam - This user has deleted their account"

    n "You stare at the empty chat window. A new message appears in your own typing box.. from muscle memory."

    p "Text: goodnight byte"

    n "But no one is there to read it."

    return

label good_ending_click_yes:

    show byte blank at byte_pos_right with dissolve
    v "Text: u rlly clicked it.."
    p "Text: ofc, u asked me to didnt u?"
    v "Text: wow."
    p "Text: are u a hacker or smth"
    show byte neutral at byte_pos_right with dissolve
    v "Text: wut dyt dingus"
    v "Text: didnt u see ur screen flashing n shit?"
    p "Text: oh."
    v "Text: dont worry ill remove it lol"

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
    show byte excited at byte_pos_right with dissolve
    v "Text: done!"
    p "Text: thanks..?"
    v "Text: okay look.."

    n "She sends a long message. It's not the usual quick lines."

    hide byte
    pause (0.5)
    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_center with dissolve
    v "Text: listen... i used to do this. talk to ppl. gain their trust. take what i needed. i told myself it was survival. but every time i did it, i felt less real."
    v "Text: then i met u. and it was... different."
    p "Text: different how"
    show byte blushing at byte_pos_center with dissolve
    v "Text: like i actually wanted to stop lying."

    n "She goes quiet for a long time."

    show byte neutral at byte_pos_center with dissolve
    v "Text: so heres the truth. im not who i said i was. not even close."
    show byte begging at byte_pos_center with dissolve
    v "Text: and i get it if u hate me now."
    p "Text: i could tell. and i dont hate you. i just wish u told me sooner."
    v "Text: yeah. me too.."
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

    return

label bad_ending_click_no_vbs_yes:

    play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0

    n "You feel a chill crawl up your spine."

    show byte blank at byte_pos_right with dissolve
    v "Text: even if u didnt trust me with the link.."
    v "Text: u still trusted me with that file to edit ur cs config"
    v "Text: u should probably check your email btw."

    n "You open your inbox. Dozens of notifications flood in. All of them about password resets, login alerts, strange transactions."

    v "Text: dont worry. i didnt take much."

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    show byte neutral at byte_pos_right with dissolve
    v "Text: hey u closing the app isnt gonna do u any good lol"

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    show byte blank at byte_pos_right with dissolve
    v "Text: yk i can see what ur doing on ur screen right?"

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    show byte angry at byte_pos_right with dissolve
    v "Text: its cute but also kinda pathetic"
    show byte blank at byte_pos_right with dissolve
    v "Text: anyways as i was sayin"
    v "Text: i just needed proof that ppl still fall for nice words."
    v "Text: dont hate me, okay?"

    n "You stare at the screen. the typing bubble blinks one last time."

    v "Text: bye, [p]."

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker
    hide byte

    "Steam - byte has left the chat"
    stop music fadeout 3.0

    n "And then she's gone."

    scene bg black
    with dissolve

    n "Your reflection stares back from the dark monitor.. smaller, quieter, a little less trusting."

    return

label neutral_ending_click_no_vbs_yes:

    v "Text: guess ur smarter than most ppl huh?"
    p "Text: depends what u mean by smart"
    v "Text: smart enough not to trust too easy."
    show byte cheerful at byte_pos_right with dissolve
    v "Text: but not smart enough to not click random cs2 files huh"
    v "Text: you opening that cs2 config file editor gave me a way in to ur laptop"
    v "Text: be smarter next time yeh [p]?"
    p "Text: y exactly?"
    v "Text: one sec.."

    scene bg desktop_2
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
    v "Text: and done!"
    p "Text: wtf"
    p "Text: my laptop"
    p "Text: U HACKED MY FUCKING LAPTOP?"
    show byte delighted at byte_pos_right with dissolve
    v "Text: yeh.. my bad"

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_center

    n "Her messages come slower, shorter, almost like she's tired."

    v "Text: truth is, i wasnt lying about everything."
    v "Text: the stories, the jokes, the 3am talks.. they were real. i just... wanted to see if ud care."
    p "Text: but i did care"
    v "Text: yeah. thats why i stopped."
    v "Text: maybe we couldve been something more, [p]"
    v "Text: but you dont deserve a ghost"

    hide byte
    with dissolve

    "Steam - This user has deleted their account"

    n "You stare at the empty chat window. A new message appears in your own typing box.. from muscle memory."

    p "Text: goodnight byte"

    n "But no one is there to read it."

    return

label good_ending_click_no_vbs_yes:

    show byte blank at byte_pos_right with dissolve
    v "Text: why didnt you click the link first"
    p "Text: well it seemed too suspicious"
    v "Text: it was suspicious"
    show byte neutral at byte_pos_right with dissolve
    v "Text: i wanted to test you lol"
    p "Text: oh"
    show byte cocky at byte_pos_right with dissolve
    v "Text: too bad that file editor i sent u for the cs2 config was a virus lol"
    p "Text: oh."
    v "Text: yeh"
    v "Text: ..."
    v "Text: dont worry ill remove it lol"

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
    show byte excited at byte_pos_right with dissolve
    v "Text: done!"
    p "Text: thanks..?"
    v "Text: okay look.."

    n "She sends a long message. It's not the usual quick lines."

    hide byte
    pause (0.5)
    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_center with dissolve
    v "Text: listen... i used to do this. talk to ppl. gain their trust. take what i needed. i told myself it was survival. but every time i did it, i felt less real."
    v "Text: then i met u. and it was... different."
    p "Text: different how"
    show byte blushing at byte_pos_center with dissolve
    v "Text: like i actually wanted to stop lying."

    n "She goes quiet for a long time."

    show byte neutral at byte_pos_center with dissolve
    v "Text: so heres the truth. im not who i said i was. not even close."
    show byte begging at byte_pos_center with dissolve
    v "Text: and i get it if u hate me now."
    p "Text: i could tell. and i dont hate you. i just wish u told me sooner."
    v "Text: yeah. me too.."
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

    return

label bad_ending_click_no_vbs_no:

    play music "audio/suspense_bgm.mp3" volume 0.4 fadein 3.0

    n "You feel a chill crawl up your spine."

    show byte blank at byte_pos_right with dissolve
    v "Text: good for you fren.."
    show byte delighted at byte_pos_right with dissolve
    v "Text: u didnt click the link so ur safe!"
    v "Text: im serious ur actually safe"

    n "You open your email inbox. No new notifications. Nothing about password resets, login alerts, strange transactions."

    show byte cheerful at byte_pos_right with dissolve
    v "Text: dont worry. ur too smart for me lol"
    v "Text: just tryin to make a living here ykyk?"
    show byte blank at byte_pos_right with dissolve
    v "Text: dont hate me, okay?"

    n "You stare at the screen. the typing bubble blinks one last time."

    v "Text: bye, [p]."

    hide byte

    "Steam - byte has left the chat"
    stop music fadeout 3.0

    n "And then she's gone."

    scene bg black
    with dissolve

    n "Your reflection stares back from the dark monitor.. smaller, quieter, a little less trusting."

    return

label neutral_ending_click_no_vbs_no:

    v "Text: guess ur smarter than most ppl huh?"
    p "Text: depends what u mean by smart"
    v "Text: smart enough not to trust too easy."
    show byte cheerful at byte_pos_right with dissolve
    p "Text: y exactly?"
    v "Text: even if i dont say, im p sure u got an idea of wut i do"
    p "Text: well ur not wrong about that i guess"

    n "Her messages come slower, shorter, almost like she's tired."

    show byte neutral at byte_pos_center
    v "Text: truth is, i wasnt lying about everything."
    v "Text: the stories, the jokes, the 3am talks.. they were real. i just... wanted to see if ud care."
    p "Text: but i did care"
    v "Text: yeah. thats why i stopped."
    v "Text: maybe we couldve been something more, [p]"
    v "Text: but you dont deserve a ghost"

    hide byte
    with dissolve

    "Steam - This user has deleted their account"

    n "You stare at the empty chat window. A new message appears in your own typing box.. from muscle memory."

    p "Text: goodnight byte"

    n "But no one is there to read it."

    return

label good_ending_click_no_vbs_no:

    show byte blank at byte_pos_right with dissolve
    v "Text: why didnt you click the link first"
    p "Text: well it seemed too suspicious"
    v "Text: it was suspicious"
    show byte neutral at byte_pos_right with dissolve
    play music "audio/game_bgm.mp3" volume 0.2 fadein 3.0
    v "Text: i wanted to test you lol"
    p "Text: oh"
    p "Text: r u like tryna hack me or smth"
    v "Text: yeh"
    p "Text: oh."
    v "Text: ..."

    n "She sends a long message. It's not the usual quick lines."

    show byte neutral at byte_pos_center with move
    v "Text: listen... i used to do this. talk to ppl. gain their trust. take what i needed. i told myself it was survival. but every time i did it, i felt less real."
    v "Text: then i met u. and it was... different."
    p "Text: different how"
    show byte blushing at byte_pos_center with dissolve
    v "Text: like i actually wanted to stop lying."

    n "She goes quiet for a long time."

    show byte neutral at byte_pos_center with dissolve
    v "Text: so heres the truth. im not who i said i was. not even close."
    show byte begging at byte_pos_center with dissolve
    v "Text: and i get it if u hate me now."
    p "Text: i could tell. and i dont hate you. i just wish u told me sooner."
    v "Text: yeah. me too.."
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

    return
