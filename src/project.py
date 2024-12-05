import random

checked_bag = False
regret_ending=False


def observe_check(observation, difficulty):
    if observation>=difficulty:
        return True
    else:
        return False

    

def main():

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
        input("Enter any key to continue: ")
    else:
        charisma = int(input(f"You have {skill_points} skill points left to use. Enter a number 0-{skill_points} to attribute to CHARISMA: "))
        skill_points -= charisma
        if skill_points == 0:
            print("""
                  You have no more skill points to distribute.""")
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
          
Enter any key to continue.""")
    
    print("""
    Our story starts in a small town, in rural America, circa the 1870's. Tensions are high here in the South, the end of the Civil War bringing just as much pain and suffering as it granted freedom to others. Those who were now set free still struggle with day-to-day life and discrimination, while others deal with the deaths of their fathers, sons, and brothers from the war.
    Despite the extrodinary changes that have already occured, there are still more to come.

Join MAX, the protagonist of this story, as he finds his place in the changing world. Follow along, and help MAX make good decisions. Or don't. I'm not your mom.
""")
    input("Enter any key to continue: ")
    print("""
    MAX finds himself on the outskirts of the town he was born and raised in, the hot afternoon sun high in the sky.
Before him lays the one road that leads in and out of town. He has been steeling his nerves for weeks, finally able to stand by the road, his horse (SILO) by his side as he contemplates his decision.""")
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
    """Has MAX prepared for this trip?""")
            if observe_check(observation,3)==True: # 3 is the difficulty of the check. lower number are easier checks.
                print("""
Hanging from SILO's saddle are two storage bags, loaded with goods. Inside is enough food and water to last until reaching the next town over.""")
            choice_1=input("""
    Anything else you want to do?
                           
Type the number of the option you'd like to pick:
    1. Hop on that horse, MAX, and get to movin'! (Continue forward.)
    2. Wait. Has MAX even prepared for this trip? (Observe your surroundings.)
    3. Screw this! Adventure will lead to nothin' but trouble. Go home, MAX. (Coward.)
""")
         ### choice 2 ^^^

        if choice_1=="3":
            print(("""
    Adventure will be nothing but trouble! Go home.
    
Alright then, I just hope you made the right call...
        
        """))
            
        
        ### choice 3 ^^^
        if choice_1=="1":
            print("""Hop on that horse and get to movin'! Yeehaw!
MAX mounts SILO, kicking the spur of his boots into the large creatures' sides, urging him forward. Slowly picking up speed, a trail of dust is soon all that remains of them in town.
""")
           
        ## choice 1^^^


if __name__=="__main__":
    main()