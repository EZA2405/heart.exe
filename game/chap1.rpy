label firstday_start:

    scene bg black
    with dissolve

    n "It's 1 in the morning and you have a shift tomorrow. Yet here you are, wasting away, game after game, loss after loss."
    n "You fucking bum."

    p "That was.. actually fun."
    p "God, how long has it been since I actually had fun"

    "Steam - New message from byte"

    scene bg chatroom
    with dissolve

    n "The background was changed to a lofi bedroom because it looked better."

    show byte excited at byte_pos_left

    v "Text: good game man.. good game"
    v "Text: still dont see why you keep saying ur shit"
    v "Text: u play better than me lol"

    p "Text: You're not so bad either. We're not that far apart in damage."
    
    show byte cheerful at byte_pos_center
    with move

    v "Text: u dont have to talk all so formal with me yk hehe"
    v "Text: its just fun and games!"
    p "Text: Hah, this is just the way I text. It feels normal for me this way"
    v "Text: well arent you quite the charmer.. all fancy and stuff"
    show byte neutral at byte_pos_center with dissolve
    v "Text: u seem chill. not like the usual guys i talk to."

    menu:
        "Different good or different weird?":
            $ awareness -= 1
            $ trust += 2
            $ charm += 1
            p "Text: Huh, different good or different weird?"
            jump choice_firstday_1a

        "You don't know me yet.":
            $ awareness += 2
            $ trust -= 1
            $ charm -= 2
            p "Text: You don't even know me yet."
            jump choice_firstday_1b

        "You say that to everyone, dont you?":
            $ charm -= 1
            $ trust -= 1
            $ awareness += 2
            p "Text: You just say that to everyone, dont you?"
            jump choice_firstday_1c

label choice_firstday_1a:

    show byte cocky at byte_pos_center with dissolve
    v "Text: haha maybe. who knows! u just feel.. very real"
    v "Text: u deffo are quite the charmer"

    jump firstday_end

label choice_firstday_1b:

    show byte begging at byte_pos_center with dissolve
    v "Text: heyhey dont be so defensive on me now!"
    show byte cocky at byte_pos_center with dissolve
    v "Text: i intend to get to know u quite well heh"

    jump firstday_end

label choice_firstday_1c:

    show byte cheerful at byte_pos_center with dissolve
    v "Text: nuhuhhhh ur the only one i said that too!"
    show byte cocky at byte_pos_center with dissolve
    v "Text: but dont get too cheeky okai? dont think ur too special heh"  

    jump firstday_end

label firstday_end:

    p "Text: You know, maybe you're the real charmer here."
    p "Text: You certainly have a way with talking to people, quite better than me at least."
    show byte cheerful at byte_pos_center with dissolve
    v "Text: wat can i say i just know how to hit the right buttons i guess"
    v "Text: kinda late already, wat u gon do tmr?"

    n "You think for a moment.. your bum ass hasn't had this much fun for a long long while."
    n "You realize that.."
    n "this.."
    n "is.."
    n "actually quite nice."
    n "You always thought that you don't need friends, but maybe, just having one isn't so bad."

    p "Text: I have work tomorrow, but I'll get on at night."
    p "Text: That's if you're not busy of course."

    show byte delighted at byte_pos_center with dissolve
    v "Text: me? busy? nah not really.. my line of work can be done at home lol"
    v "Text: thats why im always so free hehehe"
    p "Text: That's nice to know. I'll see you tomorrow then after work."
    show byte excited at byte_pos_center with dissolve
    v "Text: You got it fren!"

    hide byte
    with dissolve

    "Steam - byte has left the chat"

label latenight_start:

    scene bg black
    with dissolve

    n "A few days later, you find yourself checking Steam chat more often than usual. You bum."
    n "Every time you log in, byte's already there.. waiting."

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_center

    v "Text: hey u night owl u always up this late?"
    p "Text: yeah, my sleep schedules been doomed for years"
    show byte cheerful at byte_pos_center with dissolve
    v "Text: same lol i think ive become part bat at this point sigh"

    n "You both laugh like you guys are in a cringey romcom. The conversation feels easy, even a little familiar now."

    show byte neutral at byte_pos_center with dissolve
    v "Text: u ever feel like ppl online understand u better than real ones?"
    v "Text: like.. theres no pressure here. no judging faces. just words and vibes."

    menu:
        "Yeah. It's a lot easier to be honest behind a screen.":
            $ trust += 2
            p "Text: yeah. its a lot easier to be honest behind a screen. we cant judge each other if we cant see each other to begin with"
            show byte delighted at byte_pos_center with dissolve
            v "Text: exactly! you get me right. i like that about you already."
        "That's kind of sad when you think about it.":
            $ awareness += 1
            $ trust += 2
            p "Text: thats kind of sad tho. that just means people cant be real in person anymore"
            v "Text: maybe.. or maybe this *is* the real us. ykwim? no masks no filters"
        "You just haven't met the right people offline yet.":
            $ charm += 2
            $ trust += 1
            $ awareness -= 1
            p "Text: you just havent met the right people offline yet"
            p "Text: god i sound so cringe dont i"
            show byte delighted at byte_pos_center with dissolve
            v "Text: aww, you sound kinda sweet when you say stuff like that. careful, i might fall for it"

    n "The chat goes on for hours. All the jokes, random stories, ig reels, like just go to sleep already bruh."

    show byte neutral at byte_pos_center with dissolve
    v "Text: u ever think about how weird it is that we can just.. talk like thisss?"
    v "Text: like two strangers across who knows how many miles, pretending the world isnt falling apart"
    p "Text: maybe thats why we do it. to forget things for a bit.." 
    v "Text: ur surprisingly deep for a random guy online"

    n "Are you grinning? What a simp bro."
    n "Somewhere between her sarcasm and sincerity, you feel something shift." 
    n "It's very small, you almost miss it." 
    n "But it's starting to feel like the start of a strange connection."

    v "Text: anyway, its late.. i should probably log off" 
    show byte begging at byte_pos_center with dissolve
    v "Text: dont wanna pass out on my keyboard again gods that night was so embarassinggg"
    p "Text: haha fair. sleep well byte"
    show byte cheerful at byte_pos_center with dissolve
    v "Text: you too my mystery man. same time tomorrowwww? maybeeeee?"

    menu:
        "Yeah. I'll be here.":
            $ charm += 2
            $ trust += 2
            p "Text: yeah ill be here.. just for u lol"
            show byte delighted at byte_pos_center with dissolve
            v "Text: yay! dont make me wait too long or else im throwing on purposeee~"
        "We'll see.":
            $ awareness += 2
            p "Text: we'll see.. depends if I survive work tomorrow my boss will prolly be on my ass again"
            show byte neutral at byte_pos_center with dissolve
            v "Text: hehe ykw they say work hard sleep harder"
        "I don't know, it's weird for me to get this close with someone":
            $ awareness += 2
            $ charm -= 2
            $ trust -= 2
            p "Text: idk, its weird for me to get this close with someone"
            show byte begging at byte_pos_center with dissolve
            v "Text: ouch.. hey dont get cold feet on me nowww. u gotta cary me past 14k elo"


    hide byte
    with dissolve

    "Steam - byte has left the chat"

    n "The smile on your face stays long after the chat ends and god is it a creepy smile."
    n "Did your mom drop you as a baby?"

    p "Maybe this online thing isn't such a bad idea after all."

label gamenight_start:

    scene bg black
    with dissolve

    n "It was your usual game night."
    n "Or maybe unusual?"
    n "You don't know how and you don't know why, but a girl is outperforming you, a nerd, in CS2."

    scene bg chatroom
    with dissolve
    pause (0.5)
    show byte neutral at byte_pos_center

    p "Text: jesus christ byte great game" 
    p "Text: did u install cheats or smth fuck ur crazy bro" 
    v "Text: hahahaha, thanks"
    p "Text: like holy shit those flicks" 
    p "Text: and that clutch in ct side mirage.. beautiful man" 
    v "Text: hahahaha, thanks" 
    stop music fadeout 3.0
    show byte blank at byte_pos_center
    pause (0.1)
    show byte neutral at byte_pos_center
    pause (0.1)
    show byte blank at byte_pos_center
    pause (0.1)
    show byte neutral at byte_pos_center
    pause (1.7)
    p "Text: uhh byte u good?"
    pause (2.0)
    v "Text: oh wut" 
    show byte cheerful at byte_pos_center with dissolve
    v "Text: OH MB yeah i was just feeling it tnight lol" 
    

    menu:
        "Ask if she's alright":
            $ curiosity += 1
            p "Text: u good?"
            show byte neutral at byte_pos_center with dissolve
            v "Text: yeh im fine y?"
            p "Text: i didnt say anything a while ago cuz we were locked in"
            p "Text: but u were pretty quiet today.."
            p "Text: and ur voice was weirdly monotone"
            p "Text: sorry did i do smth to make u mad?"
            v "Text: yeh im fine y?"
            show byte begging at byte_pos_center with dissolve
            v "Text: fuck sorry thats mb"
            v "Text: sorry im just running a lot of processes rn"
            p "Text: processes? like in ur pc"
            show byte neutral at byte_pos_center with dissolve
            v "Text: sure smth like that yeh"
            p "Text: uhh alright"

            n "Things are clearly not alright."
            show byte cocky at byte_pos_center with dissolve
            v "Text: dont overthink it too much lol"
        "Ignore":
            p "Text: imo feeling it is an understatement"
            p "Text: u were destroying them like holy shit"
            p "Text: gods that was crazy"
            p "Text: u hard carried"
            show byte neutral at byte_pos_center with dissolve
            v "Text: hahahaha, thanks" 
            pause (2.0)
            show byte cheerful at byte_pos_center with dissolve
            v "Text: u didnt play too bad"
            show byte begging at byte_pos_center with dissolve
            v "Text: srry im just kinda busy rn im cramming some overtime stuff"
            p "Text: oh thats tuff i hate overtime"
            show byte neutral at byte_pos_center with dissolve
            p "Text: u should focus then"
    
    p "Text: alr then, imma hop off for the night now"
    v "Text: gn [p]"

    hide byte
    with dissolve

    "Steam - byte has left the chat"

    p "Text: gn byte"

    jump closer_start
