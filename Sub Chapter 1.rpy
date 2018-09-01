label sub1:
    "I will rely on my beautiful Rina-nee!"
    
    "And my life story will change about me with her!"
    
    "I wonder about it..."

    "(Director: should we add this choice?)(Author: Hmm... maybe xD)"

    "I want to have a big house for me and her. Also, my child name is- eh wait this is too fast."

    "(Director: NANI KORE??*Angry*)(Author: Don't hold me back director! let me erase THIS RETARD and his sister!!!)"
    
    "Is someone talking about us?"

    jump route1

label sub2:
    r "Hmm, why?"
    
    jump sub3

label sub3:
    
    menu:
     mc "Umm..."
        
     "Because I want to go to school with you.": # 5
            
            jump sub4
        
     "Because you're my sister.": # 6
            
            jump sub4

label sub4:
    r "*Blushes*"
    
    m "[mc], stop flirting with your sister."
    
    mc "Sorry, mom."
    
    r "Ehem, I'll go with you today."
    
    "YES, I’m with a perfect student!"
    
    "Who can face me!?"
    
    "I went out after drinking a cup of good, black coffee."
    
    "I will need it after all the things I did last night."
    
    "Anime, MMO, DOTA, LOL, MONSTER HUNTER!"
    
    #scene
    
    "As I went out I saw a petite body with white hair and a cute face staring at me."
    
    "She waved her small and fragile hand at me with a innocent smile to follow."
    
    mc "Shiro-chan! Bonjour.(Suddenly speak French)"
    
    r "[mc], why are you speaking French? Do you know any other words?"
    
    mc "*flustered* I’m still learning! … Maybe."

    r "*Sigh* If you want, I can teach you French."
    
    menu:
        mc "Not interested, because..."
        
        "Martial arts all the way!": #choice 7
            
            jump sub5
            
        "I want to beat Bill Gates!": #choice 8
        
            jump sub8
            
        "I have anime to watch.": #choice 9
    
            jump sub7

label sub5:
    s "Eh~"
    
    s "[mc], you really want to?"
    
    r "I can't overtake [mc] in that part."
    
    jump sub8
    
label sub6:
    s "Eh~, [mc] you really want to?"
    
    mc "Not yet, but I will!"
    
    r "Hmm~, how will you beat Bill gates?"
    
    mc "By creating a new concept, theory and invention!"
    
    s "Is he kidding, Rina-neesan?"
    
    r "It’s kinda hard but I know [mc] can do it if he wants to!"
    
    jump sub8
    
label sub7:
    s "Eh~, [mc] you really want to?"
    
    mc "Hmph! Of course!"
    
    r "I have no doubt about this."
    
    mc "Hmph! *Damn proud face*"

    jump sub8
    
label sub8:
      
    s "Anyway, can I go to school with you?"
    
    mc "*Thinking*"
    
    menu:
        "Let's go!": 
            
            jump sub9
        
        "Is it okay?": 
            
            jump sub10
        
        "Let's go-nya~": 
            
            jump sub11
        
label sub9:
   s "Let's go!"
   
   jump sub12
    
label sub10:
    mc "I believe Shiro-chan is an exemplary student. Maybe I am forgetting something?"
    
    jump sub13
    
label sub11:
    s " Rawr~ *Innocent smile radiating*"
    
    jump sub12
    
label sub12:
    "Rina-nee, Shiro and me went to school."
    
    "We parted ways after a long happy chat with each other."
    
    jump route8

label sub13:
    s "Ah! Sorry [mc]-senpai! I need to give a speech at assembly for freshmen today!"
    
    mc "It's fine."
    
    "Shiro ran in a hurry."
     
    r "Well, let's go,[mc]."
     
    "After that, we parted ways."
     
    jump route8
     
label bad1:
    
    "Well..."
    
    "A strong throw by an expert"

    stop music fadeout 5.0
    
    "BAM!"
    
    "*Flew a few feet in air before hitting the wooden tiles with a thud*"
    
    r "Are you sure he's fine?"
    
    a "well, I'm not sure, but he's still breathing... *Poke* *Poke*"
    
    o "Well, this pervert can go die for all I care."

    "BAD ENDING"

    "Make sure to not think of this novel as hentai all the time...[mc]"
    
    return