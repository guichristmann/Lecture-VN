define jb = Character("Prof. Jacky Baltes", color="#06799f", callback=speaker("jb"))
define gc = Character("Student G.C.", color="#069f67", callback=speaker("gc"))
define msG = Character("Miss G.", color="#069f67", callback=speaker("msG"))

label start:

    scene bg neutral with fade

    show jb neutral at center with dissolve

    # Prof. Jacky's Introduction
    jb "Hello! I am Prof. Jacky Baltes."
    show jb neutral:
        linear 1.0 left

    show gc neutral at right with dissolve
    pause 1.0

    gc "And I'm GC."
    gc "But you've already met us!"
    show gc smile
    jb "Now, we want to introduce you to someone else."

    show gc neutral:
        linear 1.0 left

    show msG neutral:
        offscreenright
        linear 1.0 right

    pause 1.25

    show msG neutral
    msG "Hello! Nice to meet you!"
    show msG mad
    msG "My name is Miss G."

    show msG curious explaining
    msG "I'm new here, but I'm also looking forward to see this project in action!"
    show msG neutral
    msG "See you around!"
