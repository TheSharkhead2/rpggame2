
class Player:

    baseLevelXp = 100
    levelXpMulti = 5

    def __init__(self):
        self.health = 100 #not sure if health should be here or in different variable in a separate "fight" class/enviroment
        self.stamina = 100 #similar to health, may be moved
        self.gold = 0 #currency name up to change, "gold" for now
        self.level = 1 
        self.xp = 0
        self.inventory = {
            "weapons" : [],
            "headPieces" : [],
            "chestPieces" : [],
            "legPieces" : [],
            "footPieces" : [],
            "relics" : []
        } #inventory for weapons, armor, and relics
        self.equippedItems = {
            "weaponPrimary" : [],
            "weaponSecondary" : [],
            "headPiece" : [],
            "chestPiece" : [],
            "legPiece" : [],
            "footPiece" : [],
            "relic" : []
        } #to keep track of currently equipped weapons, armor, and relics

    def xp_gain(self, amount):
        #control level-up logic
        self.xp += amount
        while self.xp >= self._xp_level_limit():
            self.xp -= self._xp_level_limit()
            self.level += 1
            self._on_level()

    def _on_level(self):
        #level reward, possibly game overlay
        pass

    def _xp_level_limit(self):
        #returns xp needed for next level (exponential scale)
        return(self.baseLevelXp * self.levelXpMulti**(self.level - 1))