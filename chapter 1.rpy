label ch1:
    stop music fadeout 4.0
    scene black
    play music audio.t5
    $ config.rollback_enabled = False
    
    $ mc = renpy.input("Please insert your name")
    
    $ mc = mc.strip()
    
    "I woke up with a yawn"
    
    "It’s gonna be boring a year."
     
    "Alone... I wonder when my waifu will be alive"
    
    m "[mc], I made your breakfast."
    
    mc "Okay, Mom."
    
    "I went out with my everyday school uniform."
    
    "I stared at my room, looks like my collection of anime and vocaloids is good enough for bragging."
    
    "I shook my head before combing my hair."
    
    "I went down. In the dinner room there is a girl with long straight black hair, with dignified aura and a mature body."
    
    r "[mc]!"
    
    "She is my step-sister who is well-known, blablabla prodigy. Blablabla your beautiful student council president."
     
    "I wonder what I should become..."
    menu:
        "Either way, I decide that I'll..."
        
        "Your cute Otouto Main Character!": # 1
            
            jump sub1
        
        "Whose IDEA PUT THAT OTHER CHOICE.": # 2
            
            jump route1
  
label route1:
    "Anyway, my mind aside."
    
    mc "Good Morning, Rina-nee."
    
    r  "Morning,[mc]!"

    r  "You’re really early today."
    
    "*Give a plate of fried rice*"
    
    mc "It's the first day after all."
  
    menu:
        mc "Actually..."
        
        "Let's go to school together.": # 3
            
            jump sub3 
        
         "Will you be busy?": # 4
            
            jump route2
label route2:
    r "Yeah, I forgot. Sorry [mc], I'll be busy today since I have become the student council president."
    
    mc "Oh, okay. Guess, gotta go."
   
    r "Alright, see you later [mc]."
    
    jump route3        
  
label route3:
    
    "I went out after drinking a cup of good black coffee."
    
    "I will need it after all the things I did last night."
    
    "Anime, MMO, DOTA, LOL, MONSTER HUNTER!"
    
    "I will surely need that black coffee."
    
    #scene unknown
    
    "As I went out to see a petite body with white hair and cute face staring at me."
    
    "She waved her small cute hand at me with innocent smile."
    
    s "Good morning, [mc]-nya~"
    
    "Yep, a loli whose age I will not tell you guys."
    
    "This girl is second years of middle school."
    
    menu:
        "Good morning, Shiro-chan.": #choice 13
            
            jump sub14
        
        "Good morning, cute kitty.": #choice 14
            
            jump sub15
            
        "You're cute, be my Imouto!": #choice 15
            
            jump sub15

label sub14:
    s "*Smile* Morning [mc]-senpai!"
    
    jump route4

label sub15:
    s "*Blush* Hmm, don't treat me like a kitty! *Still happy being pat*"
    
    jump route4
    
label sub15:
    s "*Blush* Umm...No, Rina-neesan gonna get angry."
    
    jump route4
    
label route4:
    s "Anyway, can I go school with you?"
    
    menu:
        "Let's go!": 
            
            jump sub16
        
        "Is it okay?": 
            
            jump route5
        
        "Let's go-nya~": 
            
            jump sub17
        
label sub16:
   s "Let's go!"
   
   jump route6
    
label route5:
    mc "I believe Shiro-chan is an exemplary student. Maybe you forgot something?"
    
    jump route7
    
label sub17:
    s " Rawr~ *Innocent smile radiating*"
    
    jump route6
    
label route6:
    "As I went to school, Shiro hugged my right arm happily."
    
    "I pet her head softly"
    
    s "*Rub her head at [mc]'s arm affectionately"
    
    "After arrived there, Shiro and me parted away."
    
    jump route8
    
label route7:
    
    "After arriving there, I stared at the blue sky."
     
    jump route8

label route8:
    "I went to the classroom and sat at Main character's usual seat."
    
    "Back on the right side next to the window."
    
    mc "Hah~"
    
    mc "This is boring..."
    
    g "Why you sighing? It's still early in the morning."
    
    mc "I'm bored, I want to do something!~"
    
    g "Well, suit yourself."
    
    mc "Anyway... Amani."
    
    a "What is it?"
    
    mc "Is there any homework?"
    
    a "Nope."
    
    "..."

    "Recess"
    
    "Nothing can beat..."
    
    "Fried noodle bread!"
    
    "I went to Cafeteria to buy the food."
    
    "But... If I have to say."
    
    menu:
        "This is quite good food.":
        
            jump route9
        
        "I want Yakiniku Odon.":

            jump route9
        
        "Just milk is good enough.":

            jump route9
    
label route9:
    "I'm full anyway. I'll buy that thing later."
    
    #bell ring
    
    "Welp, the next class started now."
    
    "I ran with full strength."
    
    mc "Welp, teacher's gonna get angry!!"

    a "Hurry [mc]!! Teacher is on the way to the class."

    "Teacher is on the way with stern face"

    mc "Crap! Go go go!!"   

    a "*Nod**Nod* Roger that Sir!"

    "We rushed inside to the class"

    "Then the teacher went in"
    
    mc "Life secured"

    "Terrorist Win... Wait this is not a game."

    "Well never mind that. I should focus to the class right now"
    #Insert bell ring
    "The class ended."
    
    "As I went out with a sigh."
    
    "I wonder what I should do."
    
    "Maybe I should visit to dojo."

    "I went to dojo."
    
    #music

    #scene
    
    " As I went inside the dojo, which is near to my house I met Amani and Rina-nee inside with an old man."
    
    r "Hah!"
    
    "Rina's right fist moved forward fast."
    
    r "Hah!"
    
    "Rina's left fist moved forward fast."
    
    "Yep, my sister is good at almost everything. Except she doesn't have a boyfriend."
    
    "Wonder why..."
    
    a "[mc]! You're late today!"
    
    mc "Ah, sorry. I had some other things to do."
    
    r "*laugh* Must be your homework, right?"
    
    mc "I..."
    
    "Welp, she's right."
        
    mc "I forgot to do..."
    
    r "Do you want me to help you?~"
    
    mc "Umm..."
    
    d "It's okay, your sister wanted to do it right?~"
    
    "What the f..."
    
    d "It's okay you're a mature boy after all. Huehuehue."
    
    "Why is the laugh so lame?"
    
    an "Don't remember, she is your only sister!"
    
    "You mean... st-"
    
    d "Stepsister, right. He can marry her, you know?"
    
    "Hmm..."
    
    menu:
        "Listen to devil of lust.":
        
            jump bad1
        
        "Listen to angel of anime (Not sure what the hell does that mean whatever it is)":
        
            jump route11
   
label route11:
    "I know she wanted to do something but..."
    
    mc "I will be fine! I mean, even Amani can help me."
   
    r "Oh."
    
    r "Okay... *Dejected*"
    
    o "Oh, you came late today. Down to 150."
    
    mc "NANI!?"
    
    o "Just do it!"
    
    "Behind the Dojo."
    
    s "According to keikaku. Fufufu~ *Innocent loli aura released*"
    
    "After quite while..."
    
    mc "149...... 15-.... 150.... *fall to ground."
    
    s "Jii-chan![mc] not moving!"
    
    o "He will be fine! Maybe..."
    
    s "Uuuu~~ *Started tearing up*"
    
    o "*Extreme critical hit received*[s],Grandpa. I’m so sorry! *hug [s]*"
    
    s "I Hate you!"
    
    o "*Hugs his own legs at some corner* Sorry."
    
    "After..." 
    "(Visualist: JUST STOP SKIP DAMMIT!) (K!) (THE FISH)"
    "(After a long time, the author become retard and do dab all the anime he watched all the time. The end)"
    
    "After a long time Im passed out."
    
    mc "Hmm... What happened?"
    
    s "Hmm? Oh you're tired... So... *Fidget* *fidget*"
    
    mc "Hmm.... Ah, the pillow lap is good though."
    
    s "*Blush* Is i-it good?"
    
    mc "Yup."
    
    "I stood up and started my practice."
    
    o " Go spar with [r]."
    
    mc "Alright."
    
    r "Will you be okay with your school uniform?"
    
    mc "Of course. I will be fine with the uniform."
    
    "I tied out the shirt with a smirk."
    
    "Old man Kukichi watched us with anticipation."
    
    "I moved to middle grounds facing Rina."
    
    mc "Rina-nee, you move first."
    
    r "Well, don't regret it!"
    
    "*Fush*"
    
    "Fast!"
    
    "A right fast jab appeared."
    
    "I moved my head to side avoid the jab."
        
    "Rina swang left hand aiming [mc]'s stomach"
    
    "I moved my hand stop her swing and uppercut with my other hand targeting Rina-nee."
    
    "Rina jumped back while her right hand block the uppercut."
    
    r "You're still like a demon as usual."
    
    mc "Is that praise?"
     
    "Rina run towards me before lowering her body in order to tackle my leg down."
     
    "I jumped in the air but Rina swang her hand straight to my face."
     
    "I moved my head few breaths earlier than her before I landed on the ground."
     
    "I instinctively hold her karate's uniform and throw her in air with a perfect fluid movement."
     
    "Rina flew in air before landing with a thud."
     
    r "*rubs head* Ouch! That hurts!"
     
    mc "A moment hesistation equal a moment live fly away."
     
    o "Hahahaha! As expected of [mc]! I have great expectations for your future in martial arts."
     
    mc "Of course!. *ready both hands on side and breath in and exhale lightly*"
    
    a "Splendid as always,[mc]!"
     
    s "Yeah!"
     
    a "Seeing Rina couldn't contend with you meaning she is not as perfect as she seems to be."
     
    r "Rude!"
     
    "They looked each other and laughed."
     
    "I laughed with them."
     
    #Scene unknown
     
    "I return home sluggishly."
     
    r "Are you okay?"
     
    mc "Heh, just tired though."
     
    r "Please take care of your health okay?"
     
    mc "Of course. *smile*"
     
    "I went inside my room."
     
    "Suddenly, my phone rings."
     
    "'Why don’t you video call me? Hmph!'"
     
    mc "Ah..."
     
    "I replied and went to bath after that."
    
    "I replied to Ellyn, my internet bestfriend."
     
    mc "'Sorry, Ellyn. It was a quite busy day.'"
    
    e "'It's fine.'"
    
    e "'I know you had a busy day. Good night,[mc].'"
    
    "I closed my phone and went to sleep."
    
    "It was a busy day..."
    
    "..."
    
    "Thanks for playing. This novel is still beta."
    
    stop music fadeout 3.0
    return