init python:
    """
        The piece of code below defines a kind called "speaker" that can be
        passed as an argument when creating a character. Then the character
        can be animated during the scrolling of the text.
    """
    # This is set to true while a character is speaking, and False when
    # the character is done.
    speaking = None 

    def while_speaking(name, speak_d, default_d, st, at):
        if speaking == name:
            return speak_d, 0.75
        else:
            return default_d, 0.75

    # Curried form of the above
    curried_while_speaking = renpy.curry(while_speaking)

    # Receives two arguments, the default animation and a speaking animation
    def WhileSpeaking(name, default, speaking):
        return DynamicDisplayable(curried_while_speaking(name, speaking, default))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    speaker = renpy.curry(speaker_callback)
 
################### Prof. Jacky Baltes Character ##############################
image jb neutral = LiveComposite(
    (1000, 800),
    (0, 0), im.FactorScale("Characters/ProfJB_Trunk.png",0.5),
    (0, 0), im.FactorScale("Characters/ProfJB_Head.png",0.5),
    (0, 0), "jb eyes normal",
    (0, 0), WhileSpeaking("jb", "jb mouth shut", "jb mouth speaking"),
    (0, 0), "jb left arm apple",
    (0, 0), WhileSpeaking("jb", "jb right arm rest", "jb right arm explaining"),
    )

image jb mad = LiveComposite(
    (1000, 800),
    (0, 0), im.FactorScale("Characters/ProfJB_Trunk.png",0.5),
    (0, 0), im.FactorScale("Characters/ProfJB_Head.png",0.5),
    (0, 0), "jb eyes mad",
    (0, 0), WhileSpeaking("jb", "jb mouth shut", "jb mouth speaking mad"),
    (0, 0), WhileSpeaking("jb", "jb right arm rest", "jb right arm mad"),
    (0, 0), "jb left arm apple",
    )

image jb skeptical = LiveComposite(
    (1000, 800),
    (0, 0), im.FactorScale("Characters/ProfJB_Trunk.png",0.5),
    (0, 0), im.FactorScale("Characters/ProfJB_Head.png",0.5),
    (0, 0), "jb eyes skeptical",
    (0, 0), WhileSpeaking("jb", "jb mouth tilted", "jb mouth speaking"),
    (0, 0), "jb right arm rest",
    (0, 0), "jb left arm chin",
    )

image jb ooh = LiveComposite(
    (1000, 800),
    (0, 0), im.FactorScale("Characters/ProfJB_Trunk.png",0.5),
    (0, 0), im.FactorScale("Characters/ProfJB_Head.png",0.5),
    (0, 0), "jb eyes normal",
    (0, 0), "jb mouth ooh",
    (0, 0), "jb left arm apple",
    (0, 0), "jb right arm rest",
    )

image jb eyes normal:
    im.FactorScale("Characters/ProfJB_Eyes-Neutral.png",0.5)
    choice:
        3.5
    choice:
        2.0
    choice:
        1.0
    im.FactorScale("Characters/ProfJB_Eyes-Shut.png",0.5)
    .25
    repeat

image jb eyes mad:
    im.FactorScale("Characters/ProfJB_Eyes-Mad.png",0.5)
image jb eyes skeptical:
    im.FactorScale("Characters/ProfJB_Eyes-Skeptical.png",0.5)
image jb mouth shut:
    im.FactorScale("Characters/ProfJB_Mouth-Shut.png",0.5)
image jb mouth ooh:
    im.FactorScale("Characters/ProfJB_Mouth-Ooh.png",0.5)
image jb mouth aah:
    im.FactorScale("Characters/ProfJB_Mouth-Aah.png",0.5)
image jb mouth smile:
    im.FactorScale("Characters/ProfJB_Mouth-Smile.png",0.5)
image jb mouth tilted:
    im.FactorScale("Characters/ProfJB_Mouth-Tilted.png",0.5)
image jb mouth angry:
    im.FactorScale("Characters/ProfJB_Mouth-Angry.png",0.5)
image jb mouth frown:
    im.FactorScale("Characters/ProfJB_Mouth-Frown.png",0.5)

image jb mouth speaking:
    choice:
        "jb mouth shut"
        choice:
            .15
        choice:
            .10
    choice:
        "jb mouth ooh"
        choice:
            .20
        choice:
            .10
    choice:
        "jb mouth aah"
        choice:
            .15
        choice:
            .10
    choice:
        "jb mouth smile"
        choice:
            .15
        choice:
            .10
    repeat

image jb mouth speaking mad:
    choice:
        "jb mouth angry"
        choice:
            .15
        choice:
            .10
    choice:
        "jb mouth ooh"
        choice:
            .20
        choice:
            .10
    choice:
        "jb mouth aah"
        choice:
            .15
        choice:
            .10
    choice:
        "jb mouth frown"
        choice:
            .15
        choice:
            .10
    repeat

image jb right arm rest:
    im.FactorScale("Characters/ProfJB_RightArm-Waist.png",0.5)
image jb right arm up:
    im.FactorScale("Characters/ProfJB_RightArm-5.png",0.5)
image jb right arm fist:
    im.FactorScale("Characters/ProfJB_RightArm-Fist-2.png",0.5)

image jb right arm explaining:
    choice:
        "jb right arm rest"
        choice:
            pause 2.0
        choice:
            pause 1.0
    choice:
        "jb right arm up"
        choice:
            pause 1.5
        choice:
            pause .7
    repeat

image jb right arm mad:
    choice:
        "jb right arm rest"
        choice:
            2.0
        choice:
            1.0
    choice:
        "jb right arm fist"
        choice:
            1.5
        choice:
            .7
    repeat

image jb left arm apple:
    im.FactorScale("Characters/ProfJB_LeftArm-Apple.png", 0.5)

image jb left arm chin:
    im.FactorScale("Characters/ProfJB_LeftArm-Chin-1.png", 0.5)
    .5
    im.FactorScale("Characters/ProfJB_LeftArm-Chin-2.png", 0.5)
    .5
    repeat
###################################################################

################## Student C. Character ###########################

image gc neutral = LiveComposite(
    (550, 800),
    (0, 0), im.FactorScale("Characters/mrC_Trunk.png", 0.5),
    (0, 0), im.FactorScale("Characters/mrC_Head.png", 0.5),
    (0, 0), "gc left arm neutral",
    (0, 0), "gc eyes normal",
    (0, 0), WhileSpeaking("gc", "gc mouth shut", "gc mouth speaking"),
    (0, 0), "gc right arm down",
    )

# This version raises the arm when speaking
image gc neutral arm_raiser = LiveComposite(
    (550, 800),
    (0, 0), im.FactorScale("Characters/mrC_Trunk.png", 0.5),
    (0, 0), im.FactorScale("Characters/mrC_Head.png", 0.5),
    (0, 0), "gc left arm neutral",
    (0, 0), "gc eyes normal",
    (0, 0), WhileSpeaking("gc", "gc mouth shut", "gc mouth speaking"),
    (0, 0), WhileSpeaking("gc", "gc right arm down", "gc right arm raised"),
    )

image gc smile = LiveComposite(
    (550, 800),
    (0, 0), im.FactorScale("Characters/mrC_Trunk.png", 0.5),
    (0, 0), im.FactorScale("Characters/mrC_Head.png", 0.5),
    (0, 0), "gc left arm neutral",
    (0, 0), "gc eyes normal",
    (0, 0), WhileSpeaking("gc", "gc mouth smile", "gc mouth speaking"),
    (0, 0), WhileSpeaking("gc", "gc right arm down", "gc right arm raised"),
    )

image gc mad = LiveComposite(
    (550, 800),
    (0, 0), im.FactorScale("Characters/mrC_Trunk.png", 0.5),
    (0, 0), im.FactorScale("Characters/mrC_Head.png", 0.5),
    (0, 0), "gc left arm neutral",
    (0, 0), "gc eyes mad",
    (0, 0), WhileSpeaking("gc", "gc mouth shut", "gc mouth speaking"),
    (0, 0), WhileSpeaking("gc", "gc right arm down", "gc right arm raised"),
    )

image gc frown = LiveComposite(
    (550, 800),
    (0, 0), im.FactorScale("Characters/mrC_Trunk.png",0.5),
    (0, 0), im.FactorScale("Characters/mrC_Head.png",0.5),
    (0, 0), "gc left arm neutral",
    (0, 0), "gc eyes normal",
    (0, 0), WhileSpeaking("gc", "gc mouth frown", "gc mouth speaking"),
    (0, 0), WhileSpeaking("gc", "gc right arm down", "gc right arm raised"),
    )

image gc eyes normal:
    im.FactorScale("Characters/mrC_Eyes-Neutral.png",0.5)
    choice:
        3.5
    choice:
        2.0
    choice:
        1.0
    im.FactorScale("Characters/mrC_Eyes-Shut.png",0.5)
    .25
    repeat

image gc eyes surprised:
    im.FactorScale("Characters/mrC_Eyes-Surprised.png",0.5)
    choice:
        3.5
    choice:
        2.0
    choice:
        1.0
    im.FactorScale("Characters/mrC_Eyes-Shut.png",0.5)
    .25
    repeat

image gc eyes mad:
    im.FactorScale("Characters/mrC_Eyes-Mad.png",0.5)
    choice:
        3.5
    choice:
        2.0
    choice:
        1.0
    im.FactorScale("Characters/mrC_Eyes-Shut.png",0.5)
    .25
    repeat

image gc mouth aah:
    im.FactorScale("Characters/mrC_Mouth-Aah.png", 0.5)

image gc mouth ooh:
    im.FactorScale("Characters/mrC_Mouth-Ooh.png", 0.5)

image gc mouth shut:
    im.FactorScale("Characters/mrC_Mouth-Neutral.png", 0.5)

image gc mouth frown:
    im.FactorScale("Characters/mrC_Mouth-Frown.png", 0.5)

image gc mouth smile:
    im.FactorScale("Characters/mrC_Mouth-Smile.png", 0.5)

image gc left arm neutral:
    im.FactorScale("Characters/mrC_Left-Hand-Neutral.png", 0.5)

image gc right arm down:
    im.FactorScale("Characters/mrC_Right-Hand-Down.png", 0.5)

image gc right arm raised:
    im.FactorScale("Characters/mrC_Right-Hand-Raised.png", 0.5)

image gc mouth speaking:
    choice:
        "gc mouth shut"
        choice:
            .15
        choice:
            .10
    choice:
        "gc mouth ooh"
        choice:
            .20
        choice:
            .10
    choice:
        "gc mouth aah"
        choice:
            .15
        choice:
            .10
    choice:
        "gc mouth smile"
        choice:
            .15
        choice:
            .10
    repeat

###################################################################

################## Ms. G. Character ###########################

image msG neutral = LiveComposite(
    (550, 700),
    (0, 0), "msG body",
    (0, 0), "msG head",
    (0, 0), "msG left_arm resting",
    (0, 0), "msG eyebrow normal",
    (0, 0), "msG eyes normal",
    (0, 0), WhileSpeaking("msG", "msG mouth normal", "msG mouth speaking"),
    (0, 0), "msG right_arm",
    )

image msG mad = LiveComposite(
    (550, 700),
    (0, 0), "msG body",
    (0, 0), "msG head",
    (0, 0), "msG left_arm resting",
    (0, 0), "msG eyebrow mad",
    (0, 0), "msG eyes normal",
    (0, 0), WhileSpeaking("msG", "msG mouth closed", "msG mouth speaking mad"),
    (0, 0), "msG right_arm",
    )

image msG curious = LiveComposite(
    (550, 700),
    (0, 0), "msG body",
    (0, 0), "msG head",
    (0, 0), "msG left_arm resting",
    (0, 0), "msG eyebrow curious",
    (0, 0), "msG eyes normal",
    (0, 0), WhileSpeaking("msG", "msG mouth eh", "msG mouth speaking"),
    (0, 0), "msG right_arm",
    )

image msG neutral explaining = LiveComposite(
    (550, 700),
    (0, 0), "msG body",
    (0, 0), "msG head",
    (0, 0), WhileSpeaking("msG", "msG left_arm resting", "msG left_arm explaining"),
    (0, 0), "msG eyebrow normal",
    (0, 0), "msG eyes normal",
    (0, 0), WhileSpeaking("msG", "msG mouth normal", "msG mouth speaking"),
    (0, 0), "msG right_arm",
    )

image msG curious explaining = LiveComposite(
    (550, 700),
    (0, 0), "msG body",
    (0, 0), "msG head",
    (0, 0), WhileSpeaking("msG", "msG left_arm resting", "msG left_arm explaining"),
    (0, 0), "msG eyebrow curious",
    (0, 0), "msG eyes normal",
    (0, 0), WhileSpeaking("msG", "msG mouth closed", "msG mouth speaking mad"),
    (0, 0), "msG right_arm",
    )

image msG eyes normal:
    "msG eyes open"
    choice:
        3.5
    choice:
        2.0
    choice:
        1.0
    "msG eyes closed"
    .25
    repeat

image msG body:
    im.FactorScale("Characters/msG_Body.png", 0.25)

image msG eyebrow normal:
    im.FactorScale("Characters/msG_Eyebrown-Normal.png", 0.25)

image msG eyebrow mad:
    im.FactorScale("Characters/msG_Eyebrown-Mad.png", 0.25)

image msG eyebrow curious:
    im.FactorScale("Characters/msG_Eyebrown-Curious.png", 0.25)

image msG head:
    im.FactorScale("Characters/msG_Head.png", 0.25)

image msG eyes open:
    im.FactorScale("Characters/msG_Eyes-Open.png", 0.25)

image msG eyes closed:
    im.FactorScale("Characters/msG_Eyes-Closed.png", 0.25)

image msG mouth closed:
    im.FactorScale("Characters/msG_Mouth-Closed-Sad.png", 0.25)

image msG mouth eh:
    im.FactorScale("Characters/msG_Mouth-Eh.png", 0.25)

image msG mouth kiss:
    im.FactorScale("Characters/msG_Mouth-Kiss-Ooh.png", 0.25)

image msG mouth normal:
    im.FactorScale("Characters/msG_Mouth-Normal.png", 0.25)

image msG mouth open:
    im.FactorScale("Characters/msG_Mouth-Open-Sad-Eh.png", 0.25)

image msG mouth smile:
    im.FactorScale("Characters/msG_Mouth-Smile-Ah.png", 0.25)

image msG right_arm:
    im.FactorScale("Characters/msG_RightArm.png", 0.25)

image msG left_arm resting:
    im.FactorScale("Characters/msG_LeftArm-Resting.png", 0.25)

image msG left_arm explaining:
    im.FactorScale("Characters/msG_LeftArm-Explaining.png", 0.25)

image msG mouth speaking:
    choice:
        "msG mouth normal"
        choice:
            .15
        choice:
            .10
    choice:
        "msG mouth kiss"
        choice:
            .20
        choice:
            .10
    choice:
        "msG mouth eh"
        choice:
            .15
        choice:
            .10
    choice:
        "msG mouth smile"
        choice:
            .15
        choice:
            .10
    repeat

image msG mouth speaking mad:
    choice:
        "msG mouth closed"
        choice:
            .15
        choice:
            .10
    choice:
        "msG mouth kiss"
        choice:
            .20
        choice:
            .10
    choice:
        "msG mouth eh"
        choice:
            .15
        choice:
            .10
    choice:
        "msG mouth open"
        choice:
            .15
        choice:
            .10
    repeat
