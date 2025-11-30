   
label reveal_click_yes:
    
    show bg black
    with dissolve

    n "Two days passed in the blink of an eye."
    n "No messages. No new posts. Just silence."
    n "Then, suddenly, the notification tone hits."
    "Steam - New message from byte"

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_right

    v "Text: hey"
    p "Text: hey.. wow, u disappeared"
    show byte blank at byte_pos_right
    v "Text: yeah. needed time to think."

    n "You exhale. The tone feels different.. slower, heavier."

    v "Text: been thinking a lot about u actually"
    p "Text: oh?"
    v "Text: yeah. like how u make me feel safe. how u listen. how u never judged me"
    show byte neutral at byte_pos_right
    v "Text: u dont get that a lot online yknow?"

    n "You smile a bit. Then notice her typing bubble doesnt stop."

    v "Text: so i did something"
    p "Text: uh oh. what did u do lol"
    v "Text: remember that link i sent?"

    n "Your stomach drops."
    n "As it should dumbass."

    v "Text: yeah dont freak out but i kinda used it"
    p "Text: used it? what do u mean used it"
    v "Text: i just wanted to see if ud open it. and u did. idk. i just wanted to *know* how much u trust me"

    n "The typing pauses. Your hands feel cold."

    p "Text: byte what the hell are u talking about"
    v "Text: dont be mad. i just wanted to understand something"
    v "Text: how far someone would go for someone they barely know"

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    n "The screen flickers. A different icon flashes beside her name. It's not her usual profile pic."

    if trust > awareness and charm <= 3:
        jump bad_ending_click_yes
    elif charm >= 4 and trust < 8:
        jump neutral_ending_click_yes
    elif charm > 8 and trust > 8  :
        jump good_ending_click_yes
    else:
        jump bad_ending_click_yes


label reveal_click_no_vbs_yes:

    scene bg black
    with dissolve

    n "Two days passed in the blink of an eye."
    n "No messages. No new posts. Just silence."
    n "Then, suddenly, the notification tone hits."
    "Steam - New message from byte"

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_right

    v "Text: hey"
    p "Text: hey.. wow, u disappeared"
    show byte blank at byte_pos_right
    v "Text: yeah. needed time to think."

    n "You exhale. The tone feels different.. slower, heavier."

    v "Text: been thinking a lot about u actually"
    p "Text: oh?"
    v "Text: yeah. like how u make me feel safe. how u listen. how u never judged me"
    show byte neutral at byte_pos_right
    v "Text: u dont get that a lot online yknow?"

    n "You smile a bit. Then notice her typing bubble doesnt stop."

    v "Text: so i did something"
    p "Text: uh oh. what did u do lol"
    v "Text: remember that link i sent?"

    n "Your stomach drops."

    p "Text: but i didnt click it.."
    v "Text: yeah doesnt really matter, i got other stuff to get thru"
    p "Text: get through what exactly.."
    v "Text: i just wanted to see if ud open it and idk.. i guess i just wanted to *know* how much u trust me"
    show byte cocky at byte_pos_right
    v "Text: and u didnt click it which is funny cuz i already got ur deets a long long time ago"

    n "The typing pauses. Your hands feel cold."

    p "Text: byte what the hell are u talking about"
    show byte neutral at byte_pos_right
    v "Text: dont be mad. i just wanted to understand something.."
    v "Text: how far someone would go for someone they barely know."

    show screen screen_flicker
    $ renpy.pause(1.5)  
    hide screen screen_flicker

    n "The screen flickers. A different icon flashes beside her name. It's not her usual profile pic."

    if trust > awareness and charm <= 3:
        jump bad_ending_click_no_vbs_yes
    elif charm >= 4 and trust < 8:
        jump neutral_ending_click_no_vbs_yes
    elif charm > 8 and trust > 8 :
        jump good_ending_click_no_vbs_yes
    else:
        jump bad_ending_click_no_vbs_yes

label reveal_click_no_vbs_no:

    scene bg black
    with dissolve

    n "Two days passed in the blink of an eye."
    n "No messages. No new posts. Just silence."
    n "Then, suddenly, the notification tone hits."
    "Steam - New message from byte"

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_right

    v "Text: hey"
    p "Text: hey.. wow, u disappeared"
    show byte blank at byte_pos_right
    v "Text: yeah. needed time to think."

    n "You exhale. The tone feels different.. slower, heavier."

    v "Text: been thinking a lot about u actually"
    p "Text: oh?"
    v "Text: yeah. like how u make me feel safe. how u listen. how u never judged me"
    show byte neutral at byte_pos_right
    v "Text: u dont get that a lot online yknow?"

    n "You smile a bit. Then notice her typing bubble doesnt stop."

    v "Text: so i did something"
    p "Text: uh oh. what did u do lol"
    v "Text: remember that link i sent?"

    n "Your stomach drops."

    p "Text: but i didnt click it.."
    v "Text: i just wanted to see if ud open it and idk.. i guess i just wanted to *know* how much u trust me"
    v "Text: and u didnt click it which is quite smart of u"

    n "The typing pauses. Your hands feel cold."

    p "Text: byte what the hell are u talking about"
    v "Text: dont be mad. i just wanted to understand something.."
    v "Text: how far someone would go for someone they barely know."

    n "Your Steam refreshes. A different icon flashes beside her name. It's not her usual profile pic."

    if trust > awareness and charm <= 3:
        jump bad_ending_click_no_vbs_no
    elif charm >= 4 and trust < 8:
        jump neutral_ending_click_no_vbs_no
    elif charm > 8 and trust > 8 :
        jump good_ending_click_no_vbs_no
    else:
        jump bad_ending_click_no_vbs_no