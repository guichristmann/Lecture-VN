# Redefine default transforms for our character size

#transform reset:
#    alpha 1 rotate None zoom 1 xzoom 1 yzoom 1 align (0, 0) alignaround (0, 0) subpixel False size None crop None

# These are positions that can be used inside at clauses. We set
# them up here so that they can be used throughout the program.
transform left:
    xpos 0.0 xanchor 0.0 ypos 1.0 yanchor 1.0

transform right:
    xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 1.0

transform center:
    xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0

transform fitscreen:
    zoom 0.333

transform halfsize:
    zoom 0.5

transform normalsize:
    zoom 1.0

transform offscreenleft:
    xpos -0.1 xanchor 1.0 ypos 1.0 yanchor 1.0

transform offscreenright:
    xpos 1.1 xanchor 0.0 ypos 1.0 yanchor 1.0
