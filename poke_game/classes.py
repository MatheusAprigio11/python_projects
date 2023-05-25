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
        super().__init__(name, life, damage, velocity, mov)
        self.type = type

    def advantage(self, type, damage):
        critical = damage * random.uniform(0.25, 0.35)
        normal_atk = damage * random.uniform(0.15, 0.24)
        wrong_atk = 0
        atks = [critical, normal_atk, wrong_atk]
        atks_dif_typ = [normal_atk, wrong_atk]

        if type == "Water":
            damage = random.choice(atks_dif_typ)
            if damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage
        elif type == "Plaint":
            damage = random.choice(atks)
            if damage == critical:
                print("ITS SUPER EFFECTIVE")
            elif damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage
        else:
            damage = random.choice(atks)
            if damage == critical:
                print("ITS SUPER EFFECTIVE")
            elif damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage

    # def attack(self, bot_type, damage):
    #     damage = self.advantage(bot_type, damage)
    #     return damage


class Plaint(Pokemon):
    """
    Classe filha, que está herdando de Pokemon e lhe dando um elemento
    """

    def __init__(self, name, life, damage, velocity, mov, type):
        super().__init__(name, life, damage, velocity, mov)
        self.type = type

    def advantage(self, type, damage):
        critical = damage * random.uniform(0.25, 0.35)
        normal_atk = damage * random.uniform(0.15, 0.24)
        wrong_atk = 0
        atks = [critical, normal_atk, wrong_atk]
        atks_dif_typ = [normal_atk, wrong_atk]

        if type == "Fire":
            damage = random.choice(atks_dif_typ)
            if damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage

        elif type == "Water":
            damage = random.choice(atks)
            if damage == critical:
                print("ITS SUPER EFFECTIVE")
            elif damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage
        else:
            damage = random.choice(atks)
            if damage == critical:
                print("ITS SUPER EFFECTIVE")
            elif damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage


class Water(Pokemon):
    """
    Classe filha, que está herdando de Pokemon e lhe dando um elemento
    """

    def __init__(self, name, life, damage, velocity, mov, type):
        super().__init__(name, life, damage, velocity, mov)
        self.type = type

    def advantage(self, type, damage):
        critical = damage * random.uniform(0.25, 0.35)
        normal_atk = damage * random.uniform(0.15, 0.24)
        wrong_atk = 0
        atks = [critical, normal_atk, wrong_atk]
        atks_dif_typ = [normal_atk, wrong_atk]

        if type == "Plaint":
            damage = random.choice(atks_dif_typ)
            if damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage
        elif type == "Fire":
            damage = random.choice(atks)
            if damage == critical:
                print("ITS SUPER EFFECTIVE")
            elif damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage
        else:
            damage = random.choice(atks)
            if damage == critical:
                print("ITS SUPER EFFECTIVE")
            elif damage == normal_atk:
                print("ISN'T EFFECTIVE")
            else:
                print("WRONG THE ATTACK")
            return damage

