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
    
    m "[mc], I made you breakfast."
    
    mc "Okay, Mom."
    
    "I went out with my everyday school uniform."
    
    "I stared at my room, looks like my collection of anime and vocaloids is good enough for bragging."
    
    "I shook my head before combing my hair."
    
    "I went downstairs. In the dinning room there's a girl with long straight black hair, with a dignified aura and a mature body."
    
    r "[mc]!"
    
    "She is my step-sister who is popular, blahblahblah a prodigy, and blahblahblah our beautiful student council president."
     
    "I wonder what I should become..."
    menu:
        "Either way, I think that I'll be..."
        
        "Your cute Otouto Main Character!": # 1
            
            jump sub1
        
        "Who PUT THAT OTHER CHOICE!": # 2
            
            jump route1
  
label route1:
    "Anyway, my mind aside."
    
    mc "Good Morning, Rina-nee."
    
    r  "Morning,[mc]!"

    r  "You’re really early today."
    
    "*I take the plate of fried rice she offers*"
    
    mc "It's the first day after all."
  
    menu:
        mc "Actually..."
        
        "Let's go to school together.": # 3
            
            jump sub3 
        
        "Will you be busy?": # 4
            
            jump route2
label route2:
    r "Yeah, I forgot. Sorry [mc], I'l be busy today, I've had a lot to after becoming the student council president."
    
    mc "Oh, okay. Guess I will get going now."
   
    r "Alright, see you later [mc]."
    
    jump route3        
  
label route3:
    
    "I went out after drinking a good cup of black coffee."
    
    "I will need it after all the things I did last night."
    
    "Anime, MMO, DOTA, LOL, MONSTER HUNTER!"
    
    "That black coffee will definitely come in handy."
    
    #scene unknown
    
    "As I went out i saw a petite body with white hair. Her cute face was staring right at me."
    
    "She waved her small and fragile hand at me with a innocent smile to follow."
    
    s "Good morning, [mc]-nya~"
    
    "Yep, a loli whose age I am not going to tell you guys."
    
    "This girl is in her second year of middle school."
    
    menu:
        "Good morning, Shiro-chan.": #choice 13
            
            jump sub14
        
        "Good morning, cute kitty.": #choice 14
            
            jump sub15
            
        "You're cute, be my Imouto!": #choice 15
            
            jump sub16

label sub14:
    s "*Smiles* Morning [mc]-senpai!"
    
    jump route4

label sub15:
    s "*Blushes* Hmm, don't treat me like a kitty! *She is still happy to be petted*"
    
    jump route4
    
label sub16:
    s "*Blushes* Umm...No, Rina-neesan is gonna get angry if I do."
    
    jump route4
    
label route4:
    s "Anyway, can I go school with you?"
    
    menu:
        "Let's go!": 
            
            jump sub17
        
        "Is that okay?": 
            
            jump route5
        
        "Let's go-nya~": 
            
            jump sub18
        
label sub17:
   s "Let's go!"
   
   jump route6
    
label route5:
    mc "I believe Shiro-chan is an exemplary student. Maybe I am forgetting something?"
    
    jump route7
    
label sub18:
    s " Rawr~ *Innocent smile radiating*"
    
    jump route6
    
label route6:
    "As I went to school, Shiro hugged my right arm happily."
    
    "I pet her head softly"
    
    s "*Rubs her head at [mc]'s arm affectionately*"
    
    "After arriving there, Shiro and me parted ways."
    
    jump route8
    
label route7:
    
    "After arriving there, I stared up at the blue sky."
     
    jump route8

label route8:
    "I went to the classroom and sat at the Main character's usual seat."
    
    "At the Back of the classroom on the right side next to the window."
    
    mc "Hah~"
    
    mc "This is boring..."
    
    g "Why you sighing? The day just started."
    
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
    
    "I went to Cafeteria to go get some."
    
    "But... If I have to say."
    
    menu:
        "This is some pretty good food.":
        
            jump route9
        
        "I'd rather have Yakiniku Odon.":

            jump route9
        
        "Just milk is good enough.":

            jump route9
    
label route9:
    "I'm full right now though, so I'll get some later."
    
    #bell ring
    
    "Welp, the next class started now."
    
    "I ran with full strength."
    
    mc "Geez, teacher's gonna get angry!!"

    a "Hurry [mc]!! Teacher is on the way to class."

    c "Teacher is on the way with a stern face"

    mc "Crap! Go go go!!"   

    a "*Nod**Nod* Roger that Sir!"

    "We rushed inside to the class"

    "Then the teacher went in"
    
    mc "Life secured"

    "Terrorists Win... Wait this is not a game."

    "Well never mind that. I should focus on the class right now"
    #Insert bell ring
    "The class ended."
    
    "I went out with a sigh."
    
    "I wonder what I should do."
    
    "Maybe I should visit the dojo."

    "I left to the dojo."
    
    #music

    #scene
    
    "As I went inside the dojo, which is nearby my house, I met Amani and Rina-nee inside with an old man."
    
    r "Hah!"
    
    "Rina's right fist moved forward fast."
    
    r "Hah!"
    
    "Rina's left fist moved forward fast."
    
    "Yep, my sister is good at almost everything. Except she doesn't have a boyfriend."
    
    "Wonder why..."
    
    a "[mc]! You're late today!"
    
    mc "Ah, sorry. I had some other things to do."
    
    r "*laughs* Must be your homework, right?"
    
    mc "I..."
    
    "Welp, she's right."
        
    mc "I did forget to do it..."
    
    r "Do you want me to help you?~"
    
    mc "Umm..."
    
    d "It's okay, your sister wants to do it right?~"
    
    "What the f..."
    
    d "It's okay you're a mature boy after all. Huehuehue."
    
    "Why is that laugh so lame?"
    
    an "Don't worry, she is your only sister!"
    
    "You mean... st-"
    
    d "Stepsister, right. He can marry her, you know?"
    
    "Hmm..."
    
    menu:
        "Listen to the devil of lust.":
        
            jump bad1
        
        "Listen to  the angel of anime (Whatever the hell that is)":
        
            jump route11
   
label route11:
    "I know she wanted to do something but..."
    
    mc "I will be fine! I mean, even Amani can help me."
   
    r "Oh."
    
    r "Okay... *Rejected*"
    
    o "Oh, you came late today. Get down and give me a 150."
    
    mc "NANI!?"
    
    o "Just do it!"
    
    "Behind the Dojo."
    
    s "According to keikaku. Fufufu~ *Innocent loli aura released*"
    
    "After quite a while..."
    
    mc "149...... 15-.... 150.... *falls to the ground.*"
    
    s "Jii-chan![mc] isn't moving!"
    
    o "He'll be fine! Probably..."
    
    s "Uuuu~~ *Starts to tear up*"
    
    o "*Extreme critical hit received*[s],Grandpa. I’m so sorry! *hug [s]*"
    
    s "I Hate you!"
    
    o "*Hugs his own legs at some corner* Sorry."
    
    "After..." 
    "(Visualist: JUST STOP SKIPPING DAMMIT!) (K!) (THE FISH)"
    "(After a long time, the author became a retard and proceeded to dab while watching anime all day. The end)"
    
    "After a while I passed out."
    
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
    
    "I buttoned down the shirt with a smirk."
    
    "Old man Kukichi watched us with anticipation."
    
    "I moved to the middle ground to come face to face with Rina."
    
    mc "Rina-nee, you move first."
    
    r "Well, you'll regret that!"
    
    "*Fush*"
    
    "Fast!"
    
    "A right fast jab appeared."
    
    "I moved my head to the side to avoid the jab."
        
    "Rina swung her left fist aiming at [mc]'s stomach"
    
    "I moved my hand to stop her swing and proceeded with a uppercut with my other hand"
    
    "Rina jumped back while her right hand blocked the uppercut."
    
    r "You're still like a demon as usual."
    
    mc "Is that praise?"
     
    "Rina run towards me before lowering her body in order to tackle my leg down."
     
    "I jumped in the air but Rina swang her hand straight to my face."
     
    "I moved my head a few breaths earlier than her, then I landed on the ground."
     
    "I instinctively grabbed her karate uniform and threw her in air with a perfect fluid movement."
     
    "Rina flew in air before landing with a thud."
     
    r "*rubs head* Ouch! That hurts!"
     
    mc "A moment of hesistation is the same as giving your life up."
     
    o "Hahahaha! As expected of [mc]! I have great expectations for your future in martial arts."
     
    mc "Of course! *ready both hands on side and breaths in and exhales lightly*"
    
    a "Splendid as always,[mc]!"
     
    s "Yeah!"
     
    a "Seeing Rina couldn't contend with you shows she is not as perfect as she seems to be."
     
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
     
    "I replied and took a bath after that."
    
    "I replied to Ellyn, my internet bestfriend."
     
    mc "'Sorry, Ellyn. It was a quite busy day.'"
    
    e "'It's fine.'"
    
    e "'I know you had a busy day. Good night,[mc].'"
    
    "I closed my phone and went to sleep."
    
    "It was a busy day..."
    
    "..."
    
    stop music fadeout 3.0
    return