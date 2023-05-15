import random

class Pokemon:
    """
    Classe mãe que contem as contem as caracteristiscas do pokemon
    """
    def __init__(self, name, life, attack, velocity):
        self.__name = name
        self.__life = life
        self.__attack = attack
        self.__velocity = velocity

    @property
    def name(self):
        return self.__name
    
    @property
    def life(self):
        return self.__life
    
    @property
    def attack(self):
        return self.__attack
    
    @property
    def velocity(self):
        return self.__velocity
    

class Fire(Pokemon):
    """
    Classe filha, que está herdando de Pokemon e lhe dando um elemento
    """
    def __init__(self, name, life, attack, velocity, type):
        super().__init__(name , life, attack, velocity)
        self.tpye = type

    def advantage(self, type):
        if type == "Water":
            return False
        elif type == "Plaint":
            return True
        else:
            ... #RANDINT

class Plaint(Pokemon):
    """
    Classe filha, que está herdando de Pokemon e lhe dando um elemento
    """
    def __init__(self, name, life, attack, velocity, type):
        super().__init__(name , life, attack, velocity)
        self.type = type

class Water(Pokemon):
    """
    Classe filha, que está herdando de Pokemon e lhe dando um elemento
    """
    def __init__(self, name, life, attack, velocity, type):
        super().__init__(name , life, attack, velocity)
        self.type = type


treeko = Plaint("Treeko", 40, 45, 70, "Plaint") #OBJETO CRIANDO POKEMON
moltres = Fire("Moltres", 90, 100, 90, "Fire")
lapras = Water("Lapras", 130, 85, 60, "Water")

pokemons = [treeko.name, moltres.name, lapras.name]


def choose_pokemon():
    import inquirer
    poke_selected = inquirer.prompt([
        inquirer.List('pokes',
                      message="||SELECT YOUR POKEMON BRO||",
                      choices=[*pokemons],
                      ),
    ])
    match poke_selected['pokes']:
        case "Treeko":
            poke = treeko
        case "Moltres":
            poke = moltres
        case "Lapras":
            poke = lapras
    return poke


choose_pokemon()


def poke_bot():
    pok_bot = random.choice(pokemons)
    match poke[pok_bot]:
        case "Treeko":
            poke = treeko
        case "Moltres":
            poke = moltres
        case "Lapras":
            poke = lapras
    return pok_bot


def gameplay():
    player_one = choose_pokemon()
    player_bot = poke_bot()
    print(player_one)
    print(player_bot)
    # if player_one.velocity < player_bot.velocity:
    #     player_one.advantage(player_bot.type)



gameplay()


