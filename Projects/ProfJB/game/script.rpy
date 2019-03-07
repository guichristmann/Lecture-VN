define prof_jb = Character("Prof. Jacky Baltes")

image jb base = LiveComposite(
    (1000, 800),
    (0, 0), im.FactorScale("ProfJB_0026_Trunk.png",0.5),
    (0, 0), im.FactorScale("ProfJB_0025_Head.png",0.5),
    (0, 0), "jb eyes normal",
    (0, 0), "jb mouth shut",
    (0, 0), "jb left arm apple",
    (0, 0), "jb right arm rest",
    )

image jb speaking = LiveComposite(
    (1000, 800),
    (0, 0), im.FactorScale("ProfJB_0026_Trunk.png",0.5),
    (0, 0), im.FactorScale("ProfJB_0025_Head.png",0.5),
    (0, 0), "jb eyes normal",
    (0, 0), "jb mouth speaking",
    (0, 0), "jb right arm explaining",
    (0, 0), "jb left arm apple",
    )

image jb mad speaking = LiveComposite(
    (1000, 800),
    (0, 0), im.FactorScale("ProfJB_0026_Trunk.png",0.5),
    (0, 0), im.FactorScale("ProfJB_0025_Head.png",0.5),
    (0, 0), "jb eyes mad",
    (0, 0), "jb mouth speaking mad",
    (0, 0), "jb right arm mad",
    (0, 0), "jb left arm apple",
    )

image jb skeptical = LiveComposite(
    (1000, 800),
    (0, 0), im.FactorScale("ProfJB_0026_Trunk.png",0.5),
    (0, 0), im.FactorScale("ProfJB_0025_Head.png",0.5),
    (0, 0), "jb eyes skeptical",
    (0, 0), "jb mouth tilted",
    (0, 0), "jb right arm rest",
    (0, 0), "jb left arm chin",
    )

image jb eyes mad:
    im.FactorScale("ProfJB_0013_Eyes-Mad.png",0.5)

image jb eyes normal:
    im.FactorScale("ProfJB_0017_Eyes-Neutral.png",0.5)
    choice:
        3.5
    choice:
        2.0
    choice:
        1.0
    im.FactorScale("ProfJB_0014_Eyes-Shut.png",0.5)
    .25
    repeat

image jb eyes skeptical:
    im.FactorScale("ProfJB_0012_Eyes-Skeptical.png",0.5)

image jb mouth shut: 
    im.FactorScale("ProfJB_0023_Mouth-Shut.png",0.5)

image jb mouth ooh:
    im.FactorScale("ProfJB_0021_Mouth-Ooh.png",0.5)

image jb mouth aah:
    im.FactorScale("ProfJB_0022_Mouth-Aah.png",0.5)

image jb mouth smile:
    im.FactorScale("ProfJB_0024_Mouth-Smile.png",0.5)

image jb mouth tilted:
    im.FactorScale("ProfJB_0018_Mouth-Tilted.png",0.5)

image jb mouth angry:
    im.FactorScale("ProfJB_0020_Mouth-Angry.png",0.5)

image jb mouth frown:
    im.FactorScale("ProfJB_0019_Mouth-Frown.png",0.5)

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
    im.FactorScale("ProfJB_0001_RightArm-Waist.png",0.5)

image jb right arm up:
    im.FactorScale("ProfJB_0009_RightArm-5.png",0.5)

image jb right arm fist:
    im.FactorScale("ProfJB_0003_RightArm-Fist-2.png",0.5)

image jb right arm explaining:
    choice:
        "jb right arm rest"
        choice:
            2.0
        choice:
            1.0
    choice:
        "jb right arm up"
        choice:
            1.5
        choice:
            .7
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
    im.FactorScale("ProfJB_0000_LeftArm-Apple.png",0.5)

image jb left arm chin:
    im.FactorScale("ProfJB_0010_LeftArm-Chin-1.png",0.5)
    .5
    im.FactorScale("ProfJB_0011_LeftArm-Chin-2.png",0.5)
    .5
    repeat

label start:

    scene bg room

    #show jb base
    #show jb speaking
    #show jb skeptical
    show jb mad speaking

    prof_jb "Hello! I am Prof. Jacky Baltes."

    prof_jb "I hope you enjoy this course"

    return
