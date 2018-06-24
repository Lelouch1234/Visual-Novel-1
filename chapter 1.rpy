label ch1:
    stop music fadeout 4.0
    scene black
    play music audio.t5
    
    "..."
    
    "What a daily life I have right now."
    
    "Alone..."
    
    g "Hi there!"
    
    "Huh?"
    
    g "Can I sit here?"
    
    "I just stay quiet and not answering her question."
    
    "Then she sitdown in front of me."
    
    g "Can I know your name?"
    
    "She ask my name??"
    menu:
        "Either way, I decide that I'll..."
        
        "Tell her my name.":
            
            jump choice1
        
        "Go away from her.":
            
            jump choice2
            

label choice1:
    $ mc = renpy.input("Please insert your name")
    
    $ mc = mc.strip()
    
    mc "My name is [mc]."

    jump done1

label choice2:
    "I stand up in front of her and leave her as fast as I can."
            
    "That girl look me go away from her and look down."
            
    "I guess that is the best way for her to leave me alone."
    
    "I keep running without looking back..."
    
    "Keep running..."
    
    "BAD END"
    
    n "I never though this ending so fast at first chapter. Well, try to play again."
    
    return
    
label done1:
    g "Nice to meet you, [mc]"
    
    mc "Y-yeah, me too."
    
    "This is first time I talked with girl."
    
    "I cant bring myself to see her face."
    
    g "Are you ok [mc]?"
    
    mc "Yeah, Im good."
    
    "Maybe I should ask her name since she already ask my name"
    
    mc "Can I know your name?"
    
    g "Oh, I forgot to intro myself. My Bad"
    
    a "My name is [a] and we are classmates"
    
    "Eh?"
    
    "Classmates?"
    
    "And her name is Alice, Alice, Alice..... Ah I remember her. Her sit is beside of me."
    
    a "[mc]?"
    
    mc "Oh, Im sorry. I forgot about you since I never talked with a girl"
    
    a "Ah I see. So this is the first time you talked with a girl like me?"
    
    mc "Yes *Blushing*"
    
    a "Hahaha. You are so cute when you blushing"
    
    "She keep laugh at me for a few second and I stay quiet for awhile."
    
    "Then situations getting awkward for me."
    
    a "Then can you be my friend, [mc]?"
    
    "This will change my daily life."
    
    "My life with a girl..."
    
    "Eh, What the heck Im thinking?"
    
    a "[mc]?"
    
    mc "Oh sorry. Im just thinking something."
    
    a "You still not answer my question yet."
    
    mc "Ah sure."
    
    "This is the first day I make a friend with a girl."
    
    "I guess what happen tomorrow...."
    
    "END OF THE DEMO"
    
    n " I still dont know what story I could make since Lost still not give his story yet. Well stay tuned."
    
    stop music fadeout 3.0
    
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    