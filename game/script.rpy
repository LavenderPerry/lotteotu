default right_button = True

define c = Character("Carp")
define r = Character("Radiation")

label start:
    scene bg carpexe
    show carp happy at truecenter

    c "Hello! Push the button! I would myself but it is challenging with my fins."

menu:
    "initiate cameras":
        jump button_pressed

label button_pressed:
    $ right_button = False
    show break at right onlayer overoverlay
    play sound "break.mp3"
    pause
    show carp mad at truecenter
    show text "{shake}{size=200}{color=#f00}{b}WHAT THE FUCK{/b}{/color}{/size}{/shake}"
    pause
    hide text
    c "I said push the button not destroy the entire screen!"
    c "Seems like it still got pushed though."
    show carp happy at truecenter
    c "It's fine, I suppose it is your screen, not mine. Now I can show you my life's work!"

    scene bg lineinit
    show text "Press ;?$#^& to exit fullscreen." at top
    show carp happy at left
    c "Oh good, the camera is working!"
    hide text
    c "What you are about to see is going to change the world forever."
    c "Whether it does in the way I was intending and works correctly... we will find out soon."
    c "But anyways I just need you to push one more button."
    c "Oh, you can't see it?"
    c "Right, the screen. That is your own fault really, but because I really need this button pushed I will move it for you."

menu:
    "start the line":
        jump line_start

label line_start:
    c "Good, you didn't break your screen this time. You're getting better at this! Although not breaking your own screen is a pretty low bar..."
    c "Let's see if this works."
    c "Oh right, I forgot to tell you. I've calculated that there is about a 60\% chance this thing explodes and wipes out the entire planet!\n{shake}Exciting, right?{/shake}"
    c "Don't look so worried. I like those odds!"
    show line vertical
    play sound "line.mp3"
    pause
    show text "{size=200}{b}{i}IT WORKS!{b}{i}{/size}"
    pause
    show text "{color=#f0f}C:\\Users\\carp\\Documents\\experiment.exe -- \n{b}IMPORTANT SAFETY MESSAGE: LOOK OUT FOR LARGE QUANTITIES OF RADIATION.{/b}{/color}"
    pause
    hide text
    pause
    c "I suppose I should explain myself."
    c "I'm firing a ray as far out into the universe as I can."
    c "I'm hoping it will reach to the end of the universe, or even past that."
    c "Also it will destroy Pluto, because I want to."
    c "Who knows what is beyond our universe?"
    c "I just hope nothing goes wrong..."

    scene bg radiationexe
    pause
    r "Hi."
    r "You all really decided to go to the end of the universe."
    r "Well, nothing here. Just empty space."
    r "And me, I suppose. I am so glad to finally have someone to talk to."

    scene bg bsod
    play sound "end.mp3" loop
    pause
    show text "{shake}{size=200}{color=#0f0}{b}NOOOOOOOO{/b}{/color}{/size}{/shake}"
    pause

    return
