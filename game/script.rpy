init python:
    import os, time, uuid

    fake_logs = []

    def make_safe_filename(base):
        base = base.replace(" ", "_").lower()
        unique = uuid.uuid4().hex[:8]
        return f"{base}_{unique}.txt"

    def create_fake_log_entry(display_name="byte_report", content=None, write_to_disk=True):
        """
        Create a fake log entry and optionally write it to the game's folder.
        Returns (filename, display_name, content)
        """
        if content is None:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            content = f"--- fake log generated {t} ---\nuser: byte\nnotes: suspicious activity detected\nstatus: inconclusive\n"

        filename = make_safe_filename(display_name)
        fake_logs.append((filename, display_name, content))

        if write_to_disk:
            try:
                with open(os.path.join(renpy.game.path, filename), "w", encoding="utf-8") as f:
                    f.write(content)
            except Exception:
                pass

        return filename, display_name, content

    def get_fake_logs():
        return list(fake_logs)

    def get_fake_log_content(filename):
        for fn, display, content in fake_logs:
            if fn == filename:
                return content
        full = os.path.join(renpy.game.path, filename)
        try:
            with open(full, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            return "[file not found]"

init python:
    def _delete_log(filename):
        global fake_logs, _selected_log
        if filename is None:
            renpy.notify("no log selected")
            return
        fake_logs = [entry for entry in fake_logs if entry[0] != filename]
        _selected_log = None
        renpy.notify("log deleted (in-game only)")

    def _save_copy(filename):
        if filename is None:
            renpy.notify("no log selected")
            return
        content = get_fake_log_content(filename)
        try:
            path = os.path.join(renpy.game.path, "copy_of_" + filename)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            renpy.notify("saved copy to game folder: copy_of_" + filename)
        except Exception:
            renpy.notify("couldn't save copy (permission issue)")



# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Byte", image = "byte")
define p = Character("[user]")
define n = Character("Narrator")
define vye = Character("Vye")
define nme = Character("[name]")

init python:
    import os
    username = os.getlogin()

define player_username = Character("[username]")

default vbs = False
default virus_route = False
default trust = 0
default charm = 0
default awareness = 0
default curiosity = 0



image bg vrchat = Transform("images/vrchat.png", fit="cover")
image bg request = Transform("images/request.png", fit="cover")
image bg desktop_1 = Transform("images/desktop_1.png", fit="cover")
image bg desktop_2 = Transform("images/desktop_2.png", fit="cover")
image bg desktop_3 = Transform("images/desktop_3.png", fit="cover")
image bg desktop_4 = Transform("images/desktop_4.png", fit="cover")
image bg desktop_5 = Transform("images/desktop_5.png", fit="cover")
image bg chatroom = Transform("images/chatroom.png", fit="cover")
image bg black = Transform("images/black.png", fit="cover")
image bg bluescreen = Transform("images/bluescreen.jpg", fit="cover")

image bedroom = Movie(size = (1920, 1080), play = "images/menu_bg.webm")

image byte corrupted:
    "byte corrupted 1"
    pause (0.2)
    "byte corrupted 2"
    pause (0.2)
    "byte corrupted 3"
    pause (0.2)
    "byte corrupted 2"
    pause (0.2)
    repeat

image byte angry = im.Scale("byte angry.png", 600, 1100)
image byte begging = im.Scale("byte begging.png", 600, 1100)
image byte blank = im.Scale("byte blank.png", 600, 1100)
image byte blushing = im.Scale("byte blushing.png", 600, 1100)
image byte cheerful = im.Scale("byte cheerful.png", 600, 1100)
image byte cocky = im.Scale("byte cocky.png", 600, 1100)
image byte delighted = im.Scale("byte delighted.png", 600, 1100)
image byte displeased = im.Scale("byte displeased.png", 600, 1100)
image byte excited = im.Scale("byte excited.png", 600, 1100)
image byte neutral = im.Scale("byte neutral.png", 600, 1100)

transform byte_pos_left:
    yalign 0.0
    xalign 0.0

transform byte_pos_right:
    yalign 0.0
    xalign 1.0

transform byte_pos_center:
    yalign 0.0
    xalign 0.5

transform fade_in_1:
    yalign 0.0
    xalign 0.5
    alpha 0.0
    linear 5.0 alpha 0.15

transform fade_in_2:
    yalign 0.0
    xalign 0.5
    alpha 0.0
    linear 10.0 alpha 0.15

transform zoom_in:
    yalign 0.0
    xalign 0.5
    ease 0.25 zoom 1.5
    alpha 1

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/game_bgm.mp3" volume 0.2
    scene bg vrchat

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "byte happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "It's a slow night. You've been working overtime for 4 days straight now, and its finally your well earned break."
    n "You've been working for so long, you don't really know what else to do in your free time other than playing video games and sleeping."
    n "Even if you've got quite the looks, you're already past your prime. You're just a hardcore gaming bum with no girlfriend, much less any friends."
    n "It's late and here you are, scrolling through different chatrooms in VRChat" 
    n "You're an introvert and you don't even have any friends, so why bother looking at the different chatrooms?? You really are a fucking bum."

label connection_start:

    "Steam - New message"

    show bg request
    with dissolve

    "What the hell? I don't have any friends. Why is someone messaging me on Steam?"

    show byte neutral at byte_pos_center
    pause (1)
    show byte neutral at byte_pos_left
    with move
    pause (1)
    show byte excited at byte_pos_left
    with dissolve

    v "Text: heya! ru xX67NewbDestroyer67Xx?"
    "Who the fuck even is that.. What the fuck is this guy even saying?"
    show byte cocky at byte_pos_left
    with dissolve
    v "Text: im the girl from that cs2 game you played last night? it's me, byte!" 
    "I mean I play cs2, but who the fuck is that?"
    v "Tex: yk we really hit it off that time and was just wonderinggg.. if u wanna duo sometime?"
    "Fuck, do I really have to say something?"

    menu:
        "Who's xX67NewbDestroyer67Xx?":
            $ awareness += 2
            $ trust -= 1
            "Text: Who the fuck is xX67NewbDestroyer67Xx??? Who the fuck are you??"
            jump choice_connection_1a

        "I play like shit, are you really sure about this?":
            $ trust += 1
            $ charm += 2
            "Text: haha i played like shit compared to u, u wanna duoq with a bot frag like me?"
            jump choice_connection_1b

        "Uhhhhh.":
            $ charm += 1
            "Text: uhhhhh"
            jump choice_connection_1c

label choice_connection_1a:

    show byte cheerful at byte_pos_left
    with dissolve
    v "Text: awee cmon no need to be shy. i mean u have a real shit username but i think we hit it off pretty well"
    v "Text: i mean even if your not him you should just add me"
    show byte excited at byte_pos_left with dissolve
    v "Text: im bored as fuck and need a duo"

    jump connection_end_1

label choice_connection_1b:

    show byte excited at byte_pos_left with dissolve
    v "Text: ur not ass, ive seen u hit some real clean shots"
    v "Text: lemme add you rq oki?"
    v "Text: alright now thats done you should hop on tmr!"
    show byte cheerful at byte_pos_left with dissolve
    v "Text: ill be waiting!"

    jump connection_end_2

label choice_connection_1c:

    show byte excited at byte_pos_left with dissolve
    v "Text: ill take that as a yes?"
    v "Text: there i sent a req just add me"
    show byte cheerful at byte_pos_left with dissolve
    v "Text: lets q tmr yeh?"

    jump connection_end_2

label connection_end_1:

    "Steam - byte has sent you a friend request"

    "Fuck it, why not?"
    "Text: It's my break tomorrow. I'll hop on after lunch."
    v "Text: niceeee!" 
    v "Text: oh yeah since ur obv no xX67NewbDestroyer67Xx.. wats ur real user?"

    $ user = renpy.input ("What is your user?", length = 32)
    $ user = user.strip()

    if not user:
        $ user = "xX69420CSONETAP69420Xx"

    p "Text: It's [p]."
    show byte cheerful at byte_pos_left with dissolve
    v "Text: see u tmr then [p]"

    "Steam - byte has left the chat"

    hide byte
    with dissolve

    n "Are you fucking smiling? You cringe ass bum." 
    n "It's been a while since a conversation online didn't immediately feel fake."
    n "But Jesus Christ you are so fucking cringe."

    jump firstday_start


label connection_end_2:

    "Steam - byte has sent you a friend request"

    "Fuck it, why not?"
    "Text: It's my break tomorrow. I'll hop on after lunch."
    v "Text: niceeee! see u tmr then"
    "Text: Also, you do know I'm not actually NewbDestroyer, right?"

    $ user = renpy.input ("What is your user?", length = 32)
    $ user = user.strip()

    if not user:
        $ user = "xX69420CSONETAP69420Xx"

    p "Text: It's [p]."
    show byte cocky at byte_pos_left with dissolve
    v "Text: Yupppp i know"
    v "Text: i just wanted someone to q with lol"
    show byte excited at byte_pos_left with dissolve
    v "Text: dont keep me waiting too long oki?"

    "Steam - byte has left the chat"

    hide byte
    with dissolve

    n "Are you fucking smiling? You cringe ass bum." 
    n "It's been a while since a conversation online didn't immediately feel fake."
    n "But Jesus Christ you are so fucking cringe."

    jump firstday_start
