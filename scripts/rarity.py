""" Defines a class which holds the name, integer tier, and color of each rarity.
also sets them up as lowercase objects, for Hypixel reasons. """

import paint

class Rarity:
    def __init__(self, name, value, color):
        self.name = name
        self.value = value
        self.color = color # iterable (r,g,b)

    def __str__(self):
        return paint.color(self.name, self.color)

common = Rarity("Common",0,(255,255,255))
uncommon = Rarity("Uncommon",1,(128,255,128))
rare = Rarity("Rare",2,(128,128,255))
epic = Rarity("Epic",3,(200,64,200))
legendary = Rarity("Legendary",4,(200,200,0))
mythic = Rarity("Mythic",5,(255,64,128))
divine = Rarity("Divine",6,(0,255,255))
special = Rarity("Special",7,(255,128,128))
very_special = Rarity("Very Special",7,(255,128,128))
unobtainable = Rarity("UNOBTAINABLE",666,(255,128,0))

tiers = (common, uncommon, rare, epic, legendary, mythic, divine, special, unobtainable)

# Run script to get list of all rarities as their respective color.

def main():
    for rarity in tiers:
        print(rarity)

if __name__ == "__main__":
    main()