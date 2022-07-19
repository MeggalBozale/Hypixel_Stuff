
import rarity
import entity

class Sea_Creature(entity.Entity):
    def __init__(self, level_req, name, rarity_obj, chance, level, hp, loot_obj, xp, description):
        super().__init__(name, hp, level, loot_obj)
        self.level_req = level_req # Required fishing level to reel this up
        self.rarity = rarity_obj
        self.chance = chance # float between 0.0 to 1.0
        self.loot = loot_obj
        self.xp = xp
        self.description = description

