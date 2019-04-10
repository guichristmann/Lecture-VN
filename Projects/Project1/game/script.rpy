
define jb = Character("Prof. Jacky Baltes", color="#06799f", callback=speaker("jb"))
define gc = Character("Student G.C.", color="#069f67", callback=speaker("gc"))

label start:
    show jb neutral at center with dissolve
    pause 1.0
    # Prof. Jacky's Introduction
    jb "Hello! I am Prof. Jacky Baltes."
    jb "This project describes Machine Learning - Decision Trees."
    jb "You can take a look at the imported slides."

label START:
    scene bg START with fade
    jb "This slide is called START"
    

label introduction:
    scene bg introduction with fade
    jb "This slide is called introduction"
    

label slide_00003_frag_00000:
    scene bg slide_00003_frag_00000 with fade
    jb "This slide is called slide_00003_frag_00000"
    

label slide_00004_frag_00000:
    scene bg slide_00004_frag_00000 with fade
    jb "This slide is called slide_00004_frag_00000"
    

label background:
    scene bg background with fade
    jb "This slide is called background"
    

label hierarchy1:
    scene bg hierarchy1 with fade
    jb "This slide is called hierarchy1"
    

label entropy:
    scene bg entropy with fade
    jb "This slide is called entropy"
    

label example:
    scene bg example with fade
    jb "This slide is called example"
    
