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
    def life():
        return self.__life

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


#preciso criar alguma funçao para escolha aleatoria das frutas e sorteamento das dicas.
