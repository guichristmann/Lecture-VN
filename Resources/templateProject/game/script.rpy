define jb = Character("Prof. Jacky Baltes", color="#06799f", callback=speaker("jb"))
define gc = Character("Student G.C.", color="#069f67", callback=speaker("gc"))

label start:

    scene bg neutral with fade

    show jb neutral at center with dissolve

    pause 1.0

    # Prof. Jacky's Introduction
    jb "Hello! I am Prof. Jacky Baltes."
    jb "This project doesn't contain anything yet."
    jb "You can take a look at the imported slides."
