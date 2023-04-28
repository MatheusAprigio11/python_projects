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


class Singer:
    def __init__(self, name, m1, m2, m3, m4, m5):        
        self.__name = name
        self.__musics = [m1, m2, m3, m4, m5]
        self.__life = 5

    @property
    def name(self):
        return self.__name
    
    @property
    def musics(self):
        return self.__musics
    
    @property
    def life(self):
        return self.__life

    def lose_life(self):
        self.__life -= 1

