class Physical_Chars:
    age = 0
    hair = ""
    eyes = ""
    skin = ""

class Stat:
    def __init__(self, number = 0, modifier = 0, proficiency = False):
        self.number = number
        self.modifier = modifier
        self.proficiency = proficiency

class Stats:
    strength = Stat()
    dexterity = Stat()
    constitution = Stat()
    intelligence = Stat()
    wisdom = Stat()
    charisma = Stat()

class Skills:
    acrobatics = Stat()
    animal_handling = Stat()
    arcana = Stat()
    athletics = Stat()
    deception = Stat()
    history = Stat()
    insight = Stat()
    intimidation = Stat()
    investigation = Stat()
    medicine = Stat()
    perception = Stat()
    performance = Stat()
    persuasion = Stat()
    religion = Stat()
    sleight_of_hand = Stat()
    stealth = Stat()
    survival = Stat()
    
class Character:
    name = "Unnamed"
    physical_chars = Physical_Chars()
    stats = Stats()
    skills = Skills()
    inventory = {}
