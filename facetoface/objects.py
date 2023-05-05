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

pineapple = Fruits(name='Pineapple',  
                t1='its a acid fruit', 
                t2='its yellow', 
                t3='its difficult to peel', 
                t4='some people eat this fruit wih cinnamon ', 
                t5='has a crown')

mango = Fruits(name='Mango',  
                t1='has a pit', 
                t2='its yellow and red', 
                t3='has a "milk"', 
                t4='some people eat this fruit wih salt ', 
                t5='your tree is big')

fruit_objects = [blackberry, banana, apple, pineapple, ]
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

natiruts = Singer(name='Natiruts',  
                m1='Andei só', 
                m2='Me namora', 
                m3='Quero ser feliz também', 
                m4='Sorri, sou rei', 
                m5='Voce me encantou demais')

tim_maia = Singer(name='Tim Maia',  
                m1='Azul da cor do mar', 
                m2='Me de motivo', 
                m3='Gostava tanto de voce', 
                m4='Que beleza', 
                m5='Ela partiu')



singer_objects = [drake, post_malone, eminem, natiruts, tim_maia]
select_singer = random.choice(singer_objects)
