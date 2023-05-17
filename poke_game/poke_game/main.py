import random
import inquirer
class Pokemon:
    """
    Classe mãe que contem as contem as caracteristiscas do pokemon
    """
    def __init__(self, name, life, damage, velocity, mov):
        self.__name = name
        self.life = life
        self.__damage = damage
        self.__velocity = velocity
        self.__mov = mov

    @property
    def name(self):
        return self.__name
    
    # @property
    # def life(self):
    #     return self.__life
    
    @property
    def damage(self):
        return self.__damage
    
    @property
    def velocity(self):
        return self.__velocity
    
    @property
    def mov(self):
        return self.__mov
    
    def choose_mov(self):
        move_selected = inquirer.prompt([
            inquirer.List('moves',
                        message="||SELECT YOUR ATTACK BRO||",
                        choices=[self.mov],
                        ),
        ])
        return move_selected['moves']


class Fire(Pokemon):
    """
    Classe filha, que está herdando de Pokemon e lhe dando um elemento
    """
    def __init__(self, name, life, damage, velocity, mov, type):
        super().__init__(name , life, damage, velocity, mov)
        self.tpye = type

    @staticmethod
    def advantage(type, damage):
        if type == "Water":
            damage = damage*0.10
            return damage
        else:
            return damage

    def attack(self, bot_type, damage):
        damage = self.advantage(bot_type, damage)
        damage = self.choose_mov()
        return damage

class Plaint(Pokemon):
    """
    Classe filha, que está herdando de Pokemon e lhe dando um elemento
    """
    def __init__(self, name, life, damage, velocity, mov, type):
        super().__init__(name , life, damage, velocity, mov)
        self.type = type

    @staticmethod
    def advantage(type, damage):
        if type == "Fire":
            return False
        elif type == "Water": #grass
            damage = damage*0.10
            return damage
        else:
            return damage

class Water(Pokemon):
    """
    Classe filha, que está herdando de Pokemon e lhe dando um elemento
    """
    def __init__(self, name, life, damage, velocity, mov, type):
        super().__init__(name , life, damage, velocity, mov)
        self.type = type

    @staticmethod
    def advantage(type, damage):
        if type == "Plaint":
            pass
        elif type == "Fire": #grass
            damage = damage*0.10
            return damage
        else:
            return damage


treeko = Plaint("Treeko", 40, 45, 70, "Bullet Seed", "Plaint") #OBJETO CRIANDO POKEMON
moltres = Fire("Moltres", 90, 100, 90, "Ancient Power", "Fire")
lapras = Water("Lapras", 130, 85, 60, "Hydro Pump", "Water")

pokemons = [treeko, moltres, lapras]


def choose_pokemon():
    import inquirer
    poke_selected = inquirer.prompt([
        inquirer.List('pokes',
                      message="||SELECT YOUR POKEMON BRO||",
                      choices=[*pokemons],
                      ),
    ])
    return poke_selected['pokes']
    # match poke_selected['pokes']:
    #     case "Treeko":
    #         poke = treeko
    #         return poke
    #     case "Moltres":
    #         poke = moltres
    #         return poke
    #     case "Lapras":
    #         poke = lapras
    #         return poke


def poke_bot():
    pok_bot = random.choice(pokemons)
    if pok_bot == treeko.name:
        pok_bot = treeko
    elif pok_bot == moltres.name:
        pok_bot = moltres
    elif pok_bot == lapras.name:
        pok_bot = lapras
    return pok_bot


def loose_hp(player_one, player_bot):
    atk = player_one.attack(player_bot.type, player_one.damage)
    print(atk)
    loose_hp_bot = player_bot.life - atk
    print(loose_hp_bot)

    return loose_hp_bot


def gameplay():
    player_one = choose_pokemon()
    player_bot = poke_bot()
    while player_one.life > 0 and player_bot.life > 0:
        if player_one.velocity >= player_bot.velocity:
            player_one.advantage(player_bot.type, player_one.attack(player_bot.type, player_one.damage))
            player_one.choose_mov()

            loose_hp(player_one, player_bot)
        else:
            print("baaba")

    # if player_one.velocity < player_bot:
    #     ...
    print(player_one)
    print(player_bot)
    print(player_one.mov)
    # if player_one.velocity < player_bot.velocity:
    #     player_one.advantage(player_bot.type)



gameplay()
#SEPAIR THE CODE / FINISH THE LOGIC 
