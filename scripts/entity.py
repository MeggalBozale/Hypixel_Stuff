

class Entity:
    def __init__(self, name, hp, level, drops=False):
        self.name = name
        self.hp = hp
        self.level = level
        self.drops = drops if drops else {} # Dict with keys holding lists [chance, (amt_min, amt_max)]

    def add_drops(self, new_drops):
        """Add new drops to the existing dict. Useful for.. something"""
        for new_key, new_value in new_drops:
            # This will overwrite in the event of keys already existing
            self.drops[new_key] = new_value
    
    def set_drops(self, new_drops):
        """Set the entity drops to a new dict. Useful if not declared immediately."""
        self.drops = new_drops
                
zombie_drops = {"coins":[1.0,(1,3)], "rotten-flesh"}
zombie = Entity("Zombie",20,1)

