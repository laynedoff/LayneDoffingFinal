import random

checked_bag = False
regret_ending=False
    



def main():
    print("""
--Welcome to 'The Next Town Over', a mini choose-your-own adventure text-based game!--
          
Our story starts in a small town, in rural America, circa the 1870's. Tensions are high here in the South, the end of the Civil War bringing just as much pain and suffering as it did grant freedom to others. Those who were now set free still struggling with day-to-day life and discrimination, while others deal with the deaths of their fathers or sons in the war.
But even despite the extrodinary changes that have already occured, there is still more to come.

Join MAX, the protagonist of this story, as he finds his place in the changing world. Follow along, and help MAX make good decisions. Or don't. I'm not your mom.

MAX finds himself on the outskirts of the town he was born and raised in, the hot afternoon sun high in the sky.
Before him lays the one road that leads in and out of town. He has been steeling his nerves for weeks, finally able to stand by the road, his horse (SILO) by his side as he contemplates his decision.""")
    choice_1 = input("""
    What should MAX do?
                     
Type the number of the option you'd like to pick:
    1. Hop on that horse, MAX, and get to movin'! (Continue forward.)
    2. Wait. Has MAX even prepared for this trip? (Observe your surroundings.)
    3. Screw this! Adventure will lead to nothin' but trouble. Go home, MAX. (Cowardly choice.)
""")
    
    if choice_1!="1":
        if choice_1=="2":
            print(
    """Has MAX prepared for this trip?
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