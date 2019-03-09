define jb = Character("Prof. Jacky Baltes", color="#06799f", callback=speaker("jb"))
define gc = Character("Student G.C.", color="#069f67", callback=speaker("gc"))

label start:

    scene bg neutral with fade

    show jb neutral at center

    pause 1.0

    # Prof. Jacky's Introduction
    jb "Hello! I am Prof. Jacky Baltes."
    pause 1.5
    show jb skeptical
    jb "I've turned into a cartoon because I'm trying to find new ways to engage kids these days."

    show jb mad
    jb "They only seem to care about video games nowadays!"

    # G.C. Moves into the screen
    show jb neutral:
        xalign 0.5 
        linear 1.0 right

    show gc smile at offscreenleft

    show gc smile:
        linear 1.0 left

    gc "Hello, Prof. Jacky!"
    jb "Oh, Hello, G.C."

    # GC shows some slides
    show gc neutral
    gc "I'm here to help you write these games." 
    gc "I got some old slides of mine to test our idea."
    gc "Look."

    show bg slide1 with dissolve

    pause 1.0

    show bg slide2 with dissolve

    pause 1.0
    
    show bg slide3 with dissolve

    pause 1.0

    show jb skeptical

    jb "Great, but aren't we a little too large?"

    show gc arm_raiser
    gc "We can just get smaller then."

    show gc smile at left:
        linear 1.0 halfsize
    gc "Like this."

    show gc neutral
    gc "You can do it too."

    show jb ooh at right:
        time 0.2
        linear 1.0 halfsize
    jb "Oooh."

    pause 0.5
    show jb neutral
    jb "This is kinda neat."

    show bg slide4 with dissolve
    pause 1.0

    show bg slide5 with dissolve
    pause 1.0

    gc "If we need, we can move around too."
    show gc neutral:
        linear 1.0 right
        linear 1.0 left 
    show jb neutral:
        linear 1.0 left
        linear 1.0 right

    pause 1.0

    gc "We can even go offscreen entirely."
    show gc neutral:
        linear 1.0 offscreenleft 
    show jb neutral:
        linear 1.0 offscreenright 
    
    pause 1.0

    gc "And hide the menu if we want to only show the slide."
    window hide
    pause 3.0
    show bg neutral with dissolve
    show gc neutral:
        normalsize
        linear 1.0 left
    show jb neutral:
        normalsize
        linear 2.0 right

    pause 1.0

    gc "Since this is a game we can also do some quizzes."

    $ wrong_tries = 0
    menu drink_quiz:
        "Which is the better drink?"

        "Coffee":
            "Correct!"

        "Water":
            "Try again. Wrong answer."
            $ wrong_tries += 1

            jump drink_quiz

    if wrong_tries > 0:
        gc "I can't believe you tried water %(wrong_tries)d times."
        jb "Very funny."
    
    show gc neutral
    gc "Soo... What do you think of it?"

    show jb skeptical

    jb "I think it's coming along. But, we've still got a lot of work to do."

    show gc arm_raiser
    gc "I agree."
    show gc neutral
    gc "Well, I'm gonna go, I think this is it for now."
    show gc arm_raiser
    gc "Bye, bye, Prof. Jacky."

    show gc neutral:
        linear 0.5 offscreenleft

    pause 0.5
        
    show jb neutral:
        linear 2.0 center

    pause 2.0
    jb "Well, I really hope you will enjoy these courses."
    jb "Bye, bye."

    hide jb with dissolve

    return
