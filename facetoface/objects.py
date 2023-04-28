from classes import Fruits, Singer
import random

#OBJECTS OF FRUITS CLASS
banana = Fruits(name='Banana',  
                t1='Yellow', 
                t2='A Long format', 
                t3='has not seeds', 
                t4='silver is a type', 
                t5='rich in vitamin C') 

apple = Fruits(name='Apple',  
                t1='Red but inside white', 
                t2='A Circle format', 
                t3='Its a name of brand', 
                t4='Some people peel to eat', 
                t5='Prohibited fruit')

blackberry = Fruits(name='Blackberry',  
                t1='can be red, black or white', 
                t2='its short', 
                t3='if you see a tree of this fruit in the street, you stop to take it.', 
                t4='Usualy the color stains your hand', 
                t5='Sour or So sweet.')

fruit_objects = [blackberry, banana, apple]
select_fruit = random.choice(fruit_objects)


#OBJECTS OF SINGER CLASS
drake = Singer(name='Drake',  
                m1='Gods Plan', 
                m2='Hotling Bling', 
                m3='No Guidance', 
                m4='Spin Bout U', 
                m5='Laugh Now Cry Later') 

post_malone = Singer(name='Post Malone',  
                m1='Congratulations', 
                m2='Rockstar', 
                m3='Sunflower(Miles Morales)', 
                m4='Psycho', 
                m5='Better Now') 

eminem = Singer(name='Eminem',  
                m1='Stan', 
                m2='Without me', 
                m3='Mockingbird', 
                m4='Stan', 
                m5='Lose Yourself') 


singer_objects = [drake, post_malone, eminem]
select_singer = random.choice(singer_objects)
