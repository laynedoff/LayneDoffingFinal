import random




def observe_check(observation, difficulty):
    num_list = [1, 2, 3, 4, 5, 6]
    observation += int((random.choice(num_list)))
    if observation>=difficulty:
        return True
    else:
        return False

def charisma_check(charisma, difficulty):
    num_list = [1,2,3,4,5,6]
    charisma += int((random.choice(num_list)))
    if charisma>=difficulty:
        return True
    else:
        return False

def strength_check(strength, difficulty):
    num_list = [1,2,3,4,5,6]
    strength += int((random.choice(num_list)))
    if strength>=difficulty:
        return True
    else:
        return False

def main():
    global checked_bag
    skill_points = 10
    print("""
--Welcome to 'The Next Town Over', a mini choose-your-own adventure text-based game!--
          
First things first, you will be given 10 skill points which you will be able to distribute how you please among 3 areas: OBSERVATION, CHARISMA, and STRENGTH.
Your points will determine whether or not you are able to make certain decisions sucessfully.
          """)

    observation = int(input("Enter a number 0-10 to attribute to OBSERVATION: "))
    skill_points -= observation

    if skill_points==0:
        print("""
              You have no more skill points to distribute.""")
        charisma = 0
        strength = 0
        input("Enter any key to continue: ")
    else:
        charisma = int(input(f"You have {skill_points} skill points left to use. Enter a number 0-{skill_points} to attribute to CHARISMA: "))
        skill_points -= charisma
        if skill_points == 0:
            print("""
                  You have no more skill points to distribute.""")
            strength = 0
            input("Enter any key to continue: ")
        else:
            strength = int(input(f"You have {skill_points} skill points left to use. Enter a number 0-{skill_points} to attribute to STRENGTH: "))
            skill_points-=strength
            if skill_points!=0:
                print(f"""
You have {skill_points} skill point(s) left over, would you like to use them?""")
                answer = input("Type 'y' for yes or 'n' for no: ")
                if answer =="y":
                    add_point = input("You may choose one skill to add your remaining points. Type 'o' for OBSERVATION, 'c for CHARISMA, or 's' for STRENGTH: ")
                    if add_point == "o":
                        observation += 1
                        if add_point =="c":
                            charisma += 1
                            if add_point == "s":
                                strength += 1

    input(f"""
          Your stats are OBSERVATION: {observation}, CHARISMA: {charisma}, and STRENGTH: {strength}.
          
Press Enter to continue.""")
    
    print("""
    Our story starts in a small town, in rural America, circa the 1870's. Tensions are high here in the South, the end of the Civil War bringing just as much pain and suffering as it granted freedom to others. Those who were now set free still struggle with day-to-day life and discrimination, while others deal with the deaths of their fathers, sons, and brothers from the war.

    Despite the extrodinary changes that have already occured, there are still more to come.

Join MAX, the protagonist of this story, as he finds his place in the changing world. Follow along, and help MAX make good decisions. Or don't. I'm not your mom.
""")
    input("Press Enter to continue ")
    print("""
    MAX finds himself on the outskirts of the town he was born and raised in, the hot afternoon sun high in the sky.
Before him lays the one road that leads in and out of town. He has been steeling his nerves for weeks, finally able to stand by the road, his horse (SILO) by his side as he contemplates his decision: Should he leave home?""")
    choice_1 = input("""
    What should MAX do?
                     
Type the number of the option you'd like to pick:
    1. Hop on that horse, MAX, and get to movin'! (Continue forward.)
    2. Wait. Has MAX even prepared for this trip? (OBSERVE your surroundings.)
    3. Screw this! Adventure will lead to nothin' but trouble. Go home, MAX. (Cowardly choice.)
""")
    
    if choice_1!="1":
        if choice_1=="2":
            print(
    """
    Has MAX prepared for this trip?""")
            if observe_check(observation,3)==True: # 3 is the difficulty of the check. lower number are easier checks.
                checked_bag=True
                print("""(You passed an OBSERVATION check.)
                      
Hanging from SILO's saddle are two storage bags, loaded with goods. Inside is enough food and water to last until reaching the next town over. Along side them are a few other object: a lantern, rope, and a map.""")
                choice_1=input("""
    Anything else you want to do?
                           
Type the number of the option you'd like to pick:
    1. Hop on that horse, MAX, and get to movin'! (Continue forward.)
    2. Wait. Has MAX even prepared for this trip? (OBSERVE your surroundings.)
    3. Screw this! Adventure will lead to nothin' but trouble. Go home, MAX. (Coward.)
""")
            else:
                print("""
For some reason, you can't quite tell what MAX is carrying with him, if anything. Oh well. 
                      
        (You failed an OBSERVATION check. You may retry the check or choose another choice.)""")
                choice_1 =input("""
Anything else you want to do?
                           
Type the number of the option you'd like to pick:
    1. Hop on that horse, MAX, and get to movin'! (Continue forward.)
    2. Wait. Has MAX even prepared for this trip? (OBSERVE your surroundings.)
    3. Screw this! Adventure will lead to nothin' but trouble. Go home, MAX. (Coward.)
""")
            
         ### choice 2 ^^^

        if choice_1=="3":
            print(("""
    Adventure will be nothing but trouble! Go home.
    
Alright then, I just hope you made the right call...
        
        """))
            input("Press Enter to continue:")
            print("""
                  



                                    |||GAME OVER|||
            You ended the story before it even began! I bet you're real fun at parties.
                  
                  
                  
                  



                  
                  """)
            quit()
            
        
        ### choice 3 ^^^
    if choice_1=="1":
        print("""
              
    Hop on that horse and get to movin'! Yeehaw!
              
MAX mounts SILO, kicking the spur of his boots into the large creatures' sides, urging him forward into a steady trot. Slowly picking up speed, a trail of dust is soon all that remains of them in town.
""")
           
        ## choice 1^^^
    input("""
Press Enter to continue:
          """)
    print("""For 45 minutes or so, there is nothing besides MAX, SILO, and the dirt and gravel road in any square-mile radius. The sun beats down on the man and his steed and they both perk up at the first sign of foliage. What starts as a few sparse dead trees is soon revealed to be the beginnings of a forest, the road narrowing down to a slim walking-trail through the dense brush. It's a heavenly escape from the sun, but MAX is whacked in the face with stray branches, sitting as high up as he is. Swatting at the branches, MAX doesn't notice when SILO comes to a complete halt.
          
          ???: 'Hey!' an angry looking woman shouts at MAX. She's no taller than five feet. She's a stout, black woman, getting on her years. 'What in the hell do you think you're doing here, mister?'
          """)

    choice_2 = input("""
          How should MAX respond to the MYSTERY WOMAN?
          
Type the number of the option you'd like to pick:
    1. Try to talk to her and calm her down. (Use your CHARISMA to sway her.)
    2. Giddyup on out of there! (Run!)
    3. Yell right back at her. (Make matters worse.)""")   

    if choice_2 =="1":
        print("""
Try and talk to her.
              """)
        if charisma_check(charisma, 5)==True:
            print("""(You passed a CHARISMA check)

MAX dismounts off his horse, and raises his hands up by his head, palms facing forward in a surrendering motion.
                  
                  MAX: 'My apologies, Ma'am. I mean no disrespect treadin' through here. I'm from a small town a little ways away and ain't ever left before now. It was my understandin' that this is the way to the city.'
                  
The woman eyes MAX suspiciously before her posture softens and her glare becomes less harsh. 
                  
                  ???: 'I suppose it's true you can come through this way to the city,' the woman seems to muse aloud. 'But I ain't seen any folk from your village in a long while. I'd say in the last fifteen years.' She raises an eyebrow at MAX prompting him to respond.
                  
                  MAX: 'Well...Ever since the War, and even a tad before then, my town was never too fond of gettin' involved in all that controversy and such.'
                  
                  ???: 'Controversy?' she parrots back to him. 'I ain't ever in my 60 years of livin' heard nobody call slavery a 'controversy. What a word.' She takes a moment to evaluate MAX again, looking him and SILO up and down. 'You two runnin' away from home?'
                  
                  MAX: 'No. Not quite. Just wanted to see what the world is like.'
                  
                  ???: 'What's your name, kid?'
                  
                  MAX: 'MAX, ma'am.'
                  
                  ???: 'Well, Max, my name is ALMA. Let me be the first to tell you that the world ain't all that great!' She huffs a laugh and reaches her arms out, gesturing to... the world.
                  """)
        else:
            print("""
            (You failed a CHARISMA check)
        
MAX straightens up on SILO, presenting his best posture before speaking. 
                  
                  MAX: 'No need to worry, woman. I only plan to tresspass until I get to the city!'
                  
The MYSTERY WOMAN keep the same glare directed toward him. MAX feels sweat beading on his neck.
                  
                  ???: 'Typicaly, tresspassing is not allowed at all,' her voice is stern and frankly, a little scary.""")
    if choice_2 == "2":
        print("""
    Run MAX, run!!!
              
MAX kicks into SILO's sides, startling the horse into movement.
              
              ???: 'GET BACK HERE,' the woman yells, her voice fading the farther away MAX rides.
            
Riding deeper into the forest, MAX realizes too late that he has veered off of the pre-established path in his urgent escape. He's lost.
              
MAX rides around for hours until nightfall, SILO and himself needing a break. In the daylight, the forest had been a haven from the sun, but now, it hid everything, not even the moon is able to shine through the canopy of trees. Every rustle of wind, every snapping twig and falling acorn sounds like danger. Praying for sleep to take him, MAX stares idly into the dark, leaning against a tree trunk while sat on the ground. Hopefully he'd be able to find his way home by morning...
              
              Wait a minute! Maybe he had something in his bag to help!
              """)
        input("""Press Enter to continue:
              """)
        if checked_bag==True:
            print("""(You OBSERVED MAX's bag earlier, granting you access to the items inside.)
                  
That's right, the lantern and the map! MAX sighs with relief, sagging further against the tree. He pulls the lantern out and lights it, careful to set it down away from any plants looking too dry. As a precaution, he takes the rope from his bag and hitches SILO to the tree he had been using to rest. Settling back down on the ground, MAX grabs the map from one of his bags and places it on the ground near the light, seeing if he can make out where he is. Listening closely, he can hear running water, so he narrows his position down to somewhere a long the river snaking through the forest. It probably would be easier to tell once it was morning. Feeling more at ease, MAX extinguishes the lantern, not wanting to attract any unwanted attention, and rests his eyes until morning.""")


if __name__=="__main__":
    main()