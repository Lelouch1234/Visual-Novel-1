label ch1:
    stop music fadeout 4.0
    scene black
    play music audio.t5
    $ config.rollback_enabled = False
    
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
        
        "Tell her my name.": #choiçe 1
            
            jump choice1
        
        "Go away from her.": #choice 2
            
            jump choice2
            

label choice1:
    $ mc = renpy.input("Please insert your name")
    
    $ mc = mc.strip()
    
    mc "My name is [mc]."

    jump done1

label choice2:
    stop music fadeout 3.0
    play music audio.t2
    
    "I stand up in front of her and leave her as fast as I can."
            
    "That girl look me go away from her and look down."
            
    "I guess that is the best way for her to leave me alone."
    
    "I keep running without looking back..."
    
    "Keep running..."
    
    "BAD END"
    
    n "I never though this ending so fast at first chapter. Well, try to play again."
    
    stop music fadeout 3.0
    
    return
    
label done1:
    g "Nice to meet you, [mc]"
    
    mc "Y-yeah, me too."
    
    "This is first time I talking with girl."
    
    "I can't bring myself to see her face."
    
    g "Are you ok [mc]?"
    
    mc "Yeah, Im good."
    
    "Maybe I should ask her name since she already asked!j my name."
    
    mc "Can I have your name?"
    
    g "Oh, I forget to intro myself. My Bad."
    
    a "My name is [a] and we are classmates."
    
    "Eh?"
    
    "Classmates?"
    
    "And her name is Alice, Alice, Alice..... Ah I remember her. Her desk is beside me."
    
    a "[mc]?"
    
    mc "Oh, I'm sorry. I forgot about you since I never talked with the girl."
    
    a "Oh I see. So this is the first time you talking with a girl like me?"
    
    mc "Yes.*Blushing*"
    
    a "Hahaha. You are so cute when you blushing."
    
    "She keep laughing at me while I'm stuck and clueless."
    
    "Then situations getting awkward for me."
    
    a "Then can you be my friend, [mc]?"
    
    "This will change my daily life."
    
    "My daily life with a girl..."
    
    "Eh, What the heck Im thinking?"
    
    a "[mc]?"
    
    mc "Oh sorry. I'm just thinking something."
    
    a "You still not answer my question yet."
    
    mc "sure."
    
    mc "This is my first time I make a friend with a girl."
    
    "I guess what happen tomorroww...."
    
    a "Well the lunch is almost over. Should we head back to the class?"
   
    mc "Ok then. Let's go."
    
    "While we are on the way to the class, my head suddenly feels dizzy"
    
    "Did I eat something wrong?"
    
    "My body getting numb. I can't feel my legs."
    
    a "[mc]? What's wrong with you??"
    
    "My visual is getting blurred..."
    
    "Then I suddenly vomit at hallways and lying down.."
    
    a "Someone help me!!!"
    
    "I close my eyes and my body its feeling hurt."
    
    a "Someone help me please!! HELP ME!!!"
    
    "It's hurt"
    
    s "What is happen to him??"
    
    a "I don't know what happen."
    
    s "We need to get him to Nurse Room fast!!"
    
    s "Everyone pick him up."
    
    "I think I'm gonna pass out...."
    
    "..."
    stop music fadeout 3.0
    #the screen will disolve here to show mc pass out.
    #play music audio.
    mc "Ugh..Where am I?"
    
    "I try to focus my sense and looking around"
    
    mc "Huh who is that?"
    
    "Wait is that Alice?"
    
    "To think she can be here with me. She must be alone.."
    
    "Eh wait...Why she want to friend with me? I thought she has many friends."
    
    "Ah never mind that. Now I want to know what happen to me.."
    
    a "Ah [mc] did you just wake up?"
    
    mc "Yes maybe.."
    
    a "Are you sure??"
    
    mc "Ah never mind that. Yeah I'm good right now even my head just little dizzy for what happened to me."
    
    mc "Can I know what happen to me?"
    
    a "How should I say?"
    
    a "You were vomit at hallways and pass out"
    
    mc "because what?"
    
    a "Hmm...I think you eat poison food. I guess"
    
    "She smile at me"
    
    mc "Poison food? What did I eat?"
    
    a "I don't know. You remember what you eat?"
    
    mc "Hmm...I think I just eat sandwich omelette"
    
    a "Did you feel something when you eat sandwich?"
    
    mc "Hmm...I don't know what taste I have when eat that but I remember it feels like horrible."
    
    a "Then why you eat that?"
    
    mc "I just feel hungry suddenly"
    
    a "Ah I see"
    
    mc "Before that, Why are you here? How about class?"
    
    a "Thats secret and don't worry about class. I can handle it."
    
    mc "Ok then..."
    
    a "Do you feel better now? We should head to the class and report the situation."
    
    mc "Ah yes. Let's go then."
    
    "We go out from Nurse Room and go head to the class"
    
    mc "Have you meet doctor while I'm pass out?"
    
    a "No"
    
    mc "Eh? Really? Then who heal me?"
    
    a "No one"
    
    mc "Huh?"
    
    "But I feel something odd about this. This place is too queit."
    
    "When we open the door class, "
    
    "TO BE CONTINUE..."
    
    n "This is the end of the first chapter. Soon we will put a new chapter in this Visual Novel. Thanks for playing."
      
    stop music fadeout 3.0 
    
    return
    
    
    
