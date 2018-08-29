label ch1:
    stop music fadeout 4.0
    scene black
    play music audio.t5
    $ config.rollback_enabled = False
    
    $ mc = renpy.input("Please insert your name")
    
    $ mc = mc.strip()
    
    "I woke up with a yawn"
    
    "It’s gonna be boring year today."
    
    "Alone... I wonder when my waifu will be alive"
    
    m "[mc],I made your breakfast."
    
    mc "Okay,mom."
    
    "I went out with your everyday school uniform."
    
    "I stared at my room,looks like my collection of anime and vocaloids is good enough for bragging."
    
    "I shook my head before comb my hair"
    
    "I went down.In the dinner room there is a girl with long straight black hair, with dignified aura and mature body."
    
    r "[mc]!"
    
    "She is my step-sister who is well-known, blablabla prodigy. Blablabla your beautiful student council president"
     
    "I wonder what should I become..."
    menu:
        "Either way, I decide that I'll..."
        
        "Your cute Otouto Main Character!": #choice 1
            
            jump retard1
        
        "Whose IDEA PUT THAT OTHER CHOICE.": #choice 2
            
            jump notretard1
            
            
label retard1:
    "I will rely on my beatiful Rina-nee!"
    
    "And this visual novel will become about me with her!"
    
    "I wonder should I tell Author?"

    jump done1

label notretard1:
    
    jump done1
    
    
label done1:
    "Anyway,my mind aside."
    
    mc "Good Morning,Rina-nee."
    
    r  "morning,[mc]!"
    r  "You really early today."
    
    "*Give a plate of fried rice*"
    
    mc "It's first day after all."
  
    menu:
     mc "Actually..."
        
     "Let's go to school together.": #choice 3
            
            jump choice3
        
     "Will you be busy?": #choice 4
            
            jump choice4
    
label choice3:
    r "Hmm,why?"
    
    jump done2

label done2:
    
    menu:
     mc "Umm..."
        
     "Because I want to go to school with you.": #choice 5
            
            jump done3
        
     "Because you're my sister.": #choice 6
            
            jump done3
        
label done3:
    r "*blush*"
    
    m "[mc],stop flirting your sister."
    
    mc "sorry,mom."
    
    r "Ehem,I'll go with you today."
    
    "YES, I’m with perfect student!"
    
    "who can face me!?"
    
    "I went out after drink a cup of good black coffee."
    
    "I will need after all the things I did last night."
    
    "Anime,MMO,DOTA,LOL,MONSTER HUNTER!"
    
    "I will surely need that black coffee."
    
    #scene
    
    "As I went out to see a petite body with white hair and cute face staring at me."
    
    "She waved her small cute hand at me with innocent smile."
    
    mc "Shiro-chan! Boujour (Suddenly speak French)"
    
    r "[mc], why speak french? Do you know any other words?"
    
    mc "*flustered* I’m still learning! … Maybe."

    r "*Sigh* If you want, I can teach you French."
    
    menu:
        mc "Not interested, because..."
        
        "Martial arts all the way!": #choice 7
            
            jump choice7
            
        "I'll beats Bill Gates!": #choice 8
        
            jump choice8
            
        "I Like to Anime rush.": #choice 9
    
            jump choice9

label choice7:
    s "Eh~"
    
    s "[mc], you really did it?"
    
    r "I can't overtake [mc] in that part."
    
    jump done5
    
label choice8:
    S "Eh~, [mc] you really did it?"
    
    mc "Not yet, but I will!"
    
    r "Hmm~, how you beat Bill gates?"
    
    mc "By creating New concept, theory and invention!"
    
    s "Is he kidding, Rina-neesan."
    
    r "It’s kinda hard but I know [mc] can do it if he wants to!"
    
    jump done5
    
label choice9:
    s "Eh~, [mc] you really did it?"
    
    mc "Hmph! Of course!"
    
    r "I have no doubt about this."
    
    mc "Hmph! *Damn proud face*"

    jump done5
    
label done5:
    s "Anyway,can i go with you to school?"
    
    mc "*Thinking*"
    
    menu:
        "Let's go!": #choice 10
            
            jump choice10
        
        "Is it okay?": #choice 11
            
            jump choice11
        
        "Let's go-nya~": #choice 12
            
            jump choice12
        
label choice10:
   s "Let's go!"
   
   jump done7
    
label choice11:
    mc "I believe Shiro-chan is exemplary student. Maybe you forgot something?"
    
    jump done8
    
label choice12:
    s " Rawr~ *innocent smile radiating*"
    
    jump done7
    
label done7:
    "Rina-nee,Shiro and me went to school."
    
    "We parted away after long happy chat with each other on school."
    
    jump storyline1

label done8:
    s "Ah! Sorry [mc]-senpai! I need to give a speech at assembly for freshmen today!"
    
    mc "It's fine."
    
    "Shiro ran in hurry."
     
    r "Well, let's go,[mc]."
     
    "after that, we parted away."
     
    jump storyline1
     
label choice4:
    r "Yeah,I forgot. Sorry,[mc], I'll be busy today since i have become student council president."
    
    mc "Oh,okay. Guess, gotta go."
   
    r "Alright,see you later [mc]."
    
    jump done4
    
label done4:
    
    "I went out after drink a cup of good black coffee."
    
    "I will need after all the things I did last night."
    
    "Anime,MMO,DOTA,LOL,MONSTER HUNTER!"
    
    "I will surely need that black coffee."
    
    #scene unknown
    
    "As I went out to see a petite body with white hair and cute face staring at me."
    
    "She waved her small cute hand at me with innocent smile."
    
    s "Good morning,[mc]-nya~"
    
    "Yep, a loli whose age I will not tell your guys."
    
    "This girl is second year of middle school."
    
    menu:
        "good morning,Shiro-chan.": #choice 13
            
            jump choice13
        
        "Good morning,cute kitty.": #choice 14
            
            jump choice14
            
        "You're cute,be my imouto!": #choice 15
            
            jump choice15

label choice13:
    s "*Smile* Morning [mc]-senpai!"
    
    jump done6

label choice14:
    s "*Blush* Hmm, don't treat me like a kitty! *Still happy being pat*"
    
    jump done6
    
label choice15:
    s "*Blush* Umm...No,Rina-neesan gonna get angry."
    
    jump done6
    
label done6:
    s "Anyway,can I go school with you?"
    
    menu:
        "Let's go!": #choice 16
            
            jump choice16
        
        "Is it okay?": #choice 17
            
            jump choice17
        
        "Let's go-nya~": #choice 18
            
            jump choice18
        
label choice16:
   s "Let's go!"
   
   jump done9
    
label choice17:
    mc "I believe Shiro-chan is exemplary student. Maybe you forgot something?"
    
    jump done10
    
label choice18:
    s " Rawr~ *innocent smile radiating*"
    
    jump done9
    
label done9:
    "As I went to school, Shiro hugged my right arm happily."
    
    "I pet her head softly"
    
    s "*rub her head at [mc]'s arm affectionately"
    
    "After arrived there, Shiro and me parted away."
    
    jump storyline1
    
label done10:
    
     "After arrived there, I stared at blue sky."
     
     jump storyline1

label storyline1:
    "I went to classroom and sit at Main character's usual seat."
    
    "Back on the right side next to window."
    
    mc "Hah~"
    
    mc "This is boring..."
    
    g "Why you sighing? It's still early in the morning."
    
    mc "I'm bored, i want to do something!~"
    
    g "Well, suit yourself."
    
    mc "Anyway... Amani."
    
    a "What is it?"
    
    mc "Is there any homework?"
    
    a "nope."
    
    ""
    "Recess"
    
    "Nothing can beat..."
    
    "Fried noodle bread!"
    
    "I went to canteen to buy the food."
    
    "But... If i have to say."
    
    menu:
        "This quite good food.":
        
        jump full1
        
        "I want yakiniku Odon.":
        jump full1
        
        "Just milk is good enough.":
        jump full1
    
label fullalready1:
    "I'm full anyway. I'll buy that thing later."
    
    #bell ring
    
    "Welp, the next class started now."
    
    "I ran with full strength."
    
    mc "Welp, teacher's gonna get angry!!"
    
    #Insert bell ring
    
    "The class ended."
    
    "As I went out with a sigh."
    
    "I wonder what should I do."
    
    menu:
        "Dojo":
        
        jump dojo1
        
        "Home Sweet Home":
        
        jump home1
        
label dojo1:
    "I went to dojo."
    
    #music

    #scene
    
    " As i went inside dojo, which is near to my house I met Amani and Rina-nee inside with an old man."
    
    r "Hah!"
    
    "Rina's right fist moved forward fast."
    
    r "Hah!"
    
    "Rina's left fist moved forward fast."
    
    "Yep,my sister is good at almost everything. Except she doesn't have boy friend."
    
    "Wonder why..."
    
    a "[mc]! You're late today!"
    
    mc "Ah, sorry. I have some other things to do."
    
    r " *laugh* Must be your homework, right?"
    
    mc "I..."
    
    menu:
        "Welp, she's right."
        
        jump homeworknotdone1
        
        "I finished it."
        
        jump homeworkdone1
        
label homeworknotdone1:
    mc "I forgot to do..."
    
    r "Do you want me to help~ you?~"
    
    mc "Umm..."
    
    d "It's okay, you sister wanted to do it right?~"
    
    "What the f..."
    
    d "It's okay you're mature boy after all. huehuehue."
    
    "Why the laugh is so lame?"
    
    an "Don't remember, she is your only sister!"
    
    "You mean... st-"
    
    d "Stepsister, right. He can marry her, you know?"
    
    "Hmm..."
    
    menu:
        "Listen to devil of lust."
        
        jump devil1
        
        "Listen to angel of anime (Not sure what the hell is that mean whatever it is)"
        
        jump angelofwhateverisit1
        
label devil1:
    
    "Well..."
    
    "BAM!"
    "*fly few feet in air before hit the wooden tiles with a thud."
    
    "18 fatality"
    
    "Make sure to not think this novel as hentai all the time"
    
    "Noobegg is here as author! In your face!!! Pervert!!!"
    
    stop music fadeout 3.0
    return
    
label angelofwhateverisit1:
    "I know she wanted to do something but..."
    

    stop music fadeout 3.0
    return
                                                                                                     
    
        
                                                           
                                                           
               
               