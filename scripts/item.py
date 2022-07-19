import rarity

class Item:
    def __init__(self,name,amt,rarity_obj,costs,sellback):
        self.name = name
        self.amt = amt
        self.rarity = rarity_obj
        self.costs = costs # dict with source-price key-pairs
        self.sellback = sellback # ^^
    
    def get_cost(self,source):
        for key in self.costs:
            if key == source:
                return self.costs[key] * self.amt
        return -1

    def get_value(self,source):
        for key in self.sellback:
            if key == source:
                return self.sellback[key] * self.amt
        return -1

    def print_info(self):
        print(f"Item: {self.name}")
        print(f"Rarity: {str(self.rarity)}")
        sources = [['Bazaar','bz'],['NPC','npc']]
        costs, sellback = [], []
        for source in sources:
            cost = self.get_cost(source[1]) if self.get_cost(source[1]) > -1 else "Not buyable!"
            costs.append(cost)
            value = self.get_value(source[1]) if self.get_value(source[1]) > -1 else "Not sellable!"
            print(f"Buy/Sell on {source[0]}:  [{cost}, {value}] ")




def main():
    some_unpurchaseable_twigs = Item("Twig",31,rarity.common,{},{'npc':1,'bz':0.7})
    print(some_unpurchaseable_twigs.get_cost('bz'))
    print(some_unpurchaseable_twigs.get_value('bz'))
    print(some_unpurchaseable_twigs.get_value('npc'))
    
    some_unsellable_twigs = Item("Twig",7,rarity.uncommon,{'npc':1,'bz':0.3},{})
    print(some_unsellable_twigs.get_cost('bz'))
    print(some_unsellable_twigs.get_value('bz'))
    print(some_unsellable_twigs.get_value('npc'))

    some_unsellable_twigs.print_info()

if __name__ == "__main__":
    main()