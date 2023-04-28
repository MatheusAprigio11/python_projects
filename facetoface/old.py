import random

class Fruits:
    def __init__(self, name, t1, t2, t3, t4, t5):        
        self.__name = name
        self.__tips = [t1, t2, t3, t4, t5]
        self.__life = 5

    @property
    def name(self):
        return self.__name
    
    @property
    def tips(self):
        return self.__tips
    
    @property
    def life(self):
        return self.__life

    def lose_life(self):
        self.__life -= 1


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



objects = [blackberry, banana, apple]
select_fruit = random.choice(objects)
print(select_fruit.life)

for i in range(select_fruit.life):
    print(f"\nTIP: {select_fruit.tips[i]}")
    print(f"LIFE: {select_fruit.life}")
    user_option = input("\ninput what u think>> ").title()
    if user_option != select_fruit.name:
        select_fruit.lose_life()
        print("\nYOU LOSE A LIFE!!")
        print("please try again\n")
    else:
        print("CONGRATS!! YOU TAKE IT BRO!")
        break
        
