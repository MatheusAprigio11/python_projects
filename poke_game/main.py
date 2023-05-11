class Pokemon:
    def __init__(self, name, element, life, attack, velocity):
        self.__name = name
        self.__element = element
        self.__life = life
        self.__attack = attack
        self.__velocity = velocity

    @property
    def name(self):
        return self.__name
    
    @property
    def element(self):
        return self.__element
    
    @property
    def life(self):
        return self.__life
    
    @property
    def attack(self):
        return self.__attack
    
    @property
    def velocity(self):
        return self.__velocity
